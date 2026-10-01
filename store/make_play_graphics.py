"""The two pictures Google Play wants besides the screenshots.

    python store/make_play_graphics.py

store/play/icon-512.png          App icon, 512 x 512 (Play rounds the corners itself)
store/play/feature-en.png        Feature graphic, 1024 x 500, English
store/play/feature-de.png        Feature graphic, 1024 x 500, German

Both are made from resources/icon-only.png, so they stay in step with the app icon.
The title font is resources/FrankRuhlLibre-500.ttf (not in git; see .gitignore).
"""
import pathlib
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parents[1]
ICON = ROOT / "resources/icon-only.png"
FONT = ROOT / "resources/FrankRuhlLibre-500.ttf"
OUT = ROOT / "store/play"

GREEN = (30, 61, 53)      # the icon's background, #1E3D35
PAPER = (244, 246, 242)   # #F4F6F2
MUTED = (184, 204, 194)

TEXT = {
    "en": ("Faithful parents", "Like a Father · As a Mother Comforts", "Two 31-day devotionals"),
    "de": ("Faithful parents", "Wie ein Vater · Wie eine Mutter tröstet", "Zwei Andachtsbücher, je 31 Tage"),
}


def fit(draw, text, size, width):
    """The largest font no bigger than `size` that fits `text` into `width`."""
    while size > 10:
        font = ImageFont.truetype(str(FONT), size)
        if draw.textlength(text, font=font) <= width:
            return font
        size -= 1
    return ImageFont.truetype(str(FONT), size)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    icon = Image.open(ICON).convert("RGB")
    icon.resize((512, 512), Image.LANCZOS).save(OUT / "icon-512.png")
    print("OK", OUT / "icon-512.png")

    # The aleph with its two dots, cut from the icon, on the left third.
    mark = icon.crop((232, 120, 792, 930)).resize((280, 405), Image.LANCZOS)
    for lang, (title, books, tag) in TEXT.items():
        img = Image.new("RGB", (1024, 500), GREEN)
        img.paste(mark, (70, 48))
        d = ImageDraw.Draw(img)
        left, width = 400, 1024 - 400 - 56
        f1 = fit(d, title, 76, width)
        f2 = fit(d, books, 34, width)
        f3 = fit(d, tag, 30, width)
        d.text((left, 150), title, font=f1, fill=PAPER)
        d.text((left, 262), books, font=f2, fill=PAPER)
        d.text((left, 318), tag, font=f3, fill=MUTED)
        dest = OUT / f"feature-{lang}.png"
        img.save(dest)
        print("OK", dest, img.size)


if __name__ == "__main__":
    main()
