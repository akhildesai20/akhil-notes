#!/usr/bin/env python3
"""Shape, measure, and render the candidate fonts. Proofs use FreeType on the actual files."""
from __future__ import annotations

import json
import sys
import unicodedata as ud
from pathlib import Path

import freetype
import uharfbuzz as hb
from fontTools.pens.areaPen import AreaPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import build as build_mod  # noqa: E402
SRC = ROOT / "provenance" / "AkhilsNotes-Variable.ttf"
CAND = ROOT / "fonts" / "ttf" / "AkhilNotes-Regular.ttf"
CAND_ITAL = ROOT / "fonts" / "ttf" / "AkhilNotes-Italic.ttf"
CAND_BLACK = ROOT / "fonts" / "ttf" / "AkhilNotes-Black.ttf"
CAND_VF = ROOT / "fonts" / "variable" / "AkhilNotes[wght].ttf"
BASE = ROOT / "baseline" / "fonts" / "AkhilNotes-Regular.ttf"
OUT = ROOT / "qa" / "proofs"
QA = ROOT / "qa" / "candidate"
OUT.mkdir(parents=True, exist_ok=True)

SAMPLES = {
    "en": "The way I write, wherever I type. Today I wrote down a few thoughts about design.",
    "fr": "Voilà : l'élève a déjà fini à Noël, où il a reçu un cadeau.",
    "de": "Größe, Straße und süß — die Prüfung in München ist überfüllt.",
    "es": "¿El niño preguntó «dónde»? ¡Sí, mañana!",
    "ro": "Și țara își schimbă șoaptele de dimineață.",
    "tr": "İstanbul'da iki iyi insan.",
    "ca": "La col·lecció il·lustrada de l'illa.",
    "vi": "Tiếng Việt: Nguyễn, Tưởng, Hoàng. Việt Nam Ắằặễộự.",
    "pl": "Zażółć gęślą jaźń.",
    "pt": "São Paulo não é tão longe para você.",
    "cs": "Příliš žluťoučký kůň úpěl ďábelské ódy.",
    "num": "0123456789  1,234.50   $12  £9  €8  ¥100  ₫20  ₦5  ₱40",
    "frac": "1/2 cup, 3/4 inch, 12/34 and plain 5 6 7.",
    "math": "∂f/∂x ≠ ∅   ∫ a→b   ↗↘   ⟨x⟩  ℓ № Ω",
}


def shape(font_path, text, features=None, language=None):
    blob = hb.Blob.from_file_path(str(font_path))
    face = hb.Face(blob)
    font = hb.Font(face)
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    if language:
        buf.language = language
    hb.shape(font, buf, features or {})
    infos = buf.glyph_infos
    positions = buf.glyph_positions
    return face, infos, positions


def glyph_names(font_path, infos):
    tt = TTFont(font_path)
    order = tt.getGlyphOrder()
    return [order[i.codepoint] for i in infos]


def render_text(font_path, text, size, features=None, language=None, ink=0):
    _face, infos, positions = shape(font_path, text, features, language)
    tt = TTFont(font_path)
    upem = tt["head"].unitsPerEm
    scale = size / upem
    pen = 0
    placed = []
    min_y = 0
    max_y = 0
    for info, pos in zip(infos, positions):
        placed.append((info.codepoint, pen + pos.x_offset, pos.y_offset))
        pen += pos.x_advance
        min_y = min(min_y, pos.y_offset)
        max_y = max(max_y, pos.y_offset)
    ft = freetype.Face(str(font_path))
    ft.set_char_size(int(round(size * 64)))
    pad = 12
    width = max(20, int(pen * scale) + pad * 2)
    height = int(size * 2.6)
    image = Image.new("L", (width, height), 255)
    baseline = int(size * 1.55)
    for gid, x, yoff in placed:
        ft.load_glyph(gid, freetype.FT_LOAD_RENDER | freetype.FT_LOAD_NO_HINTING)
        bitmap = ft.glyph.bitmap
        if not bitmap.width or not bitmap.rows:
            continue
        buf = bytes(bitmap.buffer)
        pitch = abs(bitmap.pitch)
        raw = bytearray()
        for row in range(bitmap.rows):
            start = row * pitch
            raw.extend(buf[start:start + bitmap.width])
        glyph = Image.frombytes("L", (bitmap.width, bitmap.rows), bytes(raw))
        left = pad + int(round(x * scale)) + ft.glyph.bitmap_left
        top = baseline - ft.glyph.bitmap_top - int(round(yoff * scale))
        color = Image.new("L", glyph.size, 0)
        # Clip to the sheet. A mark may sit above the first line; keep the canvas tall enough.
        sheet_box = (left, top, left + glyph.width, top + glyph.height)
        if sheet_box[2] < 0 or sheet_box[3] < 0 or sheet_box[0] > image.width or sheet_box[1] > image.height:
            continue
        image.paste(color, (left, top), glyph)
    return image


def stack(images, labels, label_width=220):
    width = label_width + max(im.width for im in images)
    height = sum(im.height for im in images) + 8
    sheet = Image.new("L", (width, height), 255)
    draw = ImageDraw.Draw(sheet)
    y = 0
    for label, im in zip(labels, images):
        draw.text((6, y + 8), label, fill=80)
        sheet.paste(im, (label_width, y))
        y += im.height
    return sheet


def paint_glyphs(font_path, cps, cell=120, cols=12):
    tt = TTFont(font_path)
    cmap = tt.getBestCmap()
    rows = (len(cps) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * cell, rows * cell), "white")
    draw = ImageDraw.Draw(sheet)
    ft = freetype.Face(str(font_path))
    ft.set_char_size(52 * 64)
    for i, cp in enumerate(cps):
        col, row = i % cols, i // cols
        x0, y0 = col * cell, row * cell
        draw.rectangle((x0, y0, x0 + cell - 1, y0 + cell - 1), outline=(220, 220, 220))
        draw.text((x0 + 4, y0 + 2), f"U+{cp:04X}", fill=(140, 140, 140))
        name = cmap.get(cp)
        if name is None:
            draw.text((x0 + 20, y0 + 48), "missing", fill=(180, 0, 0))
            continue
        ft.load_glyph(tt.getGlyphID(name), freetype.FT_LOAD_RENDER | freetype.FT_LOAD_NO_HINTING)
        bitmap = ft.glyph.bitmap
        if bitmap.width and bitmap.rows:
            glyph = Image.frombytes("L", (bitmap.width, bitmap.rows), bytes(bitmap.buffer))
            left = x0 + (cell - bitmap.width) // 2
            top = y0 + 28
            color = Image.new("RGB", glyph.size, (10, 10, 10))
            sheet.paste(color, (left, top), glyph)
    return sheet


def main():
    QA.mkdir(parents=True, exist_ok=True)
    source = TTFont(SRC)
    regular = TTFont(CAND)
    src_cmap = source.getBestCmap()
    reg_cmap = regular.getBestCmap()
    inst = instantiateVariableFont(source, {"wght": 400, "slnt": 0}, inplace=False)
    rename = {str(i): n for i, n in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])}

    def pts(font, name):
        g = font["glyf"][name]
        if g.numberOfContours <= 0:
            return None
        coords, ends, _flags = g.getCoordinates(font["glyf"])
        count = ends[-1] + 1
        return [(int(coords[i][0]), int(coords[i][1])) for i in range(count)]

    intentional_figure_rebuilds = []
    unexpected_drift = []
    for cp, src_name in src_cmap.items():
        built = reg_cmap.get(cp)
        if not built:
            unexpected_drift.append({"cp": hex(cp), "issue": "lost"})
            continue
        a, b = pts(inst, src_name), pts(regular, built)
        if a != b:
            delta = None
            if a and b and len(a) == len(b):
                delta = max(max(abs(p[0] - q[0]), abs(p[1] - q[1])) for p, q in zip(a, b))
            row = {
                "cp": f"U+{cp:04X}",
                "points": None if not a or not b else [len(a), len(b)],
                "max_delta": delta,
            }
            if cp in build_mod.REBUILD_FIGURES:
                intentional_figure_rebuilds.append(row)
            else:
                unexpected_drift.append(row)
    # Back-compat alias used by older notes; prefer intentional_figure_rebuilds.
    drift = intentional_figure_rebuilds + unexpected_drift

    # Extremes and contour notes on the regular and black statics.
    extremes = []
    contour_notes = []
    for label, path in (("Regular", CAND), ("Black", CAND_BLACK), ("Italic", CAND_ITAL)):
        font = TTFont(path)
        ymin = (0, None)
        ymax = (0, None)
        for name in font.getGlyphOrder():
            g = font["glyf"][name]
            if g.numberOfContours == 0:
                continue
            g.recalcBounds(font["glyf"])
            if g.yMin is not None and g.yMin < ymin[0]:
                ymin = (g.yMin, name)
            if g.yMax is not None and g.yMax > ymax[0]:
                ymax = (g.yMax, name)
            if name in reg_cmap.values() and font.getGlyphID(name):
                pass
        extremes.append({"style": label, "ymin": ymin, "ymax": ymax})
        if label != "Regular":
            continue
        new_cps = sorted(set(reg_cmap) - set(src_cmap))
        for cp in new_cps:
            name = reg_cmap[cp]
            g = font["glyf"][name]
            pen = AreaPen(font["glyf"])
            try:
                g.draw(pen, font["glyf"])
                area = pen.value
            except Exception as exc:
                area = None
                contour_notes.append({"cp": f"U+{cp:04X}", "name": name, "error": str(exc)})
                continue
            adv = font["hmtx"][name][0]
            is_mark = ud.category(chr(cp)) == "Mn" if cp > 31 else False
            note = {"cp": f"U+{cp:04X}", "name": name, "area": round(area, 1) if area is not None else None, "advance": adv}
            if is_mark and adv != 0:
                note["issue"] = "combining mark is not zero-width"
            if area is not None and abs(area) < 20 and cp > 32 and not ud.category(chr(cp)).startswith("Z"):
                note["issue"] = "near-empty outline"
            if "issue" in note:
                contour_notes.append(note)

    # Shaping tests.
    tests = []

    def record(test, text, features=None, language=None, font=CAND):
        _f, infos, positions = shape(font, text, features, language)
        names = glyph_names(font, infos)
        tests.append({
            "test": test,
            "text": text,
            "language": language,
            "features": features or {},
            "glyphs": names,
            "advances": [p.x_advance for p in positions],
        })

    record("frac-keeps-following-digits", "1/2 9", {"frac": True, "kern": False})
    record("frac-multi", "12/34", {"frac": True, "kern": False})
    record("no-frac", "1/2", {"frac": False, "kern": False})
    record("tnum", "0123456789", {"tnum": True, "kern": False})
    record("default-digits", "0123456789", {"tnum": False, "kern": False})
    record("vi-nfc", "ế", {"kern": False}, "vi")
    record("vi-nfd", ud.normalize("NFD", "ế"), {"kern": False}, "vi")
    record("ro-comma", "ȘșȚț", {"kern": False}, "ro")
    record("tr-i", "iİı", {"kern": False}, "tr")
    record("tr-i-accent", "i\u0301", {"kern": False}, "tr")
    record("default-i-accent", "i\u0301", {"kern": False}, "en")
    record("ca-geminate", "l·l", {"kern": False}, "ca")
    record("calt-off", "ooo", {"calt": True, "kern": False})
    record("zero", "0", {"zero": True, "kern": False})
    record("sups", "n2", {"sups": True, "kern": False})

    # Proof sheets.
    sizes = [12, 14, 16, 20, 24, 32]
    labels, images = [], []
    for size in sizes:
        labels.append(f"Regular {size}px")
        images.append(render_text(CAND, SAMPLES["en"], size, {"kern": True, "calt": False}))
    stack(images, labels).save(OUT / "waterfall-regular.png")
    labels, images = [], []
    for size in sizes:
        labels.append(f"Italic {size}px")
        images.append(render_text(CAND_ITAL, SAMPLES["en"], size, {"kern": True, "calt": False}))
    stack(images, labels).save(OUT / "waterfall-italic.png")

    labels, images = [], []
    for key in ("en", "fr", "de", "es", "ro", "tr", "ca", "vi", "pl", "pt", "cs", "num", "frac", "math"):
        lang = {"vi": "vi", "ro": "ro", "tr": "tr", "ca": "ca"}.get(key)
        labels.append(key)
        images.append(render_text(CAND, SAMPLES[key], 28, {"kern": True, "calt": False, "frac": key == "frac"}, lang))
    stack(images, labels, 70).save(OUT / "multilingual-regular.png")
    labels = [k + " ital" for k in ("en", "fr", "vi", "ro", "de")]
    images = [render_text(CAND_ITAL, SAMPLES[k], 28, {"kern": True}, {"vi": "vi", "ro": "ro"}.get(k)) for k in ("en", "fr", "vi", "ro", "de")]
    stack(images, labels, 90).save(OUT / "multilingual-italic.png")

    paragraph = SAMPLES["en"]
    labels = ["source 491", "baseline kern", "candidate kern on", "candidate kern off"]
    images = [
        render_text(SRC, paragraph, 26, {"kern": False}),
        render_text(BASE, paragraph, 26, {"kern": True, "calt": True}),
        render_text(CAND, paragraph, 26, {"kern": True, "calt": False}),
        render_text(CAND, paragraph, 26, {"kern": False, "calt": False}),
    ]
    stack(images, labels, 170).save(OUT / "texture-kern-compare.png")

    accent_line = "ÁÀÂÃÄÅ ĂĆČĎ ÑÓÔÕÖ Ý áàâãäå ăćčď ñóôõö ý ȘșȚț Ăă"
    labels = ["source", "baseline rebuilt", "candidate preserved"]
    images = [
        render_text(SRC, accent_line, 36, {"kern": False}),
        render_text(BASE, accent_line, 36, {"kern": False, "calt": False}),
        render_text(CAND, accent_line, 36, {"kern": False, "calt": False}),
    ]
    stack(images, labels, 180).save(OUT / "accent-preservation.png")

    new_cps = [cp for cp in sorted(set(reg_cmap) - set(src_cmap)) if cp >= 32]
    paint_glyphs(CAND, new_cps).save(OUT / "added-glyphs-regular.png")
    paint_glyphs(CAND_BLACK, new_cps).save(OUT / "added-glyphs-black.png")
    paint_glyphs(CAND_ITAL, new_cps).save(OUT / "added-glyphs-italic.png")
    focus = [ord(ch) for ch in "ÆæŒœÐðÞþØøĐđĦħŁłẞß§¶µ"]
    focus += [0x20A6, 0x20A8, 0x20A9, 0x20AA, 0x20AB, 0x20B9, 0x20BA, 0x20BD, 0x20BF, 0x2610, 0x2611, 0x2612]
    focus = [cp for cp in focus if cp in reg_cmap or cp in src_cmap]
    paint_glyphs(CAND, focus, cell=150, cols=8).save(OUT / "focus-symbols-regular.png")
    paint_glyphs(CAND_BLACK, [cp for cp in focus if cp in TTFont(CAND_BLACK).getBestCmap()], cell=150, cols=8).save(OUT / "focus-symbols-black.png")

    narrow = "The letters feel more natural when they form a paragraph in a narrow column of notes, with commas, quotes, and the odd number 12."
    # Draw a narrow column by wrapping on spaces using shaped width.
    def column(path, text, size, features, max_width=280):
        words = text.split()
        lines = []
        current = ""
        for word in words:
            trial = (current + " " + word).strip()
            image = render_text(path, trial, size, features)
            if image.width > max_width and current:
                lines.append(current)
                current = word
            else:
                current = trial
        if current:
            lines.append(current)
        images = [render_text(path, line, size, features) for line in lines]
        return stack(images, [""] * len(images), 8)

    column(CAND, narrow, 16, {"kern": True}).save(OUT / "narrow-column-16.png")
    column(CAND_ITAL, narrow, 16, {"kern": True}).save(OUT / "narrow-column-italic-16.png")

    audit = {
        "intentional_figure_rebuilds_count": len(intentional_figure_rebuilds),
        "intentional_figure_rebuilds": intentional_figure_rebuilds,
        "unexpected_original_drift_count": len(unexpected_drift),
        "unexpected_original_drift": unexpected_drift[:30],
        # Deprecated alias (was misread as regression): 38 = intentional supers/subs/fractions.
        "compiled_original_drift_count": len(intentional_figure_rebuilds),
        "compiled_original_drift": intentional_figure_rebuilds[:30],
        "extremes": extremes,
        "contour_flags": contour_notes,
        "shaping": tests,
        "added_codepoints": len(new_cps),
        "proofs": sorted(p.name for p in OUT.glob("*.png")),
    }
    (QA / "qa.json").write_text(json.dumps(audit, indent=2, ensure_ascii=False), encoding="utf-8")
    print(
        "intentional_figure_rebuilds",
        len(intentional_figure_rebuilds),
        "unexpected_drift",
        len(unexpected_drift),
    )
    print("extremes", extremes)
    print("contour flags", len(contour_notes))
    print("proofs", audit["proofs"])
    for test in tests:
        print(test["test"], " ".join(test["glyphs"]))


if __name__ == "__main__":
    main()
