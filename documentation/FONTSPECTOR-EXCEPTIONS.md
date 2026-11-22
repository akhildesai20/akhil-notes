# Fontspector exceptions (shipping VF pair)

Authoritative WARN decisions for `ofl/akhilnotes/` variable fonts. Do **not** reshape handwriting to silence these. Latest summary lives in `qa/fontspector/` and `RELEASE-STATUS.md`.

## Current profile result

After order-only start-point fixes on `ellipsis` / `registered` and overlap-flag hotfix:

- **FAIL / FATAL / ERROR:** 0  
- Remaining items below are **WARN** (typically one per face → ~18 total).

## Legitimate exceptions

| Check | Decision |
| --- | --- |
| `mandatory_avar_table` | No `avar`. Weight progression is intentionally linear (masters at 400/900). GF guide notes avar is unused for linear axes; Fontspector itself says this WARN can be ignored when no user-mapping is expected. An identity table would only silence the check. **Keep — do not add dummy avar.** |
| `googlefonts/vendor_id` | `AKHL` registered with Microsoft; listing pending. **Keep until listed.** |
| `googlefonts/vertical_metrics` | Typo 976/−530 chosen for Ắ / ydotbelow. Win metrics cover Black Â. Not shrunk for ratio aesthetics. **Keep.** |
| `outline_direction` | Handwriting + constructed `.notdef` / figures may use CCW outers matching provenance. Mass-reversing would redesign ink. **Keep.** |
| `overlapping_path_segments` | Provenance handwriting and a few constructed glyphs (e.g. `.notdef`, `paragraph`) share segment coordinates. Remove-overlap would change drawings. **Keep.** |
| `contour_count` | Digraph dots / ellipsis / punctuation use handwriting contour counts outside the static “typical” table. **Keep.** |
| `math_signs_width` | Handwriting math, not tabular mono. **Keep.** |
| `googlefonts/glyphsets/shape_languages` | Auxiliaries outside Core / Plus / Vietnamese intentionally omitted. **Keep.** |

## Resolved in this cleanup

| Check | Action |
| --- | --- |
| `interpolation_issues` on `ellipsis` | Rotated BlackItalic contour start points (order only). |
| `interpolation_issues` underweight on `registered` | Rotated Black (and BlackItalic) contour 5 start (order only). |
| `overlaps_bit` | UFO lib flags + Fontspector `--hotfix` gated on an installed binary (`scripts/ensure_fontspector.py`). |

## Explicit non-fixes

- No geometric cleanup, smoothing, or CCW mass-reverse of original 491 outlines.  
- No dummy `avar` solely to clear a WARN.  
- No redesign of `.notdef` / `paragraph` overlapping segments unless real paint bugs appear in apps.
