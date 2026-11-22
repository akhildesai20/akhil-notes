# Compliance

Candidate **2.101**. Not a Google Fonts acceptance. Counts and WARN policy:
[`RELEASE-STATUS.md`](RELEASE-STATUS.md), [`FONTSPECTOR-EXCEPTIONS.md`](FONTSPECTOR-EXCEPTIONS.md).

## Pins

- GF guide commit `355e4599ae45a8a05a42a57e8c5bbf79c821a4a5` (2026-11-18)
- Glyphsets 1.1.3 / `1dbbd54ea7bf3a3e94422c746be4da2741379d0b` — Core, Plus, Vietnamese
- Fontspector `v1.9.1` (CLI may print `1.9.0`)

Public build does **not** need `provenance/`. Maintainer regenerate from private
TTF uses SHA in `reference/input-sha256.txt`.

## Packaging

- License: SIL OFL 1.1 (`OFL.txt`); Reserved Font Name **Akhil Notes**
- Copyright: The Akhil Notes Project Authors
  (https://github.com/akhildesai20/akhil-notes)
- Designer / manufacturer (name IDs 8–10): **Akhil Desai**
- Vendor ID `AKHL`: registration requested; confirmation pending
- Vertical metrics: typo 976 / −530; Use Typo Metrics on
- Local GF-style tree: `ofl/akhilnotes/`

## Attribution

Akhil Desai is the designer and copyright holder of the handwriting and typeface.
Cursor (and similar tools) may appear in Git commit trailers as a development
assistant; they are **not** font designers or copyright holders. Do not list
Cursor in `AUTHORS.txt`, `CONTRIBUTORS.txt`, or name-table designer fields.
Historical `Co-authored-by: Cursor` trailers are left intact (no history rewrite).

## Documentation map

| Audience | File |
| --- | --- |
| Public introduction | [`../README.md`](../README.md) |
| Design story | [`ABOUT.md`](ABOUT.md) |
| GF catalog blurb | [`DESCRIPTION.en_us.html`](DESCRIPTION.en_us.html) |
| Build / release status | [`RELEASE-STATUS.md`](RELEASE-STATUS.md) |
| Fontspector WARN policy | [`FONTSPECTOR-EXCEPTIONS.md`](FONTSPECTOR-EXCEPTIONS.md) |
| Submission draft | [`GF-SUBMISSION.md`](GF-SUBMISSION.md) |
| Human optical checklist | [`HUMAN-REVIEW.md`](HUMAN-REVIEW.md) |
| Constructed-glyph review | [`DESIGN-ISSUES.md`](DESIGN-ISSUES.md) |
| Licensing log | [`../FONTLOG.txt`](../FONTLOG.txt), [`../OFL.txt`](../OFL.txt) |
| Presentation images | [`specimens/`](specimens/) |
| Technical proofs | [`proofs/`](proofs/) |
