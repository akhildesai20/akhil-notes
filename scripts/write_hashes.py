#!/usr/bin/env python3
"""Write SHA-256 hashes for shipping binaries + source commit pointer."""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "qa" / "candidate" / "hashes.json"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def commit() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    except Exception:
        return "PENDING"


def main() -> None:
    files = []
    for pattern in (
        "ofl/akhilnotes/AkhilNotes[wght].ttf",
        "ofl/akhilnotes/AkhilNotes-Italic[wght].ttf",
    ):
        # brackets are literal filenames
        path = ROOT / "ofl" / "akhilnotes" / Path(pattern).name
        if path.exists():
            files.append({"path": str(path.relative_to(ROOT)).replace("\\", "/"), "sha256": sha256(path)})
    for path in sorted((ROOT / "fonts" / "ttf").glob("*.ttf")):
        files.append({"path": str(path.relative_to(ROOT)).replace("\\", "/"), "sha256": sha256(path)})
    report = {
        "source_commit": commit(),
        "files": files,
        "note": "ofl/ VF pair is the tracked shipping binary; fonts/ttf is local/CI/Releases.",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"commit": report["source_commit"], "files": len(files)}, indent=2))


if __name__ == "__main__":
    main()
