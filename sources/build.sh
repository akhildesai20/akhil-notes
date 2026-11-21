#!/bin/sh
# Compile shipping fonts from committed UFO masters (no provenance required).
cd "$(dirname "$0")/.." || exit 1
if [ ! -x .venv/bin/python ]; then
  python3 -m venv .venv
  .venv/bin/python -m pip install -r requirements.txt
fi
export PYTHONUTF8=1
.venv/bin/python scripts/build_candidate.py --from-ufo
