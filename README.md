# Akhil Notes

Akhil Notes is a handwriting typeface by Akhil Desai for everyday notes and digital writing. Weight runs from Regular (400) to Black (900), with a matching italic.

## License

SIL Open Font License 1.1. See [OFL.txt](OFL.txt).

“Akhil Notes” is a Reserved Font Name.

## Build

Public / CI build compiles the committed UFO masters. No private fonts are required.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
$env:PYTHONUTF8 = "1"
.\.venv\Scripts\python.exe scripts\build_candidate.py
# same as: scripts\build_candidate.py --from-ufo
```

Or: `sources/build.ps1` / `sources/build.sh`.

Outputs:

- `fonts/variable/AkhilNotes[wght].ttf`
- `fonts/variable/AkhilNotes-Italic[wght].ttf`
- `fonts/ttf/AkhilNotes-*.ttf`
- `fonts/webfonts/*.woff2`
- `ofl/akhilnotes/` (Google Fonts-style package)

### Maintainer regenerate (optional)

Rebuilds UFO masters from the private provenance TTF (SHA-256 in `reference/input-sha256.txt`), then compiles. Not used in CI.

```powershell
.\.venv\Scripts\python.exe scripts\build_candidate.py --from-provenance
```

## Repository layout

| Path | Contents |
| --- | --- |
| `sources/` | UFO masters, designspace, features |
| `fonts/` | Compiled variable and static fonts |
| `ofl/akhilnotes/` | Files for a google/fonts `ofl/akhilnotes` PR |
| `scripts/` | Build and QA scripts |
| `documentation/` | Design notes, compliance, release status |
| `qa/` | Shaping, proofs, and Fontspector reports |

## Links

- Designer: [Akhil Desai](https://www.instagram.com/akhilius_)
- Source: https://github.com/akhildesai20/akhil-notes
- Specimens: open `playground/index.html` locally after building
