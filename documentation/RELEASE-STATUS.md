# Akhil Notes — release status

Authoritative numbers for the public repository. Prefer this file when docs disagree.

Warn policy: [`FONTSPECTOR-EXCEPTIONS.md`](FONTSPECTOR-EXCEPTIONS.md)  
Positioning: [`ABOUT.md`](ABOUT.md)  
**Not submitted to Google Fonts. Optical sign-off remains human.**

## Public presence

| Item | Value |
| --- | --- |
| Repository | https://github.com/akhildesai20/akhil-notes |
| Release | [v2.101](https://github.com/akhildesai20/akhil-notes/releases/tag/v2.101) |
| CI | [Build workflow](https://github.com/akhildesai20/akhil-notes/actions/workflows/build.yml) |
| Package | `ofl/akhilnotes/` |
| Specimens (canonical) | `documentation/specimens/` |

## Inventory (shipping binaries)

| Metric | Count |
| --- | --- |
| Original release codepoints | 491 (outline-faithful except 38 intentional figure rebuilds) |
| Encoded Unicode | **698** |
| Glyphs | **846** |
| Static styles | **12** |
| Variable fonts | Upright + italic `wght` 400–900 |

## Build

- Public: `python scripts/build_candidate.py --from-ufo`  
- Fontspector via `scripts/ensure_fontspector.py` (exports `GITHUB_PATH` / `FONTSPECTOR_BIN` in CI)  
- Statics: GitHub Releases / CI artifacts (not duplicate-tracked in git)  
- Specimens: `python scripts/make_specimens.py` → `documentation/specimens/` only  

## Fontspector (VF pair)

**FAIL / FATAL / ERROR: 0.** Documented WARN ceiling: **18** (both faces). See CI artifact `akhil-notes-fontspector` and `qa/fontspector/googlefonts.json` after a green run.

## Automated QA

| Check | Expected |
| --- | --- |
| OTS | Pass |
| Instantiate 400–900 | Pass |
| Upright/italic parity | Pass |
| HarfBuzz features | Pass |
| Hashes | `qa/candidate/hashes.json` (commit + ofl VF + local statics when present) |
| METADATA.pb `source.commit` | Matches the commit that produced the packaged tree |

## Human remaining

- [ ] Optical review ([`OPTICAL-REVIEW.md`](OPTICAL-REVIEW.md))  
- [ ] Device matrix  
- [ ] Vendor ID confirmation (registration requested; confirmation pending)  
- [ ] Contributor agreement / GF onboarding  
- [ ] Approval to open a google/fonts PR ([`GF-SUBMISSION.md`](GF-SUBMISSION.md))  
