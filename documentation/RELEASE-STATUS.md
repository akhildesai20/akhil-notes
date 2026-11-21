# Akhil Notes — release status

Authoritative snapshot for Google Fonts technical readiness. Counts and Fontspector numbers below supersede older notes when they disagree.

## Glyph inventory

| Metric | Count | Notes |
| --- | --- | --- |
| Original release codepoints | **491** | Outline-faithful except intentional figure rebuilds |
| Intentional figure rebuilds | **38** | `REBUILD_FIGURES` — supers, subs, fractions (not a regression) |
| Encoded codepoints (shipping) | **698** | Core + Plus + Vietnamese + constructed additions |
| Glyphs (including unencoded) | **846** | Masters / Regular static |

## Build

- **Public / CI:** `python scripts/build_candidate.py --from-ufo` (committed UFOs only; no `provenance/*.ttf`).
- **Maintainer:** `--from-provenance` regenerates masters from the private TTF, then compiles.
- Finalize applies OFL names, STAT, gasp, nested-component flatten, then packages `ofl/akhilnotes/`.
- Vertical metrics: typo **976 / −530**, win **1140 / 523**, line gap 0. Kept for Ắ / ydotbelow; not shrunk for Black Â unless real-app clipping is confirmed.

## Fontspector (`ofl/akhilnotes` VF pair)

Latest local run (see `qa/fontspector/`):

```
SKIP 95  INFO 22  PASS 244  WARN 23  FAIL 0  FATAL 0  ERROR 0
```

| Area | Status |
| --- | --- |
| FAIL | **0** |
| `interpolation_issues` | Sharply reduced after start-point rotate/reverse on Black / BlackItalic UFOs (`scripts/fix_start_points.py`). A few residual WARNs remain (underweight / edge cases). |
| Overlap flags | UFO `public.truetype.overlap` synced from Fontspector lists; build also runs Fontspector `--hotfix` on the VF pair. |
| `googlefonts/vendor_id` | `AKHL` — wait on Microsoft listing (intentional WARN). |
| Outline jaggy / direction / overlapping segments on provenance handwriting | Left alone on purpose. |
| Math widths / contour_count / shape_languages auxiliaries | Intentional handwriting / scope limits. |

## Parity / instantiate

`scripts/audit_final.py`: OTS clean; instantiate weights **400, 500, 650, 700, 900** on upright + italic VFs; upright/italic glyph set, cmap, and GSUB/GPOS feature tags match.

## Remaining (P2 / human)

- Optical review of constructed letters (Æ/Œ/ß/Þ/ð, barred forms, currencies) for recognizability and stroke weight — no geometric “cleanup.”
- Device matrix (Figma / browsers / OS) — human checklist.
- Contextual alternates only from real handwriting samples.
- Vendor ID registration when Microsoft responds.

## Package

- Repo: https://github.com/akhildesai20/akhil-notes  
- Local GF tree: `ofl/akhilnotes/`  
- Copyright: Project Authors line with that URL; OFL 1.1; Reserved Font Name “Akhil Notes.”
