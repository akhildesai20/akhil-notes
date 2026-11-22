#!/usr/bin/env python3
"""Compile Akhil Notes from committed UFOs, or regenerate masters from provenance.

Public / CI default: ``--from-ufo`` (compile only). Does not touch ``sources/masters/``.
Maintainer-only: ``--from-provenance`` regenerates UFOs from the private TTF, then compiles.

The generator preserves every original encoded outline except the intentional
``REBUILD_FIGURES`` set. Glyphs that were not in the 491-character release stay
constructed and are recorded as provisional.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import subprocess
import sys
import unicodedata as ud
from collections import defaultdict
from pathlib import Path

from fontTools.feaLib.builder import addOpenTypeFeaturesFromString
from fontTools.ttLib import TTFont, newTable
from fontTools.varLib.instancer import instantiateVariableFont
from glyphsLib.glyphdata import get_glyph
import glyphsets

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import build  # noqa: E402

SRC = ROOT / "provenance" / "AkhilsNotes-Variable.ttf"
SHA_PATH = ROOT / "reference" / "input-sha256.txt"
SOURCES = ROOT / "sources"
MASTER_DIR = SOURCES / "masters"
FEATURE_DIR = SOURCES / "features"
FONT_DIR = ROOT / "fonts"
QA = ROOT / "qa" / "candidate"
SETS = ("GF_Latin_Core", "GF_Latin_Plus", "GF_Latin_Vietnamese")
GLYPHSETS_COMMIT = "1dbbd54ea7bf3a3e94422c746be4da2741379d0b"
GUIDE_COMMIT = "355e4599ae45a8a05a42a57e8c5bbf79c821a4a5"
VERSION = (2, 101)
# Public git URL — last packaging step. Until set, designer URL stands in the copyright line.
REPO_URL = "https://github.com/akhildesai20/akhil-notes"
DESIGNER_URL = "https://www.instagram.com/akhilius_"
OFL_LICENSE = (
    "This Font Software is licensed under the SIL Open Font License, Version 1.1. "
    "This license is available with a FAQ at: https://openfontlicense.org"
)
OFL_URL = "https://openfontlicense.org"


def project_copyright() -> str:
    url = REPO_URL or DESIGNER_URL
    return f"Copyright 2026 The Akhil Notes Project Authors ({url})"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


class PreservingMaster(build.Master):
    """Keep every encoded glyph from the release. Construct only missing codepoints.

    Small figures in REBUILD_FIGURES are intentionally redrawn so supers/subs/fractions
    keep the same stem weight as the full digits.
    """

    def make(self, cp, cs, advance=None, mark=False, already_slanted=False, name=None, keep_advance=False):
        if cp is not None and cp in self.orig and cp not in build.REBUILD_FIGURES:
            return self.cmap[cp]
        return super().make(cp, cs, advance, mark, already_slanted, name, keep_advance)


def real_points(font, name):
    glyph = font["glyf"][name]
    if glyph.isComposite():
        rename = {str(i): n for i, n in enumerate(build.DIGITS)}
        return ("composite", tuple(
            (rename.get(c.glyphName, c.glyphName), int(c.x), int(c.y), int(c.flags))
            for c in glyph.components
        ))
    if glyph.numberOfContours <= 0:
        return ("empty", ())
    coords, ends, _flags = glyph.getCoordinates(font["glyf"])
    count = ends[-1] + 1
    return ("simple", tuple((int(coords[i][0]), int(coords[i][1])) for i in range(count)))


def verify_source() -> None:
    expected = SHA_PATH.read_text(encoding="utf-8").strip().lower()
    got = sha256(SRC)
    if got != expected:
        raise SystemExit(f"Refusing to build. SHA-256 {got} != {expected}")


def production_maps():
    wanted = {}
    conflicts = []
    unencoded = []
    for set_name in SETS:
        for gname in glyphsets.glyphs_in_glyphset(set_name):
            info = get_glyph(gname)
            if not info.unicode:
                unencoded.append(gname)
                continue
            cp = int(info.unicode, 16)
            prev = wanted.get(cp)
            if prev and prev != gname:
                conflicts.append((hex(cp), prev, gname, set_name))
                continue
            wanted[cp] = gname
    return wanted, sorted(set(unencoded)), conflicts


def rename_glyph(font, old, new):
    if old == new or old not in font.getGlyphOrder():
        return
    order = [new if n == old else n for n in font.getGlyphOrder()]
    glyf = font["glyf"]
    glyf.glyphs[new] = glyf.glyphs.pop(old)
    for g in glyf.glyphs.values():
        if g.isComposite():
            for comp in g.components:
                if comp.glyphName == old:
                    comp.glyphName = new
    font["hmtx"].metrics[new] = font["hmtx"].metrics.pop(old)
    font.setGlyphOrder(order)
    glyf.glyphOrder = order
    for table in font["cmap"].tables:
        if table.isUnicode():
            table.cmap = {cp: new if n == old else n for cp, n in table.cmap.items()}


def rename_master(master, mapping):
    for old, new in mapping.items():
        rename_glyph(master.f, old, new)
    master.cmap = {cp: mapping.get(n, n) for cp, n in master.cmap.items()}
    master.new = {mapping.get(n, n): v for n, v in master.new.items()}
    master.source = {mapping.get(n, n): v for n, v in master.source.items()}
    master.stacks = {k: mapping.get(v, v) for k, v in master.stacks.items()}
    master.f["maxp"].numGlyphs = len(master.f.getGlyphOrder())


def delete_glyph(master, name):
    font = master.f
    if name not in font.getGlyphOrder():
        return
    order = [n for n in font.getGlyphOrder() if n != name]
    font.setGlyphOrder(order)
    font["glyf"].glyphs.pop(name, None)
    font["glyf"].glyphOrder = order
    font["hmtx"].metrics.pop(name, None)
    font["maxp"].numGlyphs = len(order)
    master.new.pop(name, None)
    master.source.pop(name, None)


def add_whitespace(master):
    cmap = master.cmap
    space = cmap[0x20]
    aw = master.f["hmtx"][space][0]
    if 0xA0 not in cmap:
        master.make(0xA0, master.get(space), aw, already_slanted=True, name="nbspace")
    if 0x00 not in cmap:
        master.make(0x00, [], 0, name="NULL")
    if 0x0D not in cmap:
        master.make(0x0D, [], 0, name="CR")
    if 0x2028 not in cmap:
        master.make(0x2028, [], aw, name="uni2028")
    if 0x2029 not in cmap:
        master.make(0x2029, [], aw, name="uni2029")


def production_mapping(master, wanted):
    mapping = {}
    taken = set(master.f.getGlyphOrder())
    for cp, name in list(master.cmap.items()):
        target = (wanted.get(cp, name) or name).replace("-", ".")
        if cp == 0x25CC:
            target = "dottedcircle"
        if cp == 0x00A0:
            target = "uni00A0"
        if target == name or not target:
            continue
        if target in taken and target != name:
            continue
        mapping[name] = target
        taken.discard(name)
        taken.add(target)
    return mapping


def rename_fea(fea, mapping):
    for old, new in sorted(mapping.items(), key=lambda item: len(item[0]), reverse=True):
        fea = re.sub(rf"(?<![\w.]){re.escape(old)}(?![\w.])", new, fea)
    return fea


def strip_experimental(fea: str) -> str:
    fea = re.sub(r"feature calt \{.*?\n\} calt;\n", "", fea, flags=re.S)
    fea = re.sub(r"feature salt \{.*?\n\} salt;\n", "", fea, flags=re.S)
    return fea


def fix_frac(fea: str) -> str:
    """Put fraction steps in separate lookups so each sees the previous substitution."""
    digits = "[zero one two three four five six seven eight nine]"
    numr = "[zero.numr one.numr two.numr three.numr four.numr five.numr six.numr seven.numr eight.numr nine.numr]"
    dnom = "[zero.dnom one.dnom two.dnom three.dnom four.dnom five.dnom six.dnom seven.dnom eight.dnom nine.dnom]"
    replacement = (
        f"lookup FracSlash {{ sub {digits} slash' {digits} by fraction; }} FracSlash;\n"
        f"lookup FracNum1 {{ sub {digits}' lookup NumSub fraction; }} FracNum1;\n"
        f"lookup FracNum2 {{ sub {digits}' lookup NumSub {numr}; }} FracNum2;\n"
        f"lookup FracNum3 {{ sub {digits}' lookup NumSub {numr}; }} FracNum3;\n"
        f"lookup FracNum4 {{ sub {digits}' lookup NumSub {numr}; }} FracNum4;\n"
        f"lookup FracDen1 {{ sub fraction {digits}' lookup DenSub; }} FracDen1;\n"
        f"lookup FracDen2 {{ sub {dnom} {digits}' lookup DenSub; }} FracDen2;\n"
        "feature frac { lookup FracSlash; lookup FracNum1; lookup FracNum2; lookup FracNum3; lookup FracNum4; "
        "lookup FracDen1; lookup FracDen2; } frac;"
    )
    return re.sub(r"feature frac \{.*?\} frac;", replacement, fea, count=1, flags=re.S)


def add_dotted_circle(master):
    """U+25CC is the base the mark checks attach to. It is a ring of dots, not a letter."""
    if 0x25CC in master.cmap:
        return
    left, bottom, right, top = build.bounds(master.upright("o"))
    cx, cy = (left + right) / 2, (bottom + top) / 2
    radius_x, radius_y = (right - left) / 2 * 0.92, (top - bottom) / 2 * 0.92
    dot_radius = master.width * 0.42
    contours = []
    for index in range(12):
        angle = -math.pi / 2 + 2 * math.pi * index / 12
        contours.append(build.circle(
            cx + radius_x * math.cos(angle),
            cy + radius_y * math.sin(angle),
            dot_radius,
        ))
    advance = master.f["hmtx"][master.cmap[ord("o")]][0]
    master.make(0x25CC, contours, advance, name="dottedcircle")


def anchor_dotted_circle(fea: str, master) -> str:
    name = master.cmap[0x25CC]
    left, bottom, right, top = build.bounds(master.upright(name))
    center = (left + right) / 2
    above = top + max(25, master.width * 0.30)
    below = bottom - max(18, master.width * 0.25)
    shear = master.shear
    line = (
        f"pos base {name} "
        f"<anchor {build.otRound(center + shear * above)} {build.otRound(above)}> mark @top "
        f"<anchor {build.otRound(center + shear * below)} {build.otRound(below)}> mark @bottom "
        f"<anchor {build.otRound(right - 30 + shear * (top - 100))} {build.otRound(top - 100)}> mark @horn "
        f"<anchor {build.otRound(right + 65 + shear * (top - 110))} {build.otRound(top - 110)}> mark @caron;"
    )
    return fea.replace("} mark;", line + "\n} mark;", 1)


def add_soft_dot(fea: str, master) -> str:
    """Drop the dot of i/j when a below mark sits between the letter and an above mark."""
    idot = master.cmap[ord("ı")]
    jdot = master.cmap[ord("ȷ")]
    below = " ".join(master.cmap[cp] for cp in (0x323, 0x326, 0x327, 0x328))
    rules = [
        f"sub i' @BelowMarks @AboveMarks by {idot};",
        f"sub j' @BelowMarks @AboveMarks by {jdot};",
    ]
    # Only when an above mark follows. Standalone į stays the original drawing.
    for cp, below_cp in ((0x1ECB, 0x323), (0x012F, 0x328)):
        if cp in master.cmap and below_cp in master.cmap:
            rules.append(
                f"sub {master.cmap[cp]}' @AboveMarks by {idot} {master.cmap[below_cp]};"
            )
    block = "@BelowMarks = [" + below + "];\nfeature ccmp { " + " ".join(rules) + " } ccmp;\n"
    return fea.replace("} ccmp;\n", "} ccmp;\n" + block, 1)


def class_kern(masters, pairs):
    """Share a base letter's kerning with accented letters whose metrics match."""
    m0 = masters[0]
    glyphs = set()
    for a, b, _v in pairs:
        glyphs.add(a)
        glyphs.add(b)
    classes = {g: [g] for g in glyphs}
    excluded = []
    included = []
    for cp, name in sorted(m0.cmap.items()):
        text = chr(cp)
        decomp = ud.normalize("NFD", text)
        if len(decomp) < 2 or not decomp[0].isalpha():
            continue
        base = m0.cmap.get(ord(decomp[0]))
        if not base or base not in classes or name == base:
            continue
        close = True
        for m in masters:
            if name not in m.f["hmtx"].metrics or base not in m.f["hmtx"].metrics:
                close = False
                break
            aw1, lsb1 = m.f["hmtx"][base]
            aw2, lsb2 = m.f["hmtx"][name]
            if abs(aw1 - aw2) > 40 or abs(lsb1 - lsb2) > 30:
                close = False
                break
        if not close:
            excluded.append(f"U+{cp:04X} {name}")
            continue
        classes[base].append(name)
        included.append(f"U+{cp:04X} {name}")

    def token(g):
        mem = classes.get(g, [g])
        if len(set(mem)) == 1:
            return g
        return "@kc_" + re.sub(r"[^A-Za-z0-9_]", "_", g)

    lines = []
    emitted = set()
    for g, mem in sorted(classes.items()):
        mem = sorted(set(mem))
        if len(mem) == 1:
            continue
        cname = token(g)
        key = (cname, tuple(mem))
        if key in emitted:
            continue
        emitted.add(key)
        lines.append(f"{cname} = [{' '.join(mem)}];")
    body = ["feature kern {"]
    seen = set()
    for a, b, value in pairs:
        key = (token(a), token(b), value)
        if key in seen:
            continue
        seen.add(key)
        body.append(f"  pos {key[0]} {key[1]} {value};")
    body.append("} kern;")
    return "\n".join(lines + body) + "\n", {"included": included, "excluded": excluded, "rules": len(seen)}


def choose_metrics(masters):
    ymin, ymax = 0, 0
    letter_min = 0
    breve = 0
    for m in masters:
        for name in m.f.getGlyphOrder():
            _l, b, _r, t = build.bounds(m.get(name))
            ymin, ymax = min(ymin, b), max(ymax, t)
        for cp, name in m.cmap.items():
            if cp < 32 or not ud.category(chr(cp)).startswith("L"):
                continue
            letter_min = min(letter_min, build.bounds(m.get(name))[1])
        n = m.cmap.get(0x1EAE)
        if n:
            breve = max(breve, build.bounds(m.get(n))[3])
    # 976 covers Ắ. Do not shrink it. Descend below -430 when a letter, such as ydotbelow, does.
    typo_asc = max(976, int(math.ceil(breve)))
    typo_desc = min(-430, int(math.floor(letter_min)) - 7)
    return {
        "typo_ascender": typo_asc,
        "typo_descender": typo_desc,
        "win_ascent": int(math.ceil(ymax)),
        "win_descent": int(math.ceil(-ymin)),
        "measured_ymin": ymin,
        "measured_ymax": ymax,
        "letter_ymin": letter_min,
        "breveacute_ymax": breve,
    }


def apply_metrics(font, metrics):
    os2 = font["OS/2"]
    os2.version = max(4, os2.version)
    os2.sTypoAscender = metrics["typo_ascender"]
    os2.sTypoDescender = metrics["typo_descender"]
    os2.sTypoLineGap = 0
    os2.usWinAscent = metrics["win_ascent"]
    os2.usWinDescent = metrics["win_descent"]
    font["hhea"].ascent = metrics["typo_ascender"]
    font["hhea"].descent = metrics["typo_descender"]
    font["hhea"].lineGap = 0
    os2.recalcUnicodeRanges(font)
    if hasattr(os2, "recalcCodePageRanges"):
        os2.recalcCodePageRanges(font)
    os2.recalcAvgCharWidth(font)
    cmap = font.getBestCmap() or {}
    if ord("x") in cmap:
        bb = font["glyf"][cmap[ord("x")]].getCoordinates(font["glyf"])[0]
        if bb:
            os2.sxHeight = max(p[1] for p in bb)
    if ord("H") in cmap:
        bb = font["glyf"][cmap[ord("H")]].getCoordinates(font["glyf"])[0]
        if bb:
            os2.sCapHeight = max(p[1] for p in bb)


def apply_names(font, style, weight, italic, variable, license_str):
    family = "Akhil Notes"
    ps = "AkhilNotes-" + style.replace(" ", "")
    copyright_str = project_copyright()
    description = "A personal handwriting typeface designed by Akhil Desai for everyday notes and digital writing."
    typo_family = family
    typo_style = style
    name_family = family
    name_style = style
    if not variable and weight not in (400, 700):
        name_family = f"{family} {dict(build.WEIGHTS)[weight]}"
        name_style = "Italic" if italic else "Regular"
    sample = "The way I write, wherever I type."
    records = {
        0: copyright_str,
        1: name_family,
        2: name_style,
        3: f"{VERSION[0]}.{VERSION[1]:03d};AKHL;{ps}",
        4: f"{family} {style}",
        5: f"Version {VERSION[0]}.{VERSION[1]:03d}",
        6: ps,
        7: "Akhil Notes is a Reserved Font Name.",
        8: "Akhil Desai",
        9: "Akhil Desai",
        10: description,
        11: DESIGNER_URL,
        12: DESIGNER_URL,
        13: license_str or OFL_LICENSE,
        14: OFL_URL,
        19: sample,
    }
    if not (typo_family == name_family and typo_style == name_style):
        records[16] = typo_family
        records[17] = typo_style
    if variable:
        records[25] = "AkhilNotesItalic" if italic else "AkhilNotes"
    table = font["name"]
    table.names = []
    for name_id, text in records.items():
        table.setName(text, name_id, 3, 1, 0x409)
    font["head"].fontRevision = VERSION[0] + VERSION[1] / 1000
    os2 = font["OS/2"]
    os2.fsType = 0
    os2.usWeightClass = weight
    os2.usWidthClass = 5
    os2.achVendID = "AKHL"
    sel = os2.fsSelection
    sel &= ~((1 << 0) | (1 << 5) | (1 << 6) | (1 << 9))
    sel |= 1 << 7  # Use_Typo_Metrics
    sel |= 1 << 8  # WWS
    if italic:
        sel |= 1 << 0
    if weight == 700:
        sel |= 1 << 5
    elif not italic:
        sel |= 1 << 6
    os2.fsSelection = sel
    font["head"].macStyle = (1 if weight == 700 else 0) | (2 if italic else 0)
    font["post"].italicAngle = -15 if italic else 0
    font["post"].isFixedPitch = 0
    if italic:
        font["hhea"].caretSlopeRise = 1000
        font["hhea"].caretSlopeRun = build.otRound(math.tan(math.radians(15)) * 1000)
    else:
        font["hhea"].caretSlopeRise = 1
        font["hhea"].caretSlopeRun = 0


def apply_meta(font):
    """Declare Latin as design and supported script."""
    meta = newTable("meta")
    meta.data = {"dlng": "Latn", "slng": "Latn"}
    font["meta"] = meta


def apply_stat(font, italic=False, combined=False):
    from fontTools.ttLib.tables._f_v_a_r import NamedInstance
    from fontTools.otlLib.builder import buildStatTable

    axes = [dict(
        tag="wght",
        name="Weight",
        ordering=0,
        values=[
            dict(value=w, name=s, **({"flags": 0x2, "linkedValue": 700} if w == 400 else {}))
            for w, s in build.WEIGHTS
        ],
    )]
    if combined:
        axes.append(dict(
            tag="slnt",
            name="Slant",
            ordering=1,
            values=[
                dict(value=0, name="Default", flags=0x2, linkedValue=-15),
            ],
        ))
    else:
        axes.append(dict(
            tag="ital",
            name="Italic",
            ordering=1,
            values=[dict(
                value=int(italic),
                name="Italic" if italic else "Roman",
                **({} if italic else {"flags": 0x2, "linkedValue": 1}),
            )],
        ))
    fallback = "Italic" if italic and not combined else "Regular"
    buildStatTable(font, axes, elidedFallbackName=fallback)
    font["fvar"].instances = []
    for w, style in build.WEIGHTS:
        slants = [0, -15] if combined else ([-15] if italic else [0])
        for sl in slants:
            label = style + (" Italic" if sl else "")
            if label == "Regular Italic":
                label = "Italic"
            inst = NamedInstance()
            inst.subfamilyNameID = font["name"].addName(label, platforms=[(3, 1, 0x409)])
            inst.postscriptNameID = font["name"].addName(
                "AkhilNotes-" + label.replace(" ", ""), platforms=[(3, 1, 0x409)]
            )
            inst.coordinates = {"wght": w}
            if combined:
                inst.coordinates["slnt"] = sl
            font["fvar"].instances.append(inst)
    for axis in font["fvar"].axes:
        axis.axisNameID = font["name"].addName(
            {"wght": "Weight", "slnt": "Slant", "ital": "Italic"}[axis.axisTag],
            platforms=[(3, 1, 0x409)],
        )


def apply_static_stat(font, weight, italic):
    from fontTools.otlLib.builder import buildStatTable

    style_name = dict(build.WEIGHTS)[weight]
    axes = [
        dict(tag="wght", name="Weight", ordering=0, values=[
            dict(value=weight, name=style_name, flags=0x2),
        ]),
        dict(tag="ital", name="Italic", ordering=1, values=[dict(
            value=int(italic),
            name="Italic" if italic else "Roman",
            **({} if italic else {"flags": 0x2, "linkedValue": 1}),
        )]),
    ]
    buildStatTable(font, axes, elidedFallbackName="Italic" if italic else "Regular")


def apply_gasp(font):
    for tag in ("fpgm", "prep", "cvt "):
        if tag in font:
            del font[tag]
    gasp = newTable("gasp")
    gasp.version = 1
    # 0x000F is the current Google Fonts gasp recommendation: gridfit, dogray,
    # symmetric gridfit, symmetric smoothing. The font stays unhinted.
    gasp.gaspRange = {0xFFFF: 0x000F}
    font["gasp"] = gasp


def style_from_filename(stem):
    key = stem.split("-", 1)[-1]
    table = {}
    for weight, name in build.WEIGHTS:
        table[name] = (name, weight, False)
        ital_key = "Italic" if name == "Regular" else name + "Italic"
        ital_label = "Italic" if name == "Regular" else name + " Italic"
        table[ital_key] = (ital_label, weight, True)
    if key not in table:
        raise SystemExit(f"Unrecognized static filename {stem}")
    return table[key]


def ufo_style(weight, slant):
    label = dict(build.WEIGHTS)[weight] + (" Italic" if slant else "")
    if label == "Regular Italic":
        label = "Italic"
    filename = {
        (400, 0): "AkhilNotes-Regular",
        (900, 0): "AkhilNotes-Black",
        (400, -15): "AkhilNotes-Italic",
        (900, -15): "AkhilNotes-BlackItalic",
    }[(weight, slant)]
    if weight in (400, 700):
        sm_family = "Akhil Notes"
        sm_style = {400: "regular", 700: "bold"}[weight]
        if slant and weight == 400:
            sm_style = "italic"
        elif slant and weight == 700:
            sm_style = "bold italic"
    else:
        sm_family = "Akhil Notes " + dict(build.WEIGHTS)[weight]
        sm_style = "italic" if slant else "regular"
    return label, filename, sm_family, sm_style


def write_ufo(master, metrics, fea, filename, style, sm_family, sm_style):
    from ufoLib2 import Font
    from ufoLib2.objects.anchor import Anchor

    font = master.f
    ufo = Font()
    info = ufo.info
    info.familyName = "Akhil Notes"
    info.styleName = style
    info.versionMajor, info.versionMinor = VERSION
    info.unitsPerEm = 1000
    info.ascender = metrics["typo_ascender"]
    info.descender = metrics["typo_descender"]
    info.italicAngle = -15 if master.slant else 0
    info.openTypeOS2TypoAscender = metrics["typo_ascender"]
    info.openTypeOS2TypoDescender = metrics["typo_descender"]
    info.openTypeOS2TypoLineGap = 0
    info.openTypeHheaAscender = metrics["typo_ascender"]
    info.openTypeHheaDescender = metrics["typo_descender"]
    info.openTypeHheaLineGap = 0
    info.openTypeOS2WinAscent = metrics["win_ascent"]
    info.openTypeOS2WinDescent = metrics["win_descent"]
    info.openTypeOS2VendorID = "AKHL"
    info.openTypeOS2Type = []
    info.styleMapFamilyName = sm_family
    info.styleMapStyleName = sm_style
    info.openTypeNameDesigner = "Akhil Desai"
    info.openTypeNameDesignerURL = DESIGNER_URL
    info.openTypeNameManufacturer = "Akhil Desai"
    info.openTypeNameManufacturerURL = DESIGNER_URL
    info.copyright = project_copyright()
    info.openTypeNameLicense = OFL_LICENSE
    info.openTypeNameLicenseURL = OFL_URL
    rev = {cp: name for cp, name in master.cmap.items()}
    by_name = defaultdict(list)
    for cp, name in rev.items():
        by_name[name].append(cp)
    order = font.getGlyphOrder()
    front = [n for n in (".notdef", "NULL", "CR", "space") if n in order]
    order = front + [n for n in order if n not in front]
    for name in order:
        glyph = ufo.newGlyph(name)
        adv, _lsb = font["hmtx"][name]
        glyph.width = adv
        glyph.unicodes = sorted(by_name.get(name, []))
        font["glyf"][name].drawPoints(glyph.getPointPen(), font["glyf"])
        if name in master.new:
            glyph.lib["public.truetype.overlap"] = True
    # Anchors mirror the feature file so the UFO is inspectable. Compilation uses features.fea.
    for line in fea.splitlines():
        if line.startswith("pos base "):
            parts = line.split()
            gname = parts[2]
            if gname not in ufo:
                continue
            anchors = re.findall(r"<anchor (-?\d+) (-?\d+)> mark @(\w+)", line)
            for x, y, kind in anchors:
                ufo[gname].anchors.append(Anchor(x=int(x), y=int(y), name=kind))
        elif line.startswith("markClass "):
            m = re.match(r"markClass (\S+) <anchor (-?\d+) (-?\d+)> @(\w+);", line)
            if not m or m.group(1) not in ufo:
                continue
            ufo[m.group(1)].anchors.append(Anchor(x=int(m.group(2)), y=int(m.group(3)), name="_" + m.group(4)))
    ufo.glyphOrder = order
    ufo.features.text = fea
    path = MASTER_DIR / f"{filename}.ufo"
    if path.exists():
        import shutil
        shutil.rmtree(path)
    ufo.save(path, overwrite=True)
    return path


def write_designspace(entries):
    from fontTools.designspaceLib import DesignSpaceDocument, AxisDescriptor, SourceDescriptor, InstanceDescriptor

    ds = DesignSpaceDocument()
    for tag, name, minimum, default, maximum in (
        ("wght", "Weight", 400, 400, 900),
        ("slnt", "Slant", -15, 0, 0),
    ):
        axis = AxisDescriptor()
        axis.tag, axis.name = tag, name
        axis.minimum, axis.default, axis.maximum = minimum, default, maximum
        ds.addAxis(axis)
    for weight, slant, filename, style in entries:
        src = SourceDescriptor()
        src.filename = f"masters/{filename}.ufo"
        src.name = filename
        src.familyName = "Akhil Notes"
        src.styleName = style
        src.location = {"Weight": weight, "Slant": slant}
        ds.addSource(src)
    for weight, style_name in build.WEIGHTS:
        for slant in (0, -15):
            label = style_name + (" Italic" if slant else "")
            if label == "Regular Italic":
                label = "Italic"
            inst = InstanceDescriptor()
            inst.familyName = "Akhil Notes"
            inst.styleName = label
            inst.name = f"Akhil Notes {label}"
            inst.location = {"Weight": weight, "Slant": slant}
            inst.filename = "AkhilNotes-" + label.replace(" ", "") + ".ttf"
            ds.addInstance(inst)
    ds.lib["com.github.googlei18n.ufo2ft.featureWriters"] = []
    path = SOURCES / "AkhilNotes.designspace"
    ds.write(path)
    return path


def fontmake(designspace: Path):
    py = sys.executable
    common = [
        py, "-m", "fontmake", "-m", str(designspace),
        "--keep-overlaps", "--keep-direction", "--ttf-curves", "keep-quad",
        "--no-production-names", "--no-autohint", "--feature-writer", "None",
    ]
    slant_dir = FONT_DIR / "variable-slant"
    slant_dir.mkdir(parents=True, exist_ok=True)
    static_dir = FONT_DIR / "ttf"
    static_dir.mkdir(parents=True, exist_ok=True)
    slant_path = slant_dir / "AkhilNotes[slnt,wght].ttf"
    commands = [
        common + ["-o", "variable", "--output-path", str(slant_path)],
        common + ["-o", "ttf", "--output-dir", str(static_dir), "--interpolate"],
    ]
    logs = []
    for cmd in commands:
        print(" ".join(cmd), flush=True)
        proc = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
        logs.append({"cmd": cmd, "returncode": proc.returncode, "stdout": proc.stdout[-4000:], "stderr": proc.stderr[-8000:]})
        if proc.returncode != 0:
            (QA / "fontmake-error.txt").write_text(proc.stdout + "\n" + proc.stderr, encoding="utf-8")
            raise SystemExit(proc.stderr[-2000:] or proc.stdout[-2000:])
    return slant_path, static_dir, logs


def flatten_nested_components(font: TTFont) -> None:
    """Expand any component that itself points at a composite (GF disallows nesting)."""
    glyf = font["glyf"]
    changed = True
    while changed:
        changed = False
        for name in list(font.getGlyphOrder()):
            g = glyf[name]
            if not getattr(g, "isComposite", lambda: False)():
                continue
            needs = any(glyf[c.glyphName].isComposite() for c in g.components)
            if not needs:
                continue
            from fontTools.pens.ttGlyphPen import TTGlyphPen

            pen = TTGlyphPen(glyf)
            g.draw(pen, glyf)
            glyf[name] = pen.glyph()
            changed = True


def finalize_file(path, metrics, lic, variable, italic, combined, weight, style):
    font = TTFont(path)
    apply_names(font, style, weight, italic, variable, lic)
    apply_metrics(font, metrics)
    apply_gasp(font)
    apply_meta(font)
    flatten_nested_components(font)
    if variable:
        apply_stat(font, italic=italic, combined=combined)
    else:
        apply_static_stat(font, weight, italic)
    font.save(path)
    return font


def original_drift(source, master):
    inst = instantiateVariableFont(source, {"wght": master.weight, "slnt": master.slant}, inplace=False)
    drifted = []
    for cp, src_name in source.getBestCmap().items():
        if cp in build.REBUILD_FIGURES:
            continue
        built = master.cmap.get(cp)
        if built is None:
            drifted.append((hex(cp), "missing"))
            continue
        if real_points(inst, src_name) != real_points(master.f, built):
            drifted.append((f"U+{cp:04X}", built))
    return drifted


def metrics_from_ufo() -> dict:
    """Read vertical metrics from the committed Regular UFO (compile mode)."""
    from ufoLib2 import Font

    regular = MASTER_DIR / "AkhilNotes-Regular.ufo"
    if not regular.exists():
        raise SystemExit(f"Missing committed UFO: {regular}")
    ufo = Font.open(regular)
    return {
        "typo_ascender": int(ufo.info.openTypeOS2TypoAscender),
        "typo_descender": int(ufo.info.openTypeOS2TypoDescender),
        "win_ascent": int(ufo.info.openTypeOS2WinAscent),
        "win_descent": int(ufo.info.openTypeOS2WinDescent),
    }


def finalize_outputs(metrics: dict) -> list[str]:
    """Slant-split VF, finalize names/OFL/STAT, write statics + WOFF2. Returns relative paths."""
    lic = OFL_LICENSE
    slant_path = FONT_DIR / "variable-slant" / "AkhilNotes[slnt,wght].ttf"
    static_dir = FONT_DIR / "ttf"
    var_dir = FONT_DIR / "variable"
    web_dir = FONT_DIR / "webfonts"
    var_dir.mkdir(parents=True, exist_ok=True)
    web_dir.mkdir(parents=True, exist_ok=True)
    produced = []
    for slant, filename, italic in (
        (0, "AkhilNotes[wght].ttf", False),
        (-15, "AkhilNotes-Italic[wght].ttf", True),
    ):
        inst = instantiateVariableFont(TTFont(slant_path), {"slnt": slant}, inplace=False)
        out = var_dir / filename
        inst.save(out)
        style = "Italic" if italic else "Regular"
        finalize_file(out, metrics, lic, True, italic, False, 400, style)
        woff = web_dir / filename.replace(".ttf", ".woff2")
        wf = TTFont(out)
        wf.flavor = "woff2"
        wf.save(woff)
        produced.append(str(out.relative_to(ROOT)))
    finalize_file(slant_path, metrics, lic, True, False, True, 400, "Regular")
    produced.append(str(slant_path.relative_to(ROOT)))
    for path in sorted(static_dir.glob("*.ttf")):
        style, weight, italic = style_from_filename(path.stem)
        finalize_file(path, metrics, lic, False, italic, False, weight, style)
        canon = static_dir / ("AkhilNotes-" + style.replace(" ", "") + ".ttf")
        if path != canon:
            path.replace(canon)
            path = canon
        wf = TTFont(path)
        wf.flavor = "woff2"
        wf.save(web_dir / (path.stem + ".woff2"))
        produced.append(str(path.relative_to(ROOT)))
    return produced


def compile_from_ufo(*, package: bool = True) -> dict:
    """Public build: designspace + committed UFOs → shipping fonts. Never overwrites masters."""
    ds_path = SOURCES / "AkhilNotes.designspace"
    if not ds_path.exists():
        raise SystemExit(f"Missing designspace: {ds_path}")
    for name in (
        "AkhilNotes-Regular.ufo",
        "AkhilNotes-Black.ufo",
        "AkhilNotes-Italic.ufo",
        "AkhilNotes-BlackItalic.ufo",
    ):
        if not (MASTER_DIR / name).exists():
            raise SystemExit(f"Missing master UFO: {MASTER_DIR / name}")
    QA.mkdir(parents=True, exist_ok=True)
    metrics = metrics_from_ufo()
    print("compiling from UFO (no provenance)", flush=True)
    slant_path, static_dir, logs = fontmake(ds_path)
    (QA / "fontmake.log").write_text(json.dumps(logs, indent=2), encoding="utf-8")
    produced = finalize_outputs(metrics)
    # Overlap flags: require Fontspector, then hotfix shipping VF pair (flags only).
    import importlib.util

    ensure_spec = importlib.util.spec_from_file_location(
        "ensure_fontspector", ROOT / "scripts" / "ensure_fontspector.py"
    )
    ensure_mod = importlib.util.module_from_spec(ensure_spec)
    assert ensure_spec.loader is not None
    ensure_spec.loader.exec_module(ensure_mod)
    ensure_mod.ensure_fontspector(download=True)

    fix_spec = importlib.util.spec_from_file_location(
        "fix_overlap_flags", ROOT / "scripts" / "fix_overlap_flags.py"
    )
    fix_mod = importlib.util.module_from_spec(fix_spec)
    assert fix_spec.loader is not None
    fix_spec.loader.exec_module(fix_mod)
    vfs = [
        FONT_DIR / "variable" / "AkhilNotes[wght].ttf",
        FONT_DIR / "variable" / "AkhilNotes-Italic[wght].ttf",
    ]
    fix_mod.run_fontspector_hotfix([p for p in vfs if p.exists()], require=True)
    report = {
        "mode": "from-ufo",
        "designspace": str(ds_path.relative_to(ROOT)),
        "metrics": metrics,
        "produced": produced,
        "license": "OFL 1.1",
        "copyright": project_copyright(),
        "repo": REPO_URL,
    }
    (QA / "compile-report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"mode": "from-ufo", "metrics": metrics, "files": len(produced)}, indent=2))
    if package:
        subprocess.check_call([sys.executable, str(ROOT / "scripts" / "package_gf.py")], cwd=ROOT)
    return report


def generate_from_provenance(*, package: bool = True) -> dict:
    """Maintainer-only: regenerate UFOs from private TTF, then compile."""
    verify_source()
    QA.mkdir(parents=True, exist_ok=True)
    MASTER_DIR.mkdir(parents=True, exist_ok=True)
    FEATURE_DIR.mkdir(parents=True, exist_ok=True)
    source = TTFont(SRC)
    initial = dict(source.getBestCmap())
    wanted, unencoded_names, name_conflicts = production_maps()
    masters = []
    for weight, slant in ((400, 0), (900, 0), (400, -15), (900, -15)):
        print(f"master {weight} {slant}", flush=True)
        font = instantiateVariableFont(source, {"wght": weight, "slnt": slant}, inplace=False)
        build.rename_digits(font)
        if "STAT" in font:
            del font["STAT"]
        master = PreservingMaster(font, weight, slant)
        master.build_marks()
        master.build_letters()
        master.build_punct()
        master.compose_accents(set(initial) | set(map(ord, build.CORE + build.VIET)))
        master.build_plus()
        master.add_features_glyphs()
        for ch in list(master.alts):
            delete_glyph(master, f"{ch}.alt1")
            delete_glyph(master, f"{ch}.alt2")
        master.alts = []
        add_whitespace(master)
        add_dotted_circle(master)
        drift = original_drift(source, master)
        if drift:
            raise SystemExit(f"Original outlines changed at {weight}/{slant}: {drift[:8]}")
        masters.append(master)

    print("kerning", flush=True)
    pairs = build.kern_plan(masters)
    histogram = defaultdict(int)
    clamped = 0
    dropped_floor = 0
    adjusted = []
    for a, b, value in pairs:
        histogram[int(value)] += 1
        if value <= -75:
            dropped_floor += 1
            continue
        new = value
        if new < -50:
            new = -50
            clamped += 1
        elif new > 50:
            new = 50
            clamped += 1
        adjusted.append((a, b, new))
    kern_fea, kern_info = class_kern(masters, adjusted)
    metrics = choose_metrics(masters)
    for m in masters:
        for attr, value in (
            ("sTypoAscender", metrics["typo_ascender"]),
            ("sTypoDescender", metrics["typo_descender"]),
            ("sTypoLineGap", 0),
            ("usWinAscent", metrics["win_ascent"]),
            ("usWinDescent", metrics["win_descent"]),
        ):
            setattr(m.f["OS/2"], attr, value)
        m.f["hhea"].ascent = metrics["typo_ascender"]
        m.f["hhea"].descent = metrics["typo_descender"]
        m.f["hhea"].lineGap = 0
    entries = []
    for m in masters:
        style, filename, sm_family, sm_style = ufo_style(m.weight, m.slant)
        fea = strip_experimental(m.features(adjusted))
        fea = re.sub(r"feature kern \{.*?\n\} kern;\n", "", fea, flags=re.S) + kern_fea
        fea = fix_frac(fea)
        mapping = production_mapping(m, wanted)
        rename_master(m, mapping)
        fea = rename_fea(fea, mapping)
        fea = anchor_dotted_circle(fea, m)
        fea = add_soft_dot(fea, m)
        print(f"validate features {filename}", flush=True)
        addOpenTypeFeaturesFromString(m.f, fea)
        (FEATURE_DIR / f"{filename}.fea").write_text(fea, encoding="utf-8")
        write_ufo(m, metrics, fea, filename, style, sm_family, sm_style)
        entries.append((m.weight, m.slant, filename, style))
    ds_path = write_designspace(entries)
    present = set(masters[0].f.getGlyphOrder())
    missing_unencoded = sorted(set(unencoded_names) - present)
    report = {
        "mode": "from-provenance",
        "source_sha256": sha256(SRC),
        "glyphsets": {"version": "1.1.3", "commit": GLYPHSETS_COMMIT, "sets": list(SETS)},
        "gf_guide": {
            "repository": "https://github.com/googlefonts/googlefonts.github.io",
            "path": "gf-guide",
            "commit": GUIDE_COMMIT,
            "commit_date": "2026-11-18",
        },
        "mapped": len(masters[0].cmap),
        "glyphs": len(masters[0].f.getGlyphOrder()),
        "original_preserved": len(initial),
        "intentional_figure_rebuilds": sorted(f"U+{cp:04X}" for cp in build.REBUILD_FIGURES),
        "original_drift": [],
        "kern_rules": kern_info["rules"],
        "kern_input_pairs": len(adjusted),
        "kern_clamped": clamped,
        "kern_dropped_floor": dropped_floor,
        "kern_value_histogram": {str(k): histogram[k] for k in sorted(histogram)},
        "accented_kerning_included": len(kern_info["included"]),
        "accented_kerning_excluded": kern_info["excluded"],
        "metrics": metrics,
        "missing_unencoded_production_names": missing_unencoded,
        "production_name_conflicts": name_conflicts,
        "provisional_new_codepoints": [
            f"U+{cp:04X} {chr(cp)} {ud.name(chr(cp), '?')}"
            for cp in sorted(set(masters[0].cmap) - set(initial))
            if cp >= 32
        ],
        "experimental_alternates": "disabled; rotated letter alternates are not in the candidate font",
        "license": "OFL 1.1",
        "copyright": project_copyright(),
        "repo": REPO_URL,
    }
    (QA / "source-report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print("compiling", flush=True)
    slant_path, static_dir, logs = fontmake(ds_path)
    (QA / "fontmake.log").write_text(json.dumps(logs, indent=2), encoding="utf-8")
    produced = finalize_outputs(metrics)
    report["produced"] = produced
    (QA / "source-report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("mapped", "glyphs", "kern_rules", "kern_clamped", "metrics", "missing_unencoded_production_names")}, indent=2))
    if package:
        subprocess.check_call([sys.executable, str(ROOT / "scripts" / "package_gf.py")], cwd=ROOT)
    return report


def main(argv: list[str] | None = None):
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--from-ufo",
        dest="mode",
        action="store_const",
        const="ufo",
        help="Compile committed UFOs only (default; no provenance required)",
    )
    mode.add_argument(
        "--from-provenance",
        dest="mode",
        action="store_const",
        const="provenance",
        help="Regenerate UFO masters from provenance/*.ttf then compile (maintainer-only)",
    )
    parser.set_defaults(mode="ufo")
    parser.add_argument("--no-package", action="store_true", help="Skip ofl/akhilnotes packaging")
    args = parser.parse_args(argv)
    package = not args.no_package
    if args.mode == "provenance":
        generate_from_provenance(package=package)
    else:
        compile_from_ufo(package=package)


if __name__ == "__main__":
    main()
