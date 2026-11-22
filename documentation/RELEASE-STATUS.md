# Akhil Notes — release status

Authoritative numbers for the public repository after a **successful** CI run.

Warn policy: [`FONTSPECTOR-EXCEPTIONS.md`](FONTSPECTOR-EXCEPTIONS.md)  
Positioning: [`ABOUT.md`](ABOUT.md)  
**Not submitted to Google Fonts. Optical sign-off remains human.**

## Public presence

| Item | Value |
| --- | --- |
| Repository | https://github.com/akhildesai20/akhil-notes |
| `main` HEAD (CI green) | `6684d60` |
| CI run | https://github.com/akhildesai20/akhil-notes/actions/runs/45001242763 (**success**) |
| Prior green | https://github.com/akhildesai20/akhil-notes/actions/runs/45000874359 |
| Release | [v2.101](https://github.com/akhildesai20/akhil-notes/releases/tag/v2.101) |
| Package | `ofl/akhilnotes/` |
| Specimens (canonical) | `documentation/specimens/` |

## Inventory (shipping binaries)

| Metric | Count |
| --- | --- |
| Original release codepoints | 491 (outline-faithful except 38 intentional figure rebuilds) |
| Encoded Unicode | **698** |
| Glyphs | **846** |
| Static styles | **12** |
| Variable fonts | Upright + italic `wght` 400–900 |

## Build

- Public: `python scripts/build_candidate.py --from-ufo`  
- Fontspector: `scripts/ensure_fontspector.py` exports `GITHUB_PATH` + `FONTSPECTOR_BIN` for later CI steps  
- Statics: GitHub Releases / CI artifacts  
- Specimens: `documentation/specimens/` only (no duplicate mirror in `qa/proofs/`)  

## Fontspector (CI VF pair)

From run `45000874359` / `qa/fontspector/googlefonts.json`:

```
SKIP 95  INFO 22  PASS 247  WARN 18  FAIL 0  FATAL 0  ERROR 0
```

All 18 WARN subresults are listed in [`FONTSPECTOR-EXCEPTIONS.md`](FONTSPECTOR-EXCEPTIONS.md) as either intentional handwriting characteristics or accepted technical limitations (including family-level `unreachable_subsetting`).

## Automated QA (same CI run)

| Check | Result |
| --- | --- |
| Ensure Fontspector | Pass |
| UFO compile + package | Pass |
| OTS + instantiate + parity | Pass |
| HarfBuzz features | Pass |
| Fontspector googlefonts | Pass (FAIL 0; WARN 18 ≤ ceiling) |
| Artifacts | statics, ofl package, fontspector reports |

## Metadata / hashes

- `ofl/akhilnotes/METADATA.pb` `source.commit` → content commit `0a693d9…` (maintenance); tip `f9bd81f` syncs hashes pointer.  
- `qa/candidate/hashes.json` refreshed from CI artifact / local write.  
- Release v2.101 ships statics + ofl + webfonts; rebuild ofl from `main` matches CI artifact `akhil-notes-ofl`.

## Human remaining

- [ ] Optical review ([`OPTICAL-REVIEW.md`](OPTICAL-REVIEW.md))  
- [ ] Device matrix  
- [ ] Vendor ID — registration requested; confirmation pending  
- [ ] Contributor agreement / GF onboarding  
- [ ] Approval to open a google/fonts PR ([`GF-SUBMISSION.md`](GF-SUBMISSION.md))  
