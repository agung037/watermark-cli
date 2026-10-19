#!/usr/bin/env python3
"""Add a text watermark to the bottom-right corner of an image."""
import argparse

from PIL import Image, ImageDraw, ImageFont


def add_watermark(image_path, text, output, opacity=128):
    base = Image.open(image_path).convert("RGBA")
    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    size = max(12, base.size[1] // 20)
    font = ImageFont.load_default(size=size)
    m = size // 2
    draw.text(
        (base.size[0] - m, base.size[1] - m),
        text,
        font=font,
        fill=(255, 255, 255, opacity),
        anchor="rb",
    )
    Image.alpha_composite(base, overlay).convert("RGB").save(output)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("image", help="input image")
    p.add_argument("text", help="watermark text")
    p.add_argument("-o", "--output", help="output path (default: watermarked_<image>)")
    p.add_argument("--opacity", type=int, default=128, help="text opacity 0-255 (default 128)")
    a = p.parse_args()
    add_watermark(a.image, a.text, a.output or f"watermarked_{a.image}", a.opacity)


if __name__ == "__main__":
    main()
