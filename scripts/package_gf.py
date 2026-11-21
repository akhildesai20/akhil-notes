#!/usr/bin/env python3
"""Assemble a local google/fonts-style ofl/akhilnotes/ tree (no git publish).

Ships the weight-only variable pair expected by Google Fonts Workspace.
Statics remain under fonts/ttf/ for local install QA.
"""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "ofl" / "akhilnotes"
FONT_DIR = ROOT / "fonts"

COPYRIGHT = "Copyright 2026 The Akhil Notes Project Authors (https://github.com/akhildesai20/akhil-notes)"
REPO_URL = "https://github.com/akhildesai20/akhil-notes"


def current_commit() -> str:
    try:
        return (
            subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True)
            .strip()
        )
    except Exception:
        return "PENDING"


def write_metadata(path: Path) -> None:
    commit = current_commit()
    lines = [
        'name: "Akhil Notes"',
        'designer: "Akhil Desai"',
        'license: "OFL"',
        'category: "HANDWRITING"',
        'date_added: "2026-11-21"',
        "fonts {",
        '  name: "Akhil Notes"',
        '  style: "normal"',
        "  weight: 400",
        '  filename: "AkhilNotes[wght].ttf"',
        '  post_script_name: "AkhilNotes-Regular"',
        '  full_name: "Akhil Notes Regular"',
        f'  copyright: "{COPYRIGHT}"',
        "}",
        "fonts {",
        '  name: "Akhil Notes"',
        '  style: "italic"',
        "  weight: 400",
        '  filename: "AkhilNotes-Italic[wght].ttf"',
        '  post_script_name: "AkhilNotes-Italic"',
        '  full_name: "Akhil Notes Italic"',
        f'  copyright: "{COPYRIGHT}"',
        "}",
        'subsets: "latin"',
        'subsets: "latin-ext"',
        'subsets: "vietnamese"',
        "axes {",
        '  tag: "wght"',
        "  min_value: 400.0",
        "  max_value: 900.0",
        "}",
        "source {",
        f'  repository_url: "{REPO_URL}"',
        f'  commit: "{commit}"',
        "  files {",
        '    source_file: "OFL.txt"',
        '    dest_file: "OFL.txt"',
        "  }",
        "}",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    for src in (
        FONT_DIR / "variable" / "AkhilNotes[wght].ttf",
        FONT_DIR / "variable" / "AkhilNotes-Italic[wght].ttf",
    ):
        if not src.exists():
            raise SystemExit(f"missing {src}")
        shutil.copy2(src, OUT / src.name)

    for name in ("OFL.txt", "FONTLOG.txt", "AUTHORS.txt", "CONTRIBUTORS.txt"):
        shutil.copy2(ROOT / name, OUT / name)
    shutil.copy2(ROOT / "documentation" / "DESCRIPTION.en_us.html", OUT / "DESCRIPTION.en_us.html")
    write_metadata(OUT / "METADATA.pb")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
