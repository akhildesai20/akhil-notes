# Regenerates UFO masters from the private release and compiles the candidate.
# Run from the repository root.
$ErrorActionPreference = "Stop"
Set-Location (Split-Path $PSScriptRoot -Parent)
if (-not (Test-Path ".\.venv\Scripts\python.exe")) {
  py -3.12 -m venv .venv
  .\.venv\Scripts\python.exe -m pip install -r requirements.txt
}
$env:PYTHONUTF8 = "1"
.\.venv\Scripts\python.exe scripts\build_candidate.py
