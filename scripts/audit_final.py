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
    rows = []
    font = TTFont(path)
    axes = {a.axisTag for a in font["fvar"].axes}
    locations = []
    if "wght" in axes:
        for weight in (400, 500, 650, 900):
            loc = {"wght": weight}
            if "slnt" in axes:
                loc["slnt"] = 0
            locations.append(loc)
    if "slnt" in axes:
        locations.append({"wght": 700, "slnt": -15})
    for loc in locations:
        try:
            inst = instantiateVariableFont(TTFont(path), loc, inplace=False)
            rows.append({"location": loc, "glyphs": len(inst.getGlyphOrder()), "cmap": len(inst.getBestCmap())})
        except Exception as exc:
            rows.append({"location": loc, "error": str(exc)})
    return rows


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
    report = {
        "ots": "9.2.0",
        "ots_results": ots_rows,
        "instantiate": inst_rows,
        "ots_failures": [row for row in ots_rows if not row["ok"]],
    }
    (OUT / "ots-instantiate.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    inventory()
    print(json.dumps({"fonts": len(ots_rows), "ots_failures": len(report["ots_failures"])}, indent=2))
    if report["ots_failures"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
