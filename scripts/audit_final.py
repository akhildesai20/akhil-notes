"""Local checks that do not need Fontspector: OTS, instantiate, inventory."""
import json
import sys
from pathlib import Path

from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
import ots

ROOT = Path(__file__).resolve().parents[1]
FONTS = ROOT / "fonts"
OUT = ROOT / "qa" / "candidate"
OUT.mkdir(parents=True, exist_ok=True)


def ots_check(path: Path) -> dict:
    try:
        result = ots.sanitize(str(path), capture_output=True)
        stderr = (result.stderr or b"").decode("utf-8", "replace").strip()
        return {
            "path": str(path.relative_to(ROOT)),
            "ok": result.returncode == 0,
            "returncode": result.returncode,
            "stderr": stderr,
        }
    except Exception as exc:
        return {"path": str(path.relative_to(ROOT)), "ok": False, "error": str(exc)}


def instantiate(path: Path) -> list:
    """Instantiate across shipping weights (upright + italic faces checked separately)."""
    rows = []
    font = TTFont(path)
    axes = {a.axisTag for a in font["fvar"].axes}
    locations = []
    weights = (400, 500, 650, 700, 900)
    if "wght" in axes:
        for weight in weights:
            loc = {"wght": weight}
            if "slnt" in axes:
                loc["slnt"] = 0
            locations.append(loc)
            if "slnt" in axes:
                locations.append({"wght": weight, "slnt": -15})
    elif "slnt" in axes:
        for weight in weights:
            locations.append({"wght": weight, "slnt": -15})
    # Deduplicate while preserving order
    seen = set()
    uniq = []
    for loc in locations:
        key = tuple(sorted(loc.items()))
        if key not in seen:
            seen.add(key)
            uniq.append(loc)
    for loc in uniq:
        try:
            inst = instantiateVariableFont(TTFont(path), loc, inplace=False)
            rows.append({"location": loc, "glyphs": len(inst.getGlyphOrder()), "cmap": len(inst.getBestCmap())})
        except Exception as exc:
            rows.append({"location": loc, "error": str(exc)})
    return rows


def feature_tags(font: TTFont) -> list[str]:
    tags = []
    for table in ("GSUB", "GPOS"):
        if table not in font:
            continue
        for fr in font[table].table.FeatureList.FeatureRecord:
            tags.append(fr.FeatureTag)
    return sorted(set(tags))


def upright_italic_parity() -> dict:
    up = TTFont(FONTS / "variable" / "AkhilNotes[wght].ttf")
    it = TTFont(FONTS / "variable" / "AkhilNotes-Italic[wght].ttf")
    up_glyphs = set(up.getGlyphOrder())
    it_glyphs = set(it.getGlyphOrder())
    up_cmap = set(up.getBestCmap())
    it_cmap = set(it.getBestCmap())
    up_feat = feature_tags(up)
    it_feat = feature_tags(it)
    return {
        "glyph_count_upright": len(up_glyphs),
        "glyph_count_italic": len(it_glyphs),
        "glyphs_only_upright": sorted(up_glyphs - it_glyphs)[:40],
        "glyphs_only_italic": sorted(it_glyphs - up_glyphs)[:40],
        "cmap_only_upright": [f"U+{cp:04X}" for cp in sorted(up_cmap - it_cmap)[:40]],
        "cmap_only_italic": [f"U+{cp:04X}" for cp in sorted(it_cmap - up_cmap)[:40]],
        "features_upright": up_feat,
        "features_italic": it_feat,
        "features_only_upright": sorted(set(up_feat) - set(it_feat)),
        "features_only_italic": sorted(set(it_feat) - set(up_feat)),
        "glyph_set_match": up_glyphs == it_glyphs,
        "cmap_match": up_cmap == it_cmap,
        "features_match": set(up_feat) == set(it_feat),
    }


def inventory() -> None:
    font = TTFont(FONTS / "ttf" / "AkhilNotes-Regular.ttf")
    cmap = font.getBestCmap()
    lines = ["# Character inventory", "", "Encoded characters in `fonts/ttf/AkhilNotes-Regular.ttf`.", ""]
    lines.append("| Codepoint | Character | Glyph |")
    lines.append("| --- | --- | --- |")
    for cp in sorted(cmap):
        glyph = cmap[cp]
        char = chr(cp) if cp >= 32 else ""
        lines.append(f"| U+{cp:04X} | {char} | `{glyph}` |")
    (ROOT / "documentation" / "CHARACTER-INVENTORY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    targets = [
        FONTS / "variable" / "AkhilNotes[wght].ttf",
        FONTS / "variable" / "AkhilNotes-Italic[wght].ttf",
        FONTS / "variable-slant" / "AkhilNotes[slnt,wght].ttf",
    ]
    targets += sorted((FONTS / "ttf").glob("*.ttf"))
    ots_rows = [ots_check(path) for path in targets]
    inst_rows = {
        "AkhilNotes[wght].ttf": instantiate(FONTS / "variable" / "AkhilNotes[wght].ttf"),
        "AkhilNotes-Italic[wght].ttf": instantiate(FONTS / "variable" / "AkhilNotes-Italic[wght].ttf"),
        "AkhilNotes[slnt,wght].ttf": instantiate(FONTS / "variable-slant" / "AkhilNotes[slnt,wght].ttf"),
    }
    parity = upright_italic_parity()
    report = {
        "ots": "9.2.0",
        "ots_results": ots_rows,
        "instantiate": inst_rows,
        "ots_failures": [row for row in ots_rows if not row["ok"]],
        "upright_italic_parity": parity,
        "instantiate_weights": [400, 500, 650, 700, 900],
    }
    (OUT / "ots-instantiate.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    inventory()
    print(
        json.dumps(
            {
                "fonts": len(ots_rows),
                "ots_failures": len(report["ots_failures"]),
                "parity_glyphs": parity["glyph_set_match"],
                "parity_cmap": parity["cmap_match"],
                "parity_features": parity["features_match"],
            },
            indent=2,
        )
    )
    if report["ots_failures"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
