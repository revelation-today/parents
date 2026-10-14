"""The app icon: the Hebrew words ab (father) and em (mother), one above the other.

    python store/make_app_icons.py

Writes   resources/icon-only.png, splash.png, splash-dark.png, android/ic_stat_aleph.png
         web/icons/*.png
and then run  python store/make_play_graphics.py  for the Play icon and feature graphics.
The font is resources/FrankRuhlLibre-500.ttf (not in git; see .gitignore).
"""
import pathlib
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parents[1]
FONT = ROOT / "resources/FrankRuhlLibre-500.ttf"

GREEN = (30, 61, 53)        # #1E3D35, the icon's background
FATHER = (125, 187, 166)    # the green dot of the old icon
MOTHER = (226, 149, 168)    # the pink dot of the old icon
PAPER = (244, 246, 242)     # #F4F6F2
DARK = (16, 21, 20)

# Hebrew reads right to left, so each word is listed from its first letter.
ROWS = [("אב", FATHER),   # אב  ab, father
        ("אם", MOTHER)]   # אם  em, mother (mem is the final form)


def glyph_block(width, gap_ratio=0.16, row_gap_ratio=0.22):
    """The two words as one alpha-less picture `width` px wide: [(row image, colour)] stacked.

    Returns an 'L' mask per row, all the same height, on a shared baseline."""
    size = 400
    font = ImageFont.truetype(str(FONT), size)
    gap = int(size * gap_ratio)
    layers = []
    for word, _ in ROWS:
        layer = Image.new("L", (size * 4, size * 2), 0)
        d = ImageDraw.Draw(layer)
        x = size * 4 - size // 2                    # start at the right edge
        for ch in word:
            adv = font.getlength(ch)
            d.text((x - adv, size + size // 2), ch, font=font, fill=255, anchor="ls")
            x -= adv + gap
        layers.append(layer)
    # one shared crop, so the two rows keep the same height and baseline
    box = None
    for lay in layers:
        b = lay.getbbox()
        box = b if box is None else (min(box[0], b[0]), min(box[1], b[1]), max(box[2], b[2]), max(box[3], b[3]))
    top, bottom = box[1], box[3]
    rows = []
    for lay in layers:
        l, _, r, _ = lay.getbbox()
        rows.append(lay.crop((l, top, r, bottom)))
    rw = max(r.width for r in rows)
    rh = rows[0].height
    row_gap = int(rh * row_gap_ratio)
    block_h = rh * 2 + row_gap
    scale = width / rw
    return rows, rw, rh, row_gap, block_h, scale


def draw_mark(canvas, cx, cy, radius, colours, fit="circle"):
    """Draw the mark centred on (cx, cy), as large as fits inside a circle of `radius`
    (fit="circle") or a square of half-side `radius` (fit="box")."""
    rows, rw, rh, row_gap, block_h, _ = glyph_block(1)
    half_diag = (rw ** 2 + block_h ** 2) ** 0.5 / 2
    scale = radius / half_diag if fit == "circle" else min(radius * 2 / rw, radius * 2 / block_h)
    y = cy - block_h * scale / 2
    for row, colour in zip(rows, colours):
        w, h = round(row.width * scale), round(row.height * scale)
        mask = row.resize((w, h), Image.LANCZOS)
        canvas.paste(Image.new(canvas.mode, (w, h), colour), (round(cx - w / 2), round(y)), mask)
        y += (rh + row_gap) * scale


def icon(size, radius_ratio, bg=GREEN, colours=(FATHER, MOTHER), fit="circle"):
    s = 4                                           # draw large, then shrink: smooth edges
    big = Image.new("RGB", (size * s, size * s), bg)
    draw_mark(big, size * s / 2, size * s / 2, radius_ratio * size * s, colours, fit)
    return big.resize((size, size), Image.LANCZOS)


def main():
    res, web = ROOT / "resources", ROOT / "web/icons"
    # Android's adaptive icon is cut to a circle ~66% of the picture: keep clear of it.
    master = icon(1024, 0.315)
    master.save(res / "icon-only.png")
    # The browser/home-screen icons: "any" fills more, "maskable" keeps to the 80% safe circle.
    for name, size, ratio in [("icon-512", 512, 0.40), ("icon-192", 192, 0.40),
                              ("icon-maskable-512", 512, 0.36), ("icon-maskable-192", 192, 0.36),
                              ("apple-touch-icon", 180, 0.42)]:
        icon(size, ratio).save(web / f"{name}.png")
    icon(64, 0.48, fit="box").save(web / "favicon-64.png")

    # The splash: the same rounded tile as before, centred on the page colour.
    tile, radius, at = 560, 112, 1086
    t = icon(tile, 0.40)
    mask = Image.new("L", (tile * 4, tile * 4), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, tile * 4 - 1, tile * 4 - 1), radius * 4, fill=255)
    mask = mask.resize((tile, tile), Image.LANCZOS)
    for name, bg in [("splash", PAPER), ("splash-dark", DARK)]:
        page = Image.new("RGB", (2732, 2732), bg)
        page.paste(t, (at, at), mask)
        page.save(res / f"{name}.png")

    # The reminder's small icon: a white silhouette on a clear ground. (File name kept.)
    stat = Image.new("RGBA", (96 * 4, 96 * 4), (0, 0, 0, 0))
    draw_mark(stat, 96 * 2, 96 * 2, 47 * 4, ((255, 255, 255, 255),) * 2, fit="box")
    stat.resize((96, 96), Image.LANCZOS).save(res / "android/ic_stat_aleph.png")
    print("OK: icons written")


if __name__ == "__main__":
    main()
