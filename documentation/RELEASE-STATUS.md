# Akhil Notes — release status

Authoritative numbers for the current engineering candidate. Prefer this file when docs disagree. Warn policy: [`FONTSPECTOR-EXCEPTIONS.md`](FONTSPECTOR-EXCEPTIONS.md). Positioning: [`ABOUT.md`](ABOUT.md).

**Not submitted to Google Fonts. Not optically signed off.**

## Inventory (shipping binaries)

| Metric | Count |
| --- | --- |
| Original release codepoints | 491 (outline-faithful except 38 intentional figure rebuilds) |
| Encoded Unicode | **698** |
| Glyphs | **846** |
| Static styles | **12** (Regular–Black × upright/italic) |
| Variable fonts | Upright + italic `wght` 400–900 |

## Build

- Public: `python scripts/build_candidate.py --from-ufo`  
- Fontspector ensured before overlap hotfix  
- Package: `ofl/akhilnotes/`  
- Statics: `fonts/ttf/` → GitHub Releases / CI artifacts (not duplicate-tracked)  
- Specimens: `python scripts/make_specimens.py` → `documentation/specimens/`  

## Fontspector (VF pair)

**FAIL / FATAL / ERROR: 0.** Remaining WARNs are documented exceptions (no `avar` for linear weight; vendor ID pending; handwriting outline direction / overlapping segments; contour_count; math widths; glyphset language auxiliaries; vertical metrics choice).

## Automated QA

| Check | Result |
| --- | --- |
| OTS | Pass |
| Instantiate 400–900 | Pass |
| Upright/italic glyph, cmap, feature parity | Pass |
| HarfBuzz feature harness | Pass |
| Binary hashes | `qa/candidate/hashes.json` |

## Human remaining

- [ ] Optical review ([`OPTICAL-REVIEW.md`](OPTICAL-REVIEW.md))  
- [ ] Device matrix  
- [ ] Vendor ID listing confirmation  
- [ ] Contributor agreement / GF onboarding steps  
- [ ] Approval to push release & open google/fonts PR ([`GF-SUBMISSION.md`](GF-SUBMISSION.md))  
