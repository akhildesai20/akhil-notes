# Google Fonts submission — Akhil Notes

**Status:** RFN removed. Ready to file the Add Font issue after designer approval of the issue text below.  
**CLA:** Designer will complete separately — **not claimed signed here.**  
**PR:** Do not open until GF issue triage requests it.

Issue creation link:  
https://github.com/google/fonts/issues/new?template=1_add-font.md

No existing `Akhil Notes` issue on `google/fonts` (search `total_count: 0`).

---

## Licensing (Option A complete)

- SIL OFL 1.1 body unchanged  
- Copyright unchanged: The Akhil Notes Project Authors  
- Family name unchanged: **Akhil Notes**  
- Designer attribution unchanged: **Akhil Desai**  
- Reserved Font Name declaration **removed** from `OFL.txt`, `ofl/akhilnotes/OFL.txt`, docs, and name-table trademark (name ID 7)  

---

## Verified (post-RFN rebuild)

| Item | Result |
| --- | --- |
| Public UFO build | Pass |
| OTS / parity | Pass |
| HarfBuzz | 11/11 Pass |
| Fontspector googlefonts | FAIL 0 · WARN 18 |
| Chars / glyphs | 698 / 846 |
| Name ID 7 / RFN strings in fonts | Absent |
| Package | `ofl/akhilnotes/` |

WARN policy: [`FONTSPECTOR-EXCEPTIONS.md`](FONTSPECTOR-EXCEPTIONS.md).

Release **v2.101** left intact (published assets still reflect pre-RFN packaging). GF will take fonts from the upstream git commit at PR time.

---

## Final GitHub issue (awaiting publish approval)

**Title:** `Add Akhil Notes`

**Body:**

```markdown
**Font Project Git Repo URL:**

https://github.com/akhildesai20/akhil-notes

**Super short description of the Font Family:**

Akhil Notes is a handwriting family drawn from designer Akhil Desai’s own notebook letterforms. It keeps natural irregularities on purpose so typed text can keep the familiarity of handwriting for notes, education, annotations, journaling and everyday writing. Open-source OFL; variable weight 400–900 with matching italics; Latin Core, Latin Plus and Vietnamese plus math, currency and utility symbols.

**Requirements:**

By opening this issue, I confirm the project meets the following requirements:

- [x] The entire font project is available in a Github repository (repo) and licensed under the [OFL](https://openfontlicense.org/open-font-license-official-text/)
- [x] I confirm that by 'entire font project', no "plus" or "pro" or other larger version of the project exists as a retail font anywhere
- [x] The source files are available in the repo
- [x] I am the sole copyright author of the entire project, or all other copyright authors have licensed their work to me under the OFL, and I commit to clearly disclosing if AI tools were used in the creation of this project.
- [x] There are no "Reserved Font Names" in the OFL license information, or in the project documentation of any known upstream projects. If there are RFNs, they are not used in whole or in part in this family name, or, I want to discuss how Google can work with my use of them.
- [x] The family name is unique according to [namecheck.fontdata.com](https://namecheck.fontdata.com/)
- [x] The name of the font family expected to appear on app menus must be very clearly communicated and definitive. It should not include any copyright holder's full names or acronyms.
- [x] The font supports at least the Google Fonts 'Latin Core' glyphset from [github.com/googlefonts/glyphsets](https://github.com/googlefonts/glyphsets) ([direct link](https://github.com/googlefonts/glyphsets/blob/main/data/results/txt/nice-names/GF_Latin_Core.txt))
- [x] The repo has the [Google Fonts preferred upstream repo structure](https://googlefonts.github.io/gf-guide/upstream.html)
- [x] I have read, agree with, and comply with, the full [Google Fonts contributing requirements](https://googlefonts.github.io/gf-guide/index#pre-production-getting-your-fonts-ready-for-gf)
- [x] I will maintain the repository and participate in the onboarding process (addressing, solving, and responding to issues, merging pull requests, etc)

**App menu / catalog family name:** Akhil Notes

**Additional notes for reviewers:**

- Designer: Akhil Desai. Classification: Handwriting.
- Positioning: “The familiarity of handwriting. The convenience of typing.” / “Imperfect in isolation. Beautiful in context.” / “Written by hand. Made for everyone.”
- Styles: 12 static instances; VF pair `AkhilNotes[wght].ttf` + `AkhilNotes-Italic[wght].ttf`, axis `wght` 400–900. Version 2.101.
- Coverage: 698 encoded characters / 846 glyphs; GF Latin Core, Latin Plus, Vietnamese; math, currency, utility symbols.
- Features: kerning, liga/dlig (including wh joins), mark/mkmk, locl, frac, tnum.
- Public build: `python scripts/build_candidate.py --from-ufo` (committed UFOs; no private provenance required).
- Fontspector googlefonts on shipping VF pair: FAIL 0; WARN 18 documented in `documentation/FONTSPECTOR-EXCEPTIONS.md` (intentional handwriting outlines + linear axis without avar; vendor ID `AKHL` registration pending).
- Release: https://github.com/akhildesai20/akhil-notes/releases/tag/v2.101
- Local GF-style tree: `ofl/akhilnotes/`
- OFL has no Reserved Font Name. Copyright remains with The Akhil Notes Project Authors.
- AI tools (including Cursor) assisted with engineering and documentation; they are not designers or copyright holders. Original handwriting and typeface design are by Akhil Desai.
- Google CLA will be completed by the copyright holder via https://cla.developers.google.com

**Image:**

Attach `documentation/specimens/01-hero.png` when filing.
```

---

## Later PR (not now)

Title: `Akhil Notes: added`  
Body: `Taken from the upstream repo https://github.com/akhildesai20/akhil-notes at commit <SHA>.` + link to this issue.
