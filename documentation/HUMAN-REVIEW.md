# Review checklist

## Install

- [x] Static and variable fonts install and show Regular–Black, upright and italic.

## Reading

- [x] Reading sizes, kerning, multilingual samples, fractions, and ligatures checked.

## Design

- [x] Digraphs, barred letters, currencies, and long s built from the handwritten stems.
- [ ] Optical review of constructed set / stroke weight — [`OPTICAL-REVIEW.md`](OPTICAL-REVIEW.md) (no geometric cleanup).
- [ ] Optional: raise typo ascender if Black Â (y≈1139) collides with the line above.
- [ ] Optional: stylistic alternates only from real handwriting samples (not rotations).

## Technical readiness

- [x] Public UFO-only build (`--from-ufo`); see [`RELEASE-STATUS.md`](RELEASE-STATUS.md).
- [x] Interpolation start points fixed (order-only); Fontspector FAIL 0.
- [ ] Device matrix (Figma / browser / OS) on the shipping VF pair.

## License and packaging

- [x] OFL 1.1; reserved name Akhil Notes.
- [x] Public repository: https://github.com/akhildesai20/akhil-notes
- [x] `ofl/akhilnotes/` package ready.
- [ ] Vendor ID `AKHL` registration with Microsoft (email sent; listing pending).
- [ ] Pull request to google/fonts.
