# Fontspector exceptions (shipping VF pair)

Authoritative WARN decisions for `ofl/akhilnotes/` variable fonts. Do **not** reshape handwriting to silence these. Latest summary: `qa/fontspector/` and `RELEASE-STATUS.md`.

## Current profile result

- **FAIL / FATAL / ERROR:** 0  
- Remaining items below are **WARN** (typically one per face → **18** total when both upright and italic are checked).

## Intentional handwriting characteristics

These WARNs reflect authentic notebook writing or constructed glyphs that follow the same drawing approach. Changing them would redesign the face.

| Check | Decision |
| --- | --- |
| `outline_direction` | Provenance handwriting and some constructed glyphs (e.g. `.notdef`) may use outer contour directions that match the original drawings. Mass-reversing would change ink. **Keep.** |
| `overlapping_path_segments` | Handwriting and a few constructed glyphs (e.g. `.notdef`, `paragraph`) can share segment coordinates. Remove-overlap would alter drawings. **Keep.** |
| `contour_count` | Digraph dots, ellipsis, and punctuation use handwriting contour counts outside Fontspector’s static “typical” table. **Keep.** |
| `math_signs_width` | Handwriting math, not tabular mono widths. **Keep.** |

## Accepted technical limitations

Engineering or process constraints that are correct for this family, not design defects.

| Check | Decision |
| --- | --- |
| `mandatory_avar_table` | No `avar`. Weight progression is intentionally linear (masters at 400/900). GF guide notes avar is unused for linear axes; Fontspector says this WARN can be ignored when no user-mapping is expected. **Keep — do not add a dummy avar.** |
| `googlefonts/vendor_id` | Vendor ID `AKHL`. Registration requested; confirmation pending. **Keep until Microsoft lists it.** |
| `googlefonts/vertical_metrics` | Typo 976/−530 chosen for Ắ / ydotbelow. Win metrics cover Black Â. Not shrunk for ratio aesthetics. **Keep.** |
| `googlefonts/glyphsets/shape_languages` | Auxiliaries outside Core / Plus / Vietnamese intentionally omitted. **Keep.** |
| `googlefonts/metadata/unreachable_subsetting` | Spacing / mark glyphs declared for subsets in METADATA but not mapped as typical letters. Expected for this inventory. **Keep.** |

## Resolved earlier (order-only / flags)

| Check | Action |
| --- | --- |
| `interpolation_issues` on `ellipsis` | Rotated BlackItalic contour start points (order only). |
| `interpolation_issues` underweight on `registered` | Rotated Black (and BlackItalic) contour 5 start (order only). |
| `overlaps_bit` | UFO lib flags + Fontspector `--hotfix` after `ensure_fontspector.py`. |

## Explicit non-fixes

- No geometric cleanup or CCW mass-reverse of the original 491 outlines.  
- No dummy `avar` solely to clear a WARN.  
- No redesign of overlapping segments unless real paint bugs appear in apps.
