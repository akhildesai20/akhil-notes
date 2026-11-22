# Human review checklist

Not automated. Complete before Google Fonts submission.

## Optical / product

Review only. **No geometric cleanup** of provenance handwriting. Do not smooth
baselines, symmetrize bowls, or even terminals.

- [ ] Paragraph texture at 14–21px (upright + italic)
- [ ] Weight ramp recognizability — especially constructed Æ/Œ/ß/Þ/ð and currencies
- [ ] Mid-size (16–21px): constructed caps don’t look mono-linear vs handwriting
- [ ] Black (900): Æ/Œ/Ø/ß stroke weight reads in the same “pen” as D/O/B masters
- [ ] Italic: same constructed set, slant-compatible
- [ ] Currencies: recognizable at 14px; no colliding bars
- [ ] Fractions / supers / subs (intentional figure set): readable
- [ ] `wh` / wherever spacing after kern fix
- [ ] Device matrix: Windows, macOS, iOS, Android, Figma, browsers

Constructed / provisional groups: Ææ Œœ · Ðð Þþ ẞß · Đđ Ħħ Łł Øø · currencies ·
§¶µ — see [`DESIGN-ISSUES.md`](DESIGN-ISSUES.md) and [`proofs/`](proofs/).

### Explicit non-goals

- Mass reverse CCW outers, remove-overlap on original outlines, or AI “cleanup”
- Mono math widths or glyphsets outside Core / Plus / Vietnamese
- Contextual alternates invented from rotations (only from real handwriting)

## Process / legal

- [ ] Microsoft vendor ID `AKHL` — registration requested; confirmation pending
- [ ] Contributor agreement / GF onboarding forms
- [ ] Approve push of local commits & GitHub Release updates if needed
- [ ] Approve google/fonts PR using [`GF-SUBMISSION.md`](GF-SUBMISSION.md)

## Optional assets

- [ ] Replace presentation specimens in `documentation/specimens/` with
      professionally art-directed images (hero, paragraph, notebook comparison,
      weight ramp, applications) — no build/source changes required
- [ ] Provide original notebook photographs for README if desired
  (do not fabricate notebook photos or substitute another handwriting font)

## Outcome log

Record optical decisions here when reviewing (date + glyph + keep / redraw note).
