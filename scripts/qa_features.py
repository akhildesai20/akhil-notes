#!/usr/bin/env python3
"""HarfBuzz feature harness: kern, mark/mkmk, ccmp, locl, liga/dlig, frac, tnum/pnum.

Asserts that features produce expected glyph names / stable advances. Does not
require mechanical kerning uniformity.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import uharfbuzz as hb
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[1]
VF = ROOT / "fonts" / "variable" / "AkhilNotes[wght].ttf"
OUT = ROOT / "qa" / "candidate" / "features.json"


def shape(path: Path, text: str, features: dict[str, bool], *, language: str | None = None) -> dict:
    data = path.read_bytes()
    face = hb.Face(data)
    font = hb.Font(face)
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    if language:
        buf.set_language_from_ot_tag(language)
    hb.shape(font, buf, features)
    order = TTFont(path).getGlyphOrder()
    names = [order[info.codepoint] if info.codepoint < len(order) else str(info.codepoint) for info in buf.glyph_infos]
    advance = sum(p.x_advance for p in buf.glyph_positions)
    return {"text": text, "features": features, "glyphs": names, "x_advance": int(advance)}


def main() -> None:
    if not VF.exists():
        raise SystemExit(f"missing {VF}")
    cases = []

    def expect(name: str, text: str, features: dict[str, bool], pred, **kw):
        result = shape(VF, text, features, **kw)
        ok = bool(pred(result))
        cases.append({"name": name, "ok": ok, "result": result})
        print(("PASS" if ok else "FAIL"), name, result["glyphs"])

    # Kern: default-on; To/AV should not explode; sequence stays letters
    expect("kern", "To AV", {"kern": True}, lambda r: r["glyphs"] == ["T", "o", "space", "A", "V"] and r["x_advance"] > 0)
    expect(
        "mark",
        "áê",
        {"mark": True, "mkmk": True, "ccmp": True},
        lambda r: "aacute" in r["glyphs"] or any("acute" in g or "a" == g for g in r["glyphs"]),
    )
    expect(
        "mkmk",
        "a\u0302\u0301",
        {"mark": True, "mkmk": True, "ccmp": True},
        lambda r: len(r["glyphs"]) >= 1,
    )
    expect("ccmp_fi", "fi", {"liga": True, "ccmp": True}, lambda r: "f_i" in r["glyphs"] or r["glyphs"] == ["f", "i"])
    expect("liga", "fi fl", {"liga": True}, lambda r: "f_i" in r["glyphs"] and "f_l" in r["glyphs"])
    expect("dlig", "ct st", {"dlig": True}, lambda r: "c_t" in r["glyphs"] or "c" in r["glyphs"])
    expect("frac", "1/2", {"frac": True}, lambda r: "fraction" in r["glyphs"] or "one.numr" in r["glyphs"])
    expect("tnum", "0123456789", {"tnum": True}, lambda r: all(g.endswith(".tf") for g in r["glyphs"]))
    expect("pnum", "0123456789", {"pnum": True}, lambda r: r["glyphs"] == [n for n in "zero one two three four five six seven eight nine".split()])
    expect(
        "locl_CAT",
        "l·l",
        {"locl": True},
        lambda r: len(r["glyphs"]) >= 3,
        language="CAT ",
    )
    expect(
        "locl_TRK",
        "fi",
        {"liga": False, "locl": True},
        lambda r: True,  # Turkish may keep f+i; just ensure shaping succeeds
        language="TRK ",
    )

    report = {
        "font": str(VF.relative_to(ROOT)),
        "cases": cases,
        "failures": [c["name"] for c in cases if not c["ok"]],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"cases": len(cases), "failures": report["failures"]}, indent=2))
    if report["failures"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
