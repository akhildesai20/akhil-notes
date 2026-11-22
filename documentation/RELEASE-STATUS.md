# Akhil Notes — release status

Authoritative snapshot for technical readiness. Prefer this file over older notes when counts disagree. Warn exceptions: [`FONTSPECTOR-EXCEPTIONS.md`](FONTSPECTOR-EXCEPTIONS.md).

## Glyph inventory

| Metric | Count | Notes |
| --- | --- | --- |
| Original release codepoints | **491** | Outline-faithful except intentional figure rebuilds |
| Intentional figure rebuilds | **38** | `REBUILD_FIGURES` — supers, subs, fractions |
| Encoded codepoints (shipping) | **698** | Core + Plus + Vietnamese + constructed |
| Glyphs | **846** | Including unencoded |

## Build

- **Public / CI:** `python scripts/build_candidate.py --from-ufo` (committed UFOs; no provenance).
- Ensures Fontspector via `scripts/ensure_fontspector.py` before overlap hotfix.
- Packages `ofl/akhilnotes/` (tracked shipping VF pair). Statics land under `fonts/ttf/` locally and are meant for **GitHub Releases**, not duplicate git tracking.
- Vertical metrics: typo **976 / −530**, win **1140 / 523**.

## Fontspector (`ofl/akhilnotes` VF pair)

```
FAIL 0 · remaining WARN are documented exceptions (see FONTSPECTOR-EXCEPTIONS.md)
```

Interpolation start-point issues on `ellipsis` / `registered` were fixed with **order-only** contour rotates (no outline redesign).

## Parity

`scripts/audit_final.py`: OTS; instantiate 400–900 upright+italic; glyph/cmap/feature parity.

## Not done without approval

- Google Fonts PR / publish  
- Vendor ID listing wait  
- Human optical pass ([`OPTICAL-REVIEW.md`](OPTICAL-REVIEW.md))  
- Device matrix
