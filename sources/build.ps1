# Compile shipping fonts from committed UFO masters (no provenance required).
# Run from the repository root, or call this script from anywhere.
$ErrorActionPreference = "Stop"
Set-Location (Split-Path $PSScriptRoot -Parent)
if (-not (Test-Path ".\.venv\Scripts\python.exe")) {
  py -3.12 -m venv .venv
  .\.venv\Scripts\python.exe -m pip install -r requirements.txt
}
$env:PYTHONUTF8 = "1"
.\.venv\Scripts\python.exe scripts\build_candidate.py --from-ufo
