# Compliance

Local engineering report for candidate **2.101**. Not a Google Fonts acceptance. See also [`RELEASE-STATUS.md`](RELEASE-STATUS.md) for authoritative counts and Fontspector summary.

Pins, fetched 2026-11-21:

- Guide: https://googlefonts.github.io/gf-guide/ from `googlefonts/googlefonts.github.io`, path `gf-guide`, commit `355e4599ae45a8a05a42a57e8c5bbf79c821a4a5` (2026-11-18).
- Glyphsets 1.1.3, commit `1dbbd54ea7bf3a3e94422c746be4da2741379d0b`. Sets: GF_Latin_Core, GF_Latin_Plus, GF_Latin_Vietnamese.
- Fontspector release asset `fontspector-v1.9.1`, zip SHA-256 `482891cd94d6cb16918552ee4c832b51743d6abc687249340d96e60010e49370`. `--version` prints `fontspector 1.9.0` and `fontspector-v1.9.1`, commit `990bb930`.

Public build does **not** require `provenance/`. Maintainer regenerate uses `provenance/AkhilsNotes-Variable.ttf` matching `reference/input-sha256.txt` (`4778875b3c7debd3d1f6d9713a621674053dd5aced0ada6817e9796d3b760aa8`).

## Candidate

OFL 1.1 in name IDs 13/14. Copyright: `Copyright 2026 The Akhil Notes Project Authors (https://github.com/akhildesai20/akhil-notes)`. Typo metrics 976 / −530, line gap 0, win 1140 / 523. Use Typo Metrics and WWS bits on. `meta` declares `Latn`. Local package: `ofl/akhilnotes/` (variable pair + OFL + METADATA.pb + DESCRIPTION + FONTLOG).

Glyph counts: **491** original codepoints (outline-faithful except **38** intentional `REBUILD_FIGURES`), **698** encoded, **846** glyphs. The old “38 drift” QA label was those figure rebuilds, not a regression (`qa/candidate/qa.json` → `intentional_figure_rebuilds`).

## Fontspector (ofl/akhilnotes variable pair)

Command in `qa/fontspector/command.txt`.

```
SKIP 95  INFO 22  PASS 244  WARN 23  FAIL 0  FATAL 0  ERROR 0
```

Process exits 0. Full output: `qa/fontspector/googlefonts.json` and `qa/fontspector/googlefonts.md`.

### FAIL

None on the packaged variable pair.

### WARN (left open on purpose)

| Check | Decision |
| --- | --- |
| `interpolation_issues` | Most start-point WARNs fixed via order-only contour rotate/reverse on Black masters. Residual few kept under watch; no geometric cleanup. |
| Outline direction / overlapping path segments (handwriting) | Intentional irregularity. Constructed `.notdef` / `paragraph` segments noted; no mass remove-overlap. |
| `contour_count` | Constructed symbols; see `DESIGN-ISSUES.md`. |
| Overlaps bit | Synced from Fontspector lists + build hotfix; a couple edge glyphs may still WARN depending on detector vs flag. |
| `googlefonts/vertical_metrics` | hhea sum ~1.506× UPM (dot below). Not shrunk. |
| `googlefonts/vendor_id` | `AKHL` unregistered. Register with Microsoft or leave. |
| `googlefonts/glyphsets/shape_languages` | Auxiliaries outside Core/Plus/Vietnamese not drawn. |
| Math widths uneven | Handwriting math, not mono. |
| `mandatory_avar_table` | No avar; linear wght map is acceptable for this design. |

Stale jaggy / semi-vertical “must fix for VF” claims from earlier static audits do not apply as FAILs on the current VF pair.

## License

OFL 1.1 adopted. Reserved name: Akhil Notes. Public git URL is set in packaging.

## Still for a person

Install, reading sizes, optical review of constructed glyphs — `documentation/HUMAN-REVIEW.md`, `DESIGN-ISSUES.md`, and `RELEASE-STATUS.md`.
