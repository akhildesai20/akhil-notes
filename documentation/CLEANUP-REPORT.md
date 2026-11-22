# Technical cleanup report

Updated: 2026-11-22 (maintenance pass). Public repo: https://github.com/akhildesai20/akhil-notes  
Release: https://github.com/akhildesai20/akhil-notes/releases/tag/v2.101  

**Not a Google Fonts submission.**

## Principles

- No smoothing or redesign of the 491 original handwritten outlines.  
- Interpolation fixes were **point-order only**.  
- Sources required for reproducible UFO builds retained.

## Specimens

- **Canonical:** `documentation/specimens/` (README links).  
- Duplicate numbered/mirrored sheets removed from `qa/proofs/`.  
- Unique historical QA sheets (accent preservation, texture-kern, etc.) remain under `qa/proofs/` where DESIGN-ISSUES references them.  
- `qa/archive/` removed (nothing depended on it).

## CI

- `ensure_fontspector.py` writes its bindir to `GITHUB_PATH` and sets `FONTSPECTOR_BIN` so later steps find the binary (fixes exit 127).  
- Workflow runs Fontspector with that absolute path, uploads reports as artifacts.

## Remaining Fontspector WARNs

FAIL 0; WARN ≤ 18 documented in [`FONTSPECTOR-EXCEPTIONS.md`](FONTSPECTOR-EXCEPTIONS.md), split into **intentional handwriting characteristics** vs **accepted technical limitations**.

## Tracking

| Tracked | Not tracked (generated / release) |
| --- | --- |
| UFO masters, designspace, features, scripts, OFL | `fonts/ttf/`, `fonts/variable/`, `fonts/webfonts/` |
| `ofl/akhilnotes/` VF pair + metadata | `tools/`, `dist/`, `qa/artifacts/` |
| `documentation/specimens/*.png` | Specimen `_tmp/` instances |
