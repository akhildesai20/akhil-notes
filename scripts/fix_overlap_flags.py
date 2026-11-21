#!/usr/bin/env python3
"""Set/clear overlap flags only (no geometry edits).

1. UFO masters: set/clear ``public.truetype.overlap`` from a Fontspector
   ``overlaps_bit`` JSON report (``--full-lists``), applied to all masters.
2. Optional ``--ttf``: set OVERLAP_SIMPLE / OVERLAP_COMPOUND on compiled fonts
   from the same map (or from Regular UFO lib after step 1).
3. Optional ``--hotfix``: run Fontspector ``--hotfix`` on VF binaries when the
   binary is on PATH / under tools/fontspector.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._g_l_y_f import OVERLAP_COMPOUND, flagOverlapSimple
from ufoLib2 import Font

ROOT = Path(__file__).resolve().parents[1]
MASTER_DIR = ROOT / "sources" / "masters"
MASTERS = (
    "AkhilNotes-Regular.ufo",
    "AkhilNotes-Black.ufo",
    "AkhilNotes-Italic.ufo",
    "AkhilNotes-BlackItalic.ufo",
)
LIB_KEY = "public.truetype.overlap"
DEFAULT_REPORT = ROOT / "qa" / "fontspector" / "googlefonts.json"


def _glyph_token(line: str) -> str | None:
    line = line.strip().lstrip("*• ").strip()
    if not line or line.startswith("...") or line.startswith("The following"):
        return None
    # "iacute (U+00ED)" or "caroncomb.alt"
    m = re.match(r"^([A-Za-z0-9_\.]+)", line)
    return m.group(1) if m else None


def parse_overlap_lists(report_path: Path) -> tuple[set[str], set[str]]:
    """Return (need_bit, clear_bit) glyph name sets from Fontspector JSON."""
    data = json.loads(report_path.read_text(encoding="utf-8"))
    need: set[str] = set()
    clear: set[str] = set()
    for face, sections in data.get("results", {}).items():
        if not face:
            continue
        for _section, checks in sections.items():
            for check in checks:
                if check.get("check_id") != "overlaps_bit":
                    continue
                for sr in check.get("subresults") or []:
                    msg = sr.get("message") or ""
                    code = sr.get("code")
                    names = {n for line in msg.splitlines() if (n := _glyph_token(line))}
                    if code == "no-overlaps-bit":
                        need |= names
                    elif code == "overlaps-bit-set":
                        clear |= names
    # Prefer need when both (shouldn't happen)
    clear -= need
    return need, clear


def apply_ufo_flags(need: set[str], clear: set[str], *, dry_run: bool) -> list[dict]:
    reports = []
    for master in MASTERS:
        path = MASTER_DIR / master
        font = Font.open(path)
        set_true, set_false = [], []
        for name in need:
            if name not in font:
                continue
            if not font[name].lib.get(LIB_KEY):
                set_true.append(name)
                if not dry_run:
                    font[name].lib[LIB_KEY] = True
        for name in clear:
            if name not in font:
                continue
            if font[name].lib.get(LIB_KEY):
                set_false.append(name)
                if not dry_run:
                    font[name].lib.pop(LIB_KEY, None)
        if (set_true or set_false) and not dry_run:
            font.save(path, overwrite=True)
        reports.append({"ufo": master, "set_true": set_true, "set_false": set_false})
    return reports


def apply_ttf_flags(path: Path, need: set[str], clear: set[str]) -> dict:
    font = TTFont(path)
    glyf = font["glyf"]
    changed = 0

    def set_flag(name: str, should: bool) -> None:
        nonlocal changed
        if name not in glyf:
            return
        g = glyf[name]
        if getattr(g, "isComposite", lambda: False)():
            if not g.components:
                return
            flags = g.components[0].flags
            has = bool(flags & OVERLAP_COMPOUND)
            if should and not has:
                g.components[0].flags = flags | OVERLAP_COMPOUND
                changed += 1
            elif not should and has:
                g.components[0].flags = flags & ~OVERLAP_COMPOUND
                changed += 1
        else:
            if g.numberOfContours < 1 or not hasattr(g, "flags") or len(g.flags) == 0:
                return
            has = bool(g.flags[0] & flagOverlapSimple)
            if should and not has:
                g.flags[0] = int(g.flags[0]) | flagOverlapSimple
                changed += 1
            elif not should and has:
                g.flags[0] = int(g.flags[0]) & ~flagOverlapSimple
                changed += 1

    for name in need:
        set_flag(name, True)
    for name in clear:
        set_flag(name, False)
    font.save(path)
    return {"path": str(path), "changed": changed}


def find_fontspector() -> Path | None:
    cand = ROOT / "tools" / "fontspector" / "fontspector-1.9.1-x86_64-pc-windows-gnu" / "fontspector.exe"
    return cand if cand.exists() else None


def run_fontspector_hotfix(fonts: list[Path]) -> None:
    fs = find_fontspector()
    if not fs:
        print("fontspector not found; skip --hotfix", flush=True)
        return
    # Copy to temp names without brackets for Windows, hotfix, copy back
    import shutil
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        mapping = []
        for src in fonts:
            dst = tmp_path / src.name.replace("[", "").replace("]", "")
            shutil.copy2(src, dst)
            mapping.append((src, dst))
        cmd = [str(fs), "-p", "googlefonts", "--skip-network", "-c", "overlaps_bit", "--hotfix", "--full-lists"]
        cmd += [str(d) for _, d in mapping]
        print(" ".join(cmd), flush=True)
        subprocess.run(cmd, check=False)
        for src, dst in mapping:
            shutil.copy2(dst, src)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--ttf", nargs="*", type=Path, default=None)
    parser.add_argument("--hotfix", action="store_true", help="Run Fontspector overlaps_bit hotfix on VF pair")
    parser.add_argument("--full-lists-refresh", action="store_true", help="Re-run Fontspector with --full-lists into report")
    args = parser.parse_args(argv)

    if args.full_lists_refresh:
        fs = find_fontspector()
        if not fs:
            raise SystemExit("fontspector binary missing")
        ofl = ROOT / "ofl" / "akhilnotes"
        cmd = [
            str(fs), "-p", "googlefonts", "--skip-network", "--full-lists",
            "-c", "overlaps_bit",
            "--json", str(args.report.with_name("overlaps-full.json")),
            "AkhilNotes[wght].ttf", "AkhilNotes-Italic[wght].ttf",
        ]
        print(" ".join(cmd), flush=True)
        subprocess.run(cmd, cwd=ofl, check=False)
        args.report = args.report.with_name("overlaps-full.json")

    if not args.report.exists():
        raise SystemExit(f"Missing report {args.report}")
    need, clear = parse_overlap_lists(args.report)
    # Truncated lists still help; warn if message had "and N others"
    print(f"from report: need={len(need)} clear={len(clear)}", flush=True)
    reports = apply_ufo_flags(need, clear, dry_run=args.dry_run)

    ttf_reports = []
    if args.ttf is not None and not args.dry_run:
        targets = args.ttf or [
            ROOT / "fonts" / "variable" / "AkhilNotes[wght].ttf",
            ROOT / "fonts" / "variable" / "AkhilNotes-Italic[wght].ttf",
        ]
        for t in targets:
            if t.exists():
                ttf_reports.append(apply_ttf_flags(t, need, clear))

    if args.hotfix and not args.dry_run:
        vfs = [
            ROOT / "fonts" / "variable" / "AkhilNotes[wght].ttf",
            ROOT / "fonts" / "variable" / "AkhilNotes-Italic[wght].ttf",
        ]
        run_fontspector_hotfix([p for p in vfs if p.exists()])

    summary = {
        "need": len(need),
        "clear": len(clear),
        "need_sample": sorted(need)[:15],
        "clear_sample": sorted(clear)[:15],
        "ufo": [{"ufo": r["ufo"], "set_true": len(r["set_true"]), "set_false": len(r["set_false"])} for r in reports],
        "ttf": ttf_reports,
    }
    out = ROOT / "qa" / "candidate" / "overlap-flag-fixes.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2)[:800])


if __name__ == "__main__":
    main()
