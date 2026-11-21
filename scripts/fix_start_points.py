#!/usr/bin/env python3
"""Rotate/reverse UFO contour point order from Fontspector interpolation proposals.

Order-only edits: point counts and coordinates must not change (multiset-stable).
Applies to Black / BlackItalic (wght=900 reports). Composite-only glyphs are skipped;
fix shared bases first so composites inherit after recompile.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

from ufoLib2 import Font
from ufoLib2.objects.point import Point

ROOT = Path(__file__).resolve().parents[1]
MASTER_DIR = ROOT / "sources" / "masters"
DEFAULT_REPORT = ROOT / "qa" / "fontspector" / "googlefonts.json"

FACE_TO_UFO = {
    "AkhilNotes[wght].ttf": "AkhilNotes-Black.ufo",
    "AkhilNotes-Italic[wght].ttf": "AkhilNotes-BlackItalic.ufo",
}

# Shared bases / punctuation first so composites inherit after recompile.
PRIORITY = (
    "D",
    "period",
    "exclam",
    "colon",
    "semicolon",
    "quotedbl",
    "quotedblleft",
    "quotedblright",
    "quoteleft",
    "quoteright",
    "quotesinglbase",
    "quotedblbase",
    "dieresis",
    "dotaccent",
    "comma",
)


def parse_proposals(report_path: Path) -> dict[tuple[str, str, int], tuple[int, bool]]:
    """Return {(ufo_name, glyph, contour_index): (start, reverse)} for wght=900 start-point issues."""
    data = json.loads(report_path.read_text(encoding="utf-8"))
    fixes: dict[tuple[str, str, int], tuple[int, bool]] = {}
    for face, sections in data.get("results", {}).items():
        if face not in FACE_TO_UFO:
            continue
        ufo_name = FACE_TO_UFO[face]
        for _section, checks in sections.items():
            for check in checks:
                if check.get("check_id") != "interpolation_issues":
                    continue
                for sr in check.get("subresults") or []:
                    for meta in sr.get("metadata") or []:
                        gp = meta.get("GlyphProblem")
                        if not gp:
                            continue
                        exp = gp.get("expected") or {}
                        act = gp.get("actual") or {}
                        if "proposed_start_point" not in exp:
                            continue
                        loc = gp.get("userspace_location") or {}
                        if loc.get("wght") not in (900, 900.0):
                            continue
                        key = (ufo_name, gp["glyph_name"], int(act["contour_index"]))
                        val = (int(exp["proposed_start_point"]), bool(exp.get("reverse_contour", False)))
                        if key in fixes and fixes[key] != val:
                            raise SystemExit(f"Conflicting proposal for {key}: {fixes[key]} vs {val}")
                        fixes[key] = val
    return fixes


def coords(points: list[Point]) -> list[tuple[float, float, str | None, bool]]:
    return [(p.x, p.y, p.type, bool(p.smooth)) for p in points]


def apply_order(points: list[Point], start: int, reverse: bool) -> list[Point]:
    """Rotate so ``start`` becomes index 0; optionally reverse after rotate.

    Fontspector/Rust interpolatable sometimes reports a start index ``>= n`` when
    ``reverse_contour`` is set (isomorphism over a doubled ring). Normalize with
    ``start % n``. Coordinates are only reordered, never changed.
    """
    n = len(points)
    if n == 0:
        return points
    if start < 0:
        raise ValueError(f"negative start {start}")
    start = start % n
    rotated = points[start:] + points[:start]
    if reverse:
        # Reverse order but keep the new start point at index 0.
        rotated = [rotated[0]] + list(reversed(rotated[1:]))
    return rotated


def set_points(contour, points: list[Point]) -> None:
    contour.points.clear()
    contour.points.extend(points)


def priority_key(glyph: str) -> tuple[int, str]:
    try:
        return (PRIORITY.index(glyph), glyph)
    except ValueError:
        for i, base in enumerate(PRIORITY):
            if glyph == base or glyph.startswith(base):
                return (i, glyph)
        return (len(PRIORITY), glyph)


def fix_ufo(ufo_path: Path, proposals: list[tuple[str, int, int, bool]], *, dry_run: bool) -> dict:
    font = Font.open(ufo_path)
    applied = []
    skipped = []
    for glyph_name, contour_index, start, reverse in proposals:
        if glyph_name not in font:
            skipped.append({"glyph": glyph_name, "reason": "missing"})
            continue
        glyph = font[glyph_name]
        if not glyph.contours:
            skipped.append({"glyph": glyph_name, "reason": "composite-or-empty"})
            continue
        if contour_index >= len(glyph.contours):
            skipped.append({"glyph": glyph_name, "contour": contour_index, "reason": "contour-oob"})
            continue
        contour = glyph.contours[contour_index]
        before = list(contour.points)
        after = apply_order(before, start, reverse)
        if sorted(coords(before)) != sorted(coords(after)):
            raise SystemExit(
                f"Coordinate multiset changed for {ufo_path.name} {glyph_name} contour {contour_index}"
            )
        if coords(before) == coords(after):
            skipped.append({"glyph": glyph_name, "contour": contour_index, "reason": "already-aligned"})
            continue
        if not dry_run:
            set_points(contour, after)
        applied.append(
            {
                "glyph": glyph_name,
                "contour": contour_index,
                "start": start,
                "reverse": reverse,
                "points": len(before),
            }
        )
    if applied and not dry_run:
        font.save(ufo_path, overwrite=True)
    return {"ufo": ufo_path.name, "applied": applied, "skipped": skipped}


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    if not args.report.exists():
        raise SystemExit(f"Missing Fontspector report: {args.report}")
    fixes = parse_proposals(args.report)
    by_ufo: dict[str, list[tuple[str, int, int, bool]]] = defaultdict(list)
    for (ufo_name, glyph, contour), (start, reverse) in fixes.items():
        by_ufo[ufo_name].append((glyph, contour, start, reverse))
    reports = []
    for ufo_name in sorted(by_ufo):
        items = sorted(by_ufo[ufo_name], key=lambda t: (priority_key(t[0]), t[1]))
        path = MASTER_DIR / ufo_name
        if not path.exists():
            raise SystemExit(f"Missing UFO: {path}")
        print(f"{ufo_name}: {len(items)} proposals", flush=True)
        reports.append(fix_ufo(path, items, dry_run=args.dry_run))
    summary = {
        "dry_run": args.dry_run,
        "proposals": len(fixes),
        "applied": sum(len(r["applied"]) for r in reports),
        "skipped": sum(len(r["skipped"]) for r in reports),
        "reports": reports,
    }
    out = ROOT / "qa" / "candidate" / "start-point-fixes.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps({k: summary[k] for k in ("dry_run", "proposals", "applied", "skipped")}, indent=2))


if __name__ == "__main__":
    main()
