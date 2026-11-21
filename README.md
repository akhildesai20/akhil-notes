# Akhil Notes

Akhil Notes is a handwriting typeface by Akhil Desai for everyday notes and digital writing. Weight runs from Regular (400) to Black (900), with a matching italic.

## License

SIL Open Font License 1.1. See [OFL.txt](OFL.txt).

“Akhil Notes” is a Reserved Font Name.

## Build

Requires the private release font at `provenance/AkhilsNotes-Variable.ttf` (SHA-256 in `reference/input-sha256.txt`).

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
$env:PYTHONUTF8 = "1"
.\.venv\Scripts\python.exe scripts\build_candidate.py
```

Outputs:

- `fonts/variable/AkhilNotes[wght].ttf`
- `fonts/variable/AkhilNotes-Italic[wght].ttf`
- `fonts/ttf/AkhilNotes-*.ttf`
- `ofl/akhilnotes/` (Google Fonts-style package)

## Repository layout

| Path | Contents |
| --- | --- |
| `sources/` | UFO masters, designspace, features |
| `fonts/` | Compiled variable and static fonts |
| `ofl/akhilnotes/` | Files for a google/fonts `ofl/akhilnotes` PR |
| `scripts/` | Build and QA scripts |
| `documentation/` | Design notes and compliance |
| `qa/` | Shaping and Fontspector reports |

## Links

- Designer: [Akhil Desai](https://www.instagram.com/akhilius_)
- Source: https://github.com/akhildesai20/akhil-notes
