# Compliance

Local engineering report for candidate **2.101**. Not a Google Fonts acceptance. Public git URL is still the last packaging step before a PR.

Pins, fetched 2026-11-21:

- Guide: https://googlefonts.github.io/gf-guide/ from `googlefonts/googlefonts.github.io`, path `gf-guide`, commit `355e4599ae45a8a05a42a57e8c5bbf79c821a4a5` (2026-11-18).
- Glyphsets 1.1.3, commit `1dbbd54ea7bf3a3e94422c746be4da2741379d0b`. Sets: GF_Latin_Core, GF_Latin_Plus, GF_Latin_Vietnamese.
- Fontspector release asset `fontspector-v1.9.1`, zip SHA-256 `482891cd94d6cb16918552ee4c832b51743d6abc687249340d96e60010e49370`. `--version` prints `fontspector 1.9.0` and `fontspector-v1.9.1`, commit `990bb930`.

The source file `provenance/AkhilsNotes-Variable.ttf` matches `reference/input-sha256.txt` (`4778875b3c7debd3d1f6d9713a621674053dd5aced0ada6817e9796d3b760aa8`).

## Candidate

OFL 1.1 in name IDs 13/14. Copyright: `Copyright 2026 The Akhil Notes Project Authors (https://www.instagram.com/akhilius_)` until `REPO_URL` is set. Typo metrics 976 / −530, line gap 0, win 1140 / 523. Use Typo Metrics and WWS bits on. `meta` declares `Latn`. Local package: `ofl/akhilnotes/` (variable pair + OFL + METADATA.pb + DESCRIPTION + FONTLOG).

## Fontspector (ofl/akhilnotes variable pair)

Command in `qa/fontspector/command.txt`.

```
SKIP 95  INFO 22  PASS 243  WARN 649  FAIL 0  FATAL 0  ERROR 0
```

Process exits 0. Full output: `qa/fontspector/googlefonts.json` and `qa/fontspector/googlefonts.md`.

### FAIL

None on the packaged variable pair.

### WARN (left open on purpose)

| Check | Decision |
| --- | --- |
| Outline jaggy / overlap / direction / semi-vertical | Handwriting + constructed additions. Not smoothed. |
| `contour_count` | Constructed symbols; see `DESIGN-ISSUES.md`. |
| Overlaps bit mismatches | Some composites set OVERLAP_COMPOUND; release outlines left alone. |
| `googlefonts/vertical_metrics` | hhea sum 1.506× UPM (dot below on ỵ). Not shrunk. |
| `googlefonts/vendor_id` | `AKHL` unregistered. Register with Microsoft or leave. |
| `googlefonts/glyphsets/shape_languages` | Auxiliaries outside Core/Plus/Vietnamese not drawn. |
| Math widths uneven | Handwriting math, not mono. |
| `unreachable_subsetting` | Spacing accents; subsets declared in METADATA.pb. |

## License

OFL 1.1 adopted. Reserved name: Akhil Notes. Replace the Instagram stand-in with the public git URL before opening a google/fonts PR (`scripts/build_candidate.py` → `REPO_URL`).

## Still for a person

Install, reading sizes, and redraw of high-priority provisional glyphs — `documentation/HUMAN-REVIEW.md` and `DESIGN-ISSUES.md`.
