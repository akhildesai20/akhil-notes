# GF submission preparation — deliverables

Date: 2026-11-22. **Local only — not pushed, not released, not submitted.**

## Positioning (locked copy)

- Core: *The familiarity of handwriting. The convenience of typing.*  
- Philosophy: *Imperfect in isolation. Beautiful in context.*  
- Open source: *Written by hand. Made for everyone.*  
- Long form: [`ABOUT.md`](ABOUT.md)  
- GF blurb: [`GF-DESCRIPTION.md`](GF-DESCRIPTION.md) / `DESCRIPTION.en_us.html`  
- PR/issue draft: [`GF-SUBMISSION.md`](GF-SUBMISSION.md)  

## Technical

| Item | Decision / result |
| --- | --- |
| `ellipsis` / `registered` interpolation | Order-only start fixes (already landed); no redesign |
| Identity `avar` | **Not added** — linear `wght`; GF/Fontspector allow ignoring missing avar |
| Overlap bits | Hotfix after `ensure_fontspector` |
| Fontspector | **FAIL 0**, WARN 18 — [`FONTSPECTOR-EXCEPTIONS.md`](FONTSPECTOR-EXCEPTIONS.md) |
| Counts | 698 encoded / 846 glyphs / 12 statics / VF pair |

## Specimens generated (actual binaries)

Under `documentation/specimens/` (also mirrored where useful into `qa/proofs/`):

01 hero · 02 paragraph · 03 waterfall sizes · 04 weight ramp · 05 upright/italic · 06 coverage · 07 multilingual · 08 applications · 09 kern/liga · 10 interpolation · 11 constructed  

No fabricated notebook photographs (section omitted until you provide them).

## README

Specimen-led README with narrative, downloads, badges, install, build, QA pointers.

## Retained / removed / generated (this pass)

**Generated:** specimen PNGs, refreshed ofl DESCRIPTION/FONTLOG copies, QA hashes as applicable.  
**Updated docs:** ABOUT, GF-DESCRIPTION, GF-SUBMISSION, RELEASE-STATUS, HUMAN-REVIEW, FONTSPECTOR-EXCEPTIONS, FONTLOG, DESCRIPTION.en_us.html, README.  
**Not deleted:** UFO masters, designspace, features, build scripts, OFL, provenance checksum reference.  

## Validation

- `--from-ufo` build · `audit_final` · `qa_features` · Fontspector FAIL 0  

## Left for you

Optical approval · devices · vendor listing · CLA · **approval to push / release / open GF PR**  
