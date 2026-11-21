#!/usr/bin/env python3
"""Regenerate committed proof sheets under qa/proofs/."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
import uharfbuzz as hb

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "qa" / "proofs"
VF = ROOT / "fonts" / "variable" / "AkhilNotes[wght].ttf"
VF_IT = ROOT / "fonts" / "variable" / "AkhilNotes-Italic[wght].ttf"
REG = ROOT / "fonts" / "ttf" / "AkhilNotes-Regular.ttf"

OUT.mkdir(parents=True, exist_ok=True)

PARAGRAPH = (
    "The way I write, wherever I type. Notes gather commas, quotes, and the odd "
    "number 12 — with fi/fl ligatures when enabled, and handwriting kerning left alone."
)
MULTILINGUAL = [
    ("en", "The way I write, wherever I type."),
    ("fr", "Voilà : l'élève a déjà fini à Noël."),
    ("de", "Größe, Straße und süß — München."),
    ("vi", "Tiếng Việt: Nguyễn, Tưởng, Hoàng."),
    ("tr", "İstanbul'da iki iyi insan."),
    ("ca", "La col·lecció il·lustrada de l'illa."),
]
CONSTRUCTED = "ÆæŒœÐðÞþØøẞß§¶ ₦₩₪₫₹₺ ①✓✗"


def render(path: Path, text: str, px: int, features: dict[str, bool] | None = None) -> Image.Image:
    features = features or {"kern": True}
    data = path.read_bytes()
    face = hb.Face(data)
    font = hb.Font(face)
    upem = face.upem
    scale = int(px * 64)
    font.scale = (scale, scale)
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf, features)
    infos = buf.glyph_infos
    positions = buf.glyph_positions
    # Pillow FreeType path for raster
    try:
        pil = ImageFont.truetype(str(path), px)
    except Exception:
        pil = ImageFont.load_default()
    # Approximate canvas from advances
    width = max(1, sum(p.x_advance for p in positions) // 64 + px)
    height = int(px * 1.6)
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)
    draw.text((8, 8), text, font=pil, fill="black")
    return img


def stack(images: list[Image.Image], labels: list[str], gap: int = 12) -> Image.Image:
    w = max(i.width for i in images) + 160
    h = sum(i.height for i in images) + gap * (len(images) + 1) + 24 * len(images)
    out = Image.new("RGB", (w, h), "white")
    draw = ImageDraw.Draw(out)
    y = gap
    for label, im in zip(labels, images):
        draw.text((8, y), label, fill="black")
        out.paste(im, (150, y))
        y += im.height + gap + 16
    return out


def main() -> None:
    # Paragraph sizes 12–32
    sizes = [12, 14, 16, 18, 21, 24, 28, 32]
    stack(
        [render(REG, PARAGRAPH, s, {"kern": True}) for s in sizes],
        [f"{s}px kern on" for s in sizes],
    ).save(OUT / "paragraph-12-32-kern-on.png")
    stack(
        [render(REG, PARAGRAPH, s, {"kern": False}) for s in sizes],
        [f"{s}px kern off" for s in sizes],
    ).save(OUT / "paragraph-12-32-kern-off.png")

    # Weight ramp
    weights = [400, 500, 650, 700, 900]
    ramp_imgs, ramp_labels = [], []
    for w in weights:
        inst_path = OUT / f"_tmp-{w}.ttf"
        instantiateVariableFont(TTFont(VF), {"wght": w}, inplace=False).save(inst_path)
        ramp_imgs.append(render(inst_path, f"Weight {w} — packing notes.", 28))
        ramp_labels.append(f"wght={w}")
        inst_path.unlink(missing_ok=True)
    stack(ramp_imgs, ramp_labels).save(OUT / "weight-ramp.png")

    # Multilingual
    stack(
        [render(REG, text, 22) for _, text in MULTILINGUAL],
        [code for code, _ in MULTILINGUAL],
    ).save(OUT / "multilingual.png")

    # Constructed set
    render(REG, CONSTRUCTED, 40).save(OUT / "constructed-set.png")
    render(VF_IT, CONSTRUCTED, 40).save(OUT / "constructed-set-italic.png")

    print("wrote", sorted(p.name for p in OUT.glob("*.png")))


if __name__ == "__main__":
    main()
