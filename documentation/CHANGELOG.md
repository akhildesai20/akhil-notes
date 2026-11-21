# Changelog

## 2.101 candidate

- OFL 1.1 adopted in the fonts (name IDs 13/14). Copyright uses Project Authors form; git URL still pending.
- Added `meta` (Latn), WWS fsSelection bit, `FONTLOG.txt`, `DESCRIPTION.en_us.html`, local `ofl/akhilnotes/` package.
- Ligatures (`liga`/`dlig`) including Title Case joins; spacing tuned for loose/tight/eased pairs and `ing`.
- Section as squeezed S + centered zero; improved AE/OE/æ/œ/ß/ẞ/Þ/þ/ð and Łł constructions.
- Currency overlays as translate-only composites where possible.

## 2.100 candidate

Engineering candidate built from the version 1.000 release. Not published.

- UFO masters and a designspace replace the TTF-only master pipeline as the editable source.
- All 491 encoded outlines from the release are preserved, including the accented letters the 2.000 development build had redrawn.
- Missing Google Fonts Latin Core, Latin Plus, and Vietnamese codepoints from glyphsets 1.1.3 are constructed and marked provisional.
- `NULL` (U+0000) and `CR` (U+000D) were added. `nbspace` is the no-break space.
- Rotated stylistic alternates are not in the font. They were rigid rotations of the original letters.
- Fraction substitution is split into chained lookups so a fraction does not leave a full-size digit in a multi-digit numerator, and so a following digit after a space stays a digit.
- Kerning no longer keeps pairs that had already hit the generator's −75 floor. Remaining negative pairs are capped at −50. Accented letters share a class with the base letter only when advance and left sidebearing are close.
- Vertical metrics: typo ascender 976, typo descender −530, line gap 0, win metrics equal to the family bounding box. Use Typo Metrics is on.
- Family name is Akhil Notes. Designer and manufacturer are Akhil Desai.
- Fraction digits chain through four places. A digit after a space is left alone.
- Combining marks attach to the original dotted circle (U+25CC). `i` or `ị` followed by an above accent drops the tittle.
- No-break space is named `uni00A0`. U+2028 is an empty line separator with the space width.
- gasp is 0x000F. Static fonts have a STAT table for weight and italic. The font is unhinted.

## 2.000 development

Retained in `baseline/`. 693 encoded characters, 771 glyphs, 4,300 kerning pairs, 12 named instances. It redrew 251 of the original encoded glyphs. Do not treat it as the design source.

## 1.000 release

The owner's variable font. 491 encoded characters. No GPOS kerning. Typo metrics 950 / −450 with line gap 90, and Use Typo Metrics off.
