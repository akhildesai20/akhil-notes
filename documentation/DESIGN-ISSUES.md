# Design issues for hand review

These are not approved. Codepoints refer to the candidate Regular at `fonts/ttf/AkhilNotes-Regular.ttf`. Screenshots are FreeType rasters, not device captures.

## 1. Provisional constructed letters

These were not in the original release. They are built from the handwritten stems and letters. Review them against the rest of the hand before calling the set finished.

Look at `documentation/proofs/focus-symbols-regular.png`.

| Priority | Codepoints | What to look at |
| --- | --- | --- |
| High | U+00C6 Æ, U+00E6 æ, U+0152 Œ, U+0153 œ | Built from your A/E, O/E, a/e, o/e with shared spines (`join_letters`). Review optical join. |
| High | U+00DF ß, U+1E9E ẞ | ß = your f+s (ſs); ẞ = optically taller ß. Review if you want a different sharp-s habit. |
| High | U+00DE Þ, U+00FE þ | Your I/l stem + P/p bowl on one centerline. |
| High | U+00D0 Ð, U+00F0 ð, U+0110 Đ, U+0111 đ, U+0126 Ħ, U+0127 ħ, U+0141 Ł, U+0142 ł | Letter + your en-dash / slash / diagonal at `self.width`. |
| High | Currencies on the focus sheet | Letter + `l` / en-dash overlays, or strokes at `self.width` (₺ ₪ ₨). |
| Medium | U+00A7 §, U+00B6 ¶, U+00B5 µ, U+2113 ℓ, U+2126 Ω, U+222B ∫ | § is squeezed S + centered 0 (2.101). ¶ and the rest are still invented strokes. |
| Medium | U+2196–U+2199 arrows, U+25AA–U+25C3 geometric shapes, U+24B9 Ⓓ | Rotations and scaled copies of arrows and blocks. Sizes should be checked against the period and the bullet you already drew. |
| Low | Combining marks U+0300–U+0328 that were not in the release | Built at about 24 units at Regular and 70 at Black so they match the stem of l. They are smoother than your letters. |

Checkboxes U+2610 and U+2611 are already in the release and were not redrawn.

## 2. Accents that stayed yours

`documentation/proofs/accent-preservation.png` shows the release, the 2.000 rebuild, and this candidate. The candidate matches the release on the accents that were already drawn. The 2.000 build replaced those with new marks. That replacement is undone here.

Still look at clearance yourself, especially:

- U+00C2 Â. At Black the outline reaches y=1139, above the typo ascender 976. Win ascent is 1140, so Windows clipping is covered, but a line above can meet this circumflex. The Google Fonts guide sets the typo ascender from Ắ (here y=966, so the ascender stays 976). Raising it to 1140 would loosen every line.
- U+1EF5 ỵ. The dot below reaches y=−523 at Black. The typo descender is −530 so the dot sits inside the line box. The dot is a constructed mark on your y.

## 3. Alternates

Repeated-letter rotations of about 1.6° were removed from the font. They are not handwriting. If you want alternates, draw them. A `calt` that swaps in rotations should not come back.

## 4. Kerning

Kerning is on by default. Pairs that the old generator pinned at −75 were removed. Other negative pairs are capped at −50. `documentation/proofs/texture-kern-compare.png` compares the release (no kerning), the 2.000 build, and this candidate with kerning on and off. On the sentence "The way I write, wherever I type." the candidate with kerning is 375 units shorter than with kerning off. That is a mild tighten, not a finished kerning pass. Accented capitals whose sidebearings differ from the base letter enough to break class kerning are excluded from the shared class at build time.

## 5. Shaping compromises

- U+25CC ◌ is the dotted circle from the version 1.000 release. It now has the same mark anchors as the letters, so a combining accent sits on it. The drawing was not replaced.
- U+1ECB ị and U+012F į, when an above accent follows, become dotless i plus the below mark plus the accent. Standalone į stays the original glyph. The stacked form is not a separate drawing.
- Turkish `i` plus acute still becomes `iacute` before the language feature runs, because HarfBuzz composes that pair first. Bare `i İ ı` does use the Turkish forms.

## 6. What was checked here, and what was not

Checked locally: fontTools outline identity for the 491 release characters, HarfBuzz shaping, FreeType rasters at 12, 14, 16, 20, 24, and 32 px, and the static and variable files this build wrote.

Not checked: a browser, a phone, a desktop app, a print, or a native reader. Those are in `documentation/HUMAN-REVIEW.md`.
