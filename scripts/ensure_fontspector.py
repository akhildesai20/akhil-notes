#!/usr/bin/env python3
"""Ensure a Fontspector binary is available before hotfix / QA steps.

Looks on PATH, then under tools/fontspector/. If missing, downloads the
platform release asset into tools/ (gitignored). Returns the executable path.
"""
from __future__ import annotations

import os
import platform
import shutil
import subprocess
import sys
import tarfile
import zipfile
from pathlib import Path
from urllib.request import urlretrieve

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools" / "fontspector"
VERSION = "1.9.1"
TAG = f"fontspector-v{VERSION}"
BASE = f"https://github.com/fonttools/fontspector/releases/download/{TAG}"


def _asset_for_platform() -> tuple[str, str]:
    system = platform.system().lower()
    machine = platform.machine().lower()
    if system == "windows":
        return f"fontspector-{VERSION}-x86_64-pc-windows-gnu.zip", "fontspector.exe"
    if system == "darwin":
        arch = "aarch64" if machine in ("arm64", "aarch64") else "x86_64"
        return f"fontspector-{VERSION}-{arch}-apple-darwin.tar.gz", "fontspector"
    # linux
    return f"fontspector-{VERSION}-x86_64-unknown-linux-gnu.tar.gz", "fontspector"


def find_fontspector() -> Path | None:
    which = shutil.which("fontspector")
    if which:
        return Path(which)
    name = "fontspector.exe" if platform.system().lower() == "windows" else "fontspector"
    for path in TOOLS.rglob(name):
        if path.is_file():
            return path
    return None


def ensure_fontspector(*, download: bool = True) -> Path:
    found = find_fontspector()
    if found:
        return found
    if not download:
        raise SystemExit(
            "Fontspector not found. Install it or run: python scripts/ensure_fontspector.py"
        )
    asset, binary_name = _asset_for_platform()
    TOOLS.mkdir(parents=True, exist_ok=True)
    archive = TOOLS / asset
    url = f"{BASE}/{asset}"
    print(f"Downloading Fontspector {VERSION}: {url}", flush=True)
    urlretrieve(url, archive)
    extract_dir = TOOLS / asset.replace(".zip", "").replace(".tar.gz", "")
    extract_dir.mkdir(parents=True, exist_ok=True)
    if asset.endswith(".zip"):
        with zipfile.ZipFile(archive) as zf:
            zf.extractall(extract_dir)
    else:
        with tarfile.open(archive, "r:gz") as tf:
            tf.extractall(extract_dir)
    found = next(extract_dir.rglob(binary_name), None)
    if not found:
        raise SystemExit(f"Fontspector binary not found after extracting {archive}")
    if os.name != "nt":
        found.chmod(found.stat().st_mode | 0o111)
    print(f"Fontspector ready: {found}", flush=True)
    # smoke
    subprocess.run([str(found), "--version"], check=False)
    return found


def main() -> None:
    path = ensure_fontspector(download=True)
    print(path)


if __name__ == "__main__":
    main()
