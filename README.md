# Akhil Notes

[![Build](https://github.com/akhildesai20/akhil-notes/actions/workflows/build.yml/badge.svg)](https://github.com/akhildesai20/akhil-notes/actions/workflows/build.yml)

Akhil Notes is a handwriting typeface by [Akhil Desai](https://www.instagram.com/akhilius_) for everyday notes and digital writing. Weight runs from Regular (400) to Black (900), with a matching italic. Natural irregularities in the outlines are intentional.

## Specimens

Representative FreeType proofs (after build, or browse the committed sheets):

| | |
| --- | --- |
| [Paragraph (kern on)](qa/proofs/paragraph-12-32-kern-on.png) | [Weight ramp](qa/proofs/weight-ramp.png) |
| [Multilingual](qa/proofs/multilingual.png) | [Constructed set](qa/proofs/constructed-set.png) |
| [Waterfall](qa/proofs/waterfall-regular.png) | [Ligatures](qa/proofs/ligatures-Regular.png) |

More sheets under [`qa/proofs/`](qa/proofs/). Status and warn policy: [`documentation/RELEASE-STATUS.md`](documentation/RELEASE-STATUS.md).

## Install

1. Download a release from [GitHub Releases](https://github.com/akhildesai20/akhil-notes/releases) (static TTFs), **or** build from source (below).
2. Windows: select the `.ttf` files → right-click → **Install**.  
   macOS: double-click → **Install Font**.  
   Linux: copy into `~/.local/share/fonts/` and run `fc-cache -f`.

Variable fonts for apps that support `wght`: use the pair in [`ofl/akhilnotes/`](ofl/akhilnotes/) after a build or from the release assets.

## Download

- **Source:** https://github.com/akhildesai20/akhil-notes  
- **Releases (statics / packaged builds):** https://github.com/akhildesai20/akhil-notes/releases  
- **Designer:** [Instagram @akhilius_](https://www.instagram.com/akhilius_)

## License

SIL Open Font License 1.1. See [OFL.txt](OFL.txt).

“Akhil Notes” is a Reserved Font Name.

## Build

Public / CI build compiles the **committed UFO masters**. No private fonts are required.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
$env:PYTHONUTF8 = "1"
.\.venv\Scripts\python.exe scripts\build_candidate.py --from-ufo
```

Or: `sources/build.ps1` / `sources/build.sh`.

The build ensures [Fontspector](https://github.com/fonttools/fontspector) is present (downloads under `tools/` if needed) before the overlap-flag hotfix.

Outputs:

| Path | Role |
| --- | --- |
| `ofl/akhilnotes/*.ttf` | Shipping variable pair (tracked; GF-style package) |
| `fonts/ttf/*.ttf` | Static instances (local / Releases; not git-tracked) |
| `fonts/variable/*.ttf` | Local VF copy used by packaging |
| `fonts/webfonts/*.woff2` | Local webfonts |

Automated QA: `scripts/audit_final.py`, `scripts/qa_features.py`. Full warn exceptions: [`documentation/FONTSPECTOR-EXCEPTIONS.md`](documentation/FONTSPECTOR-EXCEPTIONS.md).

### Maintainer regenerate (optional)

```powershell
.\.venv\Scripts\python.exe scripts\build_candidate.py --from-provenance
```

Requires `provenance/AkhilsNotes-Variable.ttf` matching `reference/input-sha256.txt`. Not used in CI.

## Repository layout

| Path | Contents |
| --- | --- |
| `sources/` | UFO masters, designspace, features |
| `ofl/akhilnotes/` | Google Fonts-style package (VF + metadata + OFL) |
| `scripts/` | Build and QA |
| `documentation/` | Status, compliance, review checklists |
| `qa/proofs/` | Representative specimen images |

## Links

- Designer: [Akhil Desai](https://www.instagram.com/akhilius_)  
- Source: https://github.com/akhildesai20/akhil-notes  
