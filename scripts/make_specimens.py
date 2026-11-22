#!/usr/bin/env python3
"""Generate technical specimen sheets from shipping binaries (Akhil Notes only).

Default output: ``output/generated-specimens/`` (gitignored).

Designer-authored presentation artwork lives in ``documentation/specimens/`` and
is never written by this script. Pass ``--output`` for a custom directory; paths
under ``documentation/specimens/`` are rejected.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "output" / "generated-specimens"
PROTECTED = (ROOT / "documentation" / "specimens").resolve()
VF = ROOT / "fonts" / "variable" / "AkhilNotes[wght].ttf"
VF_IT = ROOT / "fonts" / "variable" / "AkhilNotes-Italic[wght].ttf"
REG = ROOT / "fonts" / "ttf" / "AkhilNotes-Regular.ttf"

# Set in main() after resolving --output
OUT: Path
TMP: Path

BG = (252, 250, 247)
INK = (28, 26, 24)
MUTED = (110, 105, 98)

PARAGRAPH = (
    "I've always found that writing something by hand helps me understand and remember it better. "
    "There is something about the deliberate movement of a pen, the rhythm of forming letters, "
    "and the freedom of an imperfect page that makes thinking feel more personal. "
    "Akhil Notes keeps that rhythm when you type — imperfect in isolation, beautiful in context."
)
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ  abcdefghijklmnopqrstuvwxyz  0123456789"
EXTENDED = "ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ"
VIET = "Tiếng Việt: Nguyễn, Tưởng, Hoàng. Việt Nam Ắằặễộự."
MATH = "∑ ∫ √ ≈ ≠ ≤ ≥ ± × ÷ ½ ¾ ¹²³ ₀₁₂  ∴ ∵ ∞"
MONEY = "$12.50  £9.99  €40  ¥100  ₹500  ₫20  ₦5  ₩1000  ₪40  ₺25  ₿0.01"
UTILS = "→ ← ↑ ↓ ☑ ☐ ☒ ● ○ ■ □ ★ ☆ ✓ ✗ ¶ §"
FEATURES = "fi fl ct st th wh  1/2 3/4  0123456789"

EXPECTED = (
    "01-hero.png",
    "02-paragraph.png",
    "03-waterfall-sizes.png",
    "04-weight-ramp.png",
    "05-upright-italic.png",
    "06-character-coverage.png",
    "07-multilingual.png",
    "08-applications.png",
    "09-kern-liga.png",
    "10-interpolation.png",
)


def resolve_output(raw: str | None) -> Path:
    """Resolve output dir relative to repo root; reject designer specimen tree."""
    if raw is None:
        out = DEFAULT_OUT
    else:
        candidate = Path(raw)
        out = candidate if candidate.is_absolute() else (ROOT / candidate)
    out = out.resolve()
    try:
        out.relative_to(PROTECTED)
        blocked = True
    except ValueError:
        blocked = out == PROTECTED
    if blocked:
        raise SystemExit(
            f"Refusing to write into designer specimen directory: {PROTECTED}\n"
            f"Use the default ({DEFAULT_OUT.relative_to(ROOT)}) or another path outside "
            f"documentation/specimens/."
        )
    return out


def load_font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size)


def instance(weight: int, italic: bool = False) -> Path:
    src = VF_IT if italic else VF
    out = TMP / f"w{weight}{'-Italic' if italic else ''}.ttf"
    if not out.exists() or out.stat().st_mtime < src.stat().st_mtime:
        instantiateVariableFont(TTFont(str(src)), {"wght": weight}, inplace=False).save(str(out))
    return out


def measure(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0], box[3] - box[1]


def wrap(draw, text: str, font, max_width: int) -> list[str]:
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        tw, _ = measure(draw, trial, font)
        if tw > max_width and cur:
            lines.append(cur)
            cur = w
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines


def canvas(width: int, height: int) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    img = Image.new("RGB", (width, height), BG)
    return img, ImageDraw.Draw(img)


def save(img: Image.Image, name: str) -> Path:
    path = OUT / name
    img.save(path, optimize=True)
    try:
        rel = path.relative_to(ROOT)
    except ValueError:
        rel = path
    print("wrote", rel)
    return path


def sheet_hero() -> None:
    path = REG if REG.exists() else instance(400)
    img, draw = canvas(1400, 720)
    title = load_font(path, 92)
    tag = load_font(path, 36)
    meta = load_font(path, 22)
    draw.text((72, 120), "Akhil Notes", font=title, fill=INK)
    draw.text((72, 250), "The familiarity of handwriting.\nThe convenience of typing.", font=tag, fill=INK)
    draw.text((72, 400), "698 characters  ·  12 styles  ·  Open source", font=meta, fill=MUTED)
    draw.text((72, 480), "Imperfect in isolation. Beautiful in context.", font=tag, fill=INK)
    save(img, "01-hero.png")


def sheet_paragraph() -> None:
    path = REG if REG.exists() else instance(400)
    img, draw = canvas(1400, 900)
    h = load_font(path, 28)
    body = load_font(path, 32)
    draw.text((72, 48), "Imperfect in isolation. Beautiful in context.", font=h, fill=MUTED)
    y = 120
    for line in wrap(draw, PARAGRAPH, body, 1240):
        draw.text((72, y), line, font=body, fill=INK)
        y += 48
    save(img, "02-paragraph.png")


def sheet_waterfall() -> None:
    path = REG if REG.exists() else instance(400)
    sizes = [12, 14, 16, 20, 24, 32]
    rows = []
    width = 1400
    for s in sizes:
        font = load_font(path, s)
        probe = Image.new("RGB", (10, 10), BG)
        d = ImageDraw.Draw(probe)
        lines = wrap(d, f"{s}px — {PARAGRAPH}", font, 1240)
        row_h = max(40, int(s * 1.55) * len(lines) + 16)
        row = Image.new("RGB", (width, row_h), BG)
        rd = ImageDraw.Draw(row)
        y = 8
        for line in lines:
            rd.text((72, y), line, font=font, fill=INK)
            y += int(s * 1.55)
        rows.append(row)
    h = sum(r.height for r in rows) + 80
    img = Image.new("RGB", (width, h), BG)
    draw = ImageDraw.Draw(img)
    label = load_font(path, 22)
    draw.text((72, 24), "Paragraph sizes", font=label, fill=MUTED)
    y = 60
    for r in rows:
        img.paste(r, (0, y))
        y += r.height
    save(img, "03-waterfall-sizes.png")


def sheet_weights() -> None:
    img, draw = canvas(1400, 780)
    label = load_font(instance(400), 22)
    draw.text((72, 32), "Weight progression 400–900", font=label, fill=MUTED)
    y = 90
    sample = "Packing notes — weight {w}"
    for w in (400, 500, 650, 700, 900):
        font = load_font(instance(w), 40)
        draw.text((72, y), sample.format(w=w), font=font, fill=INK)
        y += 110
    save(img, "04-weight-ramp.png")


def sheet_italic() -> None:
    img, draw = canvas(1400, 520)
    up = load_font(instance(400), 36)
    it = load_font(instance(400, italic=True), 36)
    lab = load_font(instance(400), 22)
    draw.text((72, 40), "Upright and italic", font=lab, fill=MUTED)
    draw.text((72, 120), "The way I write, wherever I type.", font=up, fill=INK)
    draw.text((72, 220), "The way I write, wherever I type.", font=it, fill=INK)
    draw.text((72, 340), "fi fl ct st th wh  —  ligatures & joins", font=up, fill=INK)
    draw.text((72, 420), "fi fl ct st th wh  —  italic", font=it, fill=INK)
    save(img, "05-upright-italic.png")


def sheet_charset() -> None:
    path = REG if REG.exists() else instance(400)
    img, draw = canvas(1400, 980)
    h = load_font(path, 22)
    body = load_font(path, 28)
    y = 40
    blocks = [
        ("Alphabet & numerals", ALPHA),
        ("Latin extended", EXTENDED),
        ("Vietnamese", VIET),
        ("Math & fractions", MATH),
        ("Currencies", MONEY),
        ("Utility symbols", UTILS),
        ("Features (liga / dlig / frac / figures)", FEATURES),
    ]
    for title, text in blocks:
        draw.text((72, y), title, font=h, fill=MUTED)
        y += 36
        for line in wrap(draw, text, body, 1240):
            draw.text((72, y), line, font=body, fill=INK)
            y += 40
        y += 24
    save(img, "06-character-coverage.png")


def sheet_multilingual() -> None:
    path = REG if REG.exists() else instance(400)
    samples = [
        ("en", "The way I write, wherever I type."),
        ("fr", "Voilà : l'élève a déjà fini à Noël."),
        ("de", "Größe, Straße und süß — München."),
        ("vi", VIET),
        ("tr", "İstanbul'da iki iyi insan."),
        ("pl", "Zażółć gęślą jaźń."),
    ]
    img, draw = canvas(1400, 720)
    lab = load_font(path, 22)
    body = load_font(path, 30)
    draw.text((72, 32), "Multilingual Latin", font=lab, fill=MUTED)
    y = 90
    for code, text in samples:
        draw.text((72, y), code, font=lab, fill=MUTED)
        draw.text((160, y), text, font=body, fill=INK)
        y += 90
    save(img, "07-multilingual.png")


def sheet_applications() -> None:
    path = REG if REG.exists() else instance(400)
    apps = [
        ("Study notes", "Review: photosynthesis → light + CO₂ → sugar + O₂"),
        ("Journaling", "Tuesday — walked to the river. Clearer head afterward."),
        ("Annotations", "Move CTA left. Increase contrast on the secondary label."),
        ("Education", "If a² + b² = c², then the triangle is right-angled."),
        ("Planning", "☐ email  ☑ ship fonts  ☐ write README specimens"),
        ("Storytelling", "Once, a notebook became a typeface — and kept writing."),
    ]
    img, draw = canvas(1400, 860)
    h = load_font(path, 22)
    title = load_font(path, 28)
    body = load_font(path, 30)
    draw.text((72, 32), "One typeface. Many expressions.", font=h, fill=MUTED)
    y = 90
    for name, sample in apps:
        draw.text((72, y), name, font=title, fill=INK)
        draw.text((72, y + 40), sample, font=body, fill=INK)
        y += 120
    save(img, "08-applications.png")


def sheet_kern_liga() -> None:
    path = REG if REG.exists() else instance(400)
    img, draw = canvas(1400, 520)
    lab = load_font(path, 22)
    body = load_font(path, 36)
    draw.text((72, 40), "Kerning & joins (including wh)", font=lab, fill=MUTED)
    draw.text((72, 120), "wherever  ·  which  ·  when  ·  why", font=body, fill=INK)
    draw.text((72, 220), "To AV  ·  The way I write", font=body, fill=INK)
    draw.text((72, 320), "fi fl  ·  ct st th  ·  1/2 3/4", font=body, fill=INK)
    draw.text((72, 420), "Tabular: 0123456789    Default: 0123456789", font=body, fill=INK)
    save(img, "09-kern-liga.png")


def sheet_interp() -> None:
    img, draw = canvas(1400, 640)
    lab = load_font(instance(400), 22)
    draw.text((72, 32), "Intermediate weights (interpolation check)", font=lab, fill=MUTED)
    y = 100
    sample = "Hamburgfonts — Dperiod"
    for w in (400, 500, 650, 700, 900):
        font = load_font(instance(w), 42)
        draw.text((72, y), f"{w}  {sample}", font=font, fill=INK)
        y += 100
    save(img, "10-interpolation.png")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=(
            "Generate technical Akhil Notes specimen PNGs. "
            "Does not write to documentation/specimens/ (designer artwork)."
        )
    )
    p.add_argument(
        "--output",
        metavar="DIR",
        help=(
            f"Output directory for generated PNGs "
            f"(default: {DEFAULT_OUT.relative_to(ROOT).as_posix()}). "
            "Must not be documentation/specimens/ or a path inside it."
        ),
    )
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    global OUT, TMP
    args = parse_args(argv)
    OUT = resolve_output(args.output)
    TMP = OUT / "_tmp"
    OUT.mkdir(parents=True, exist_ok=True)
    TMP.mkdir(parents=True, exist_ok=True)

    if not VF.exists():
        raise SystemExit(
            f"Missing {VF.relative_to(ROOT)}; run scripts/build_candidate.py --from-ufo first"
        )

    sheet_hero()
    sheet_paragraph()
    sheet_waterfall()
    sheet_weights()
    sheet_italic()
    sheet_charset()
    sheet_multilingual()
    sheet_applications()
    sheet_kern_liga()
    sheet_interp()

    written = sorted(p.name for p in OUT.glob("*.png"))
    missing = [n for n in EXPECTED if n not in written]
    if missing:
        raise SystemExit(f"Missing generated specimens: {missing}")
    print(f"specimens complete: {len(EXPECTED)} → {OUT}")


if __name__ == "__main__":
    main()
