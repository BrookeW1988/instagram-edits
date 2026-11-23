#!/usr/bin/env python3
"""make_text_card.py: draw a boxed text hook or a numbered list card as a see-through PNG for Edits.

WHY: Edits' automation tools can add text but can't put a white rounded box behind it, and the boxed hook
is the signature of most looks here. So we draw it as a PNG with a transparent background and Claude drops
it in with Edits' addOverlay (x 0.5, y ~0.14 for a hook; scale = fraction of the frame width).

Run with the skill's Python (it has Pillow):  ~/.instagram-edits/venv/bin/python make_text_card.py ...

  Hook (one white box per line, lines touching, optional emoji on the end):
    make_text_card.py hook --lines "I tried 5 AI tools" "and one blew my mind" --emoji 🤯 \
        --font ~/Movies/Edits-assets/fonts/Inter-ExtraBold.ttf --ink "#141414" --out ~/Movies/Edits-assets/reel/hook.png

  Number card (white pill, coloured number badge, label):
    make_text_card.py number --num 1 --label "Dopamine" --accent "#FF5A36" \
        --font ~/Movies/Edits-assets/fonts/Inter-ExtraBold.ttf --out ~/Movies/Edits-assets/reel/card-1.png

Colours and fonts come from the member's profile.md. Prints the PNG's path and size.
"""
import argparse
import os

from PIL import Image, ImageDraw, ImageFont

EMOJI_FONT = "/System/Library/Fonts/Apple Color Emoji.ttc"   # built into every Mac


def emoji_img(ch, size):
    # Apple Color Emoji only draws at 160 px, so draw it big then shrink it to match the text
    f = ImageFont.truetype(EMOJI_FONT, 160)
    im = Image.new("RGBA", (200, 200), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((10, 10), ch, font=f, embedded_color=True)
    return im.crop(im.getbbox()).resize((size, size), Image.LANCZOS)


def line_box(text, font, size, ink, box, emoji=None, pad_x=44, pad_y=26, radius=34):
    """One rounded box holding one line of text (+ optional emoji at the end)."""
    f = ImageFont.truetype(font, size)
    l, _t, r, _b = f.getbbox(text)
    asc, desc = f.getmetrics()
    tw, th = r - l, asc + desc
    ew = (size + 18) if emoji else 0
    w, h = tw + ew + pad_x * 2, th + pad_y * 2
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, w - 1, h - 1), radius=radius, fill=box)
    d.text((pad_x - l, pad_y), text, font=f, fill=ink)
    if emoji and os.path.exists(EMOJI_FONT):
        im.alpha_composite(emoji_img(emoji, size), (pad_x + tw + 18, pad_y + (th - size) // 2))
    return im


def stack(boxes, gap=-6):
    """Stack the line boxes centred, slightly overlapping so they read as one block (the Taki-style look)."""
    w = max(b.width for b in boxes)
    h = sum(b.height for b in boxes) + gap * (len(boxes) - 1)
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    y = 0
    for b in boxes:
        im.alpha_composite(b, ((w - b.width) // 2, y))
        y += b.height + gap
    return im


def number_card(num, label, font, size, ink, box, accent):
    """White pill with a coloured number badge, one per list item."""
    f = ImageFont.truetype(font, size)
    l, _t, r, _b = f.getbbox(label)
    asc, desc = f.getmetrics()
    th = asc + desc
    badge, pad = th + 10, 30
    w, h = pad + badge + 30 + (r - l) + 54, badge + pad * 2
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, w - 1, h - 1), radius=h // 2, fill=box)
    d.ellipse((pad, pad, pad + badge, pad + badge), fill=accent)
    nl, _nt, nr, _nb = f.getbbox(num)
    d.text((pad + (badge - (nr - nl)) // 2 - nl, pad + 5), num, font=f, fill=box)
    d.text((pad + badge + 30 - l, pad + 5), label, font=f, fill=ink)
    return im


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("kind", choices=["hook", "number"])
    p.add_argument("--lines", nargs="+", help="hook: one string per line (2 lines best, 3 max)")
    p.add_argument("--emoji", help="hook: one emoji added to the end of the last line")
    p.add_argument("--num", help="number card: the number")
    p.add_argument("--label", help="number card: the label")
    p.add_argument("--font", required=True, help="full path to a .ttf/.otf (bold weights read best)")
    p.add_argument("--size", type=int, default=88, help="text size in px on a 1080-wide frame")
    p.add_argument("--ink", default="#141414", help="text colour")
    p.add_argument("--box", default="#FFFFFF", help="box colour")
    p.add_argument("--accent", default="#FF5A36", help="number badge colour")
    p.add_argument("--out", required=True)
    a = p.parse_args()

    font = os.path.expanduser(a.font)
    out = os.path.expanduser(a.out)
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)

    if a.kind == "hook":
        if not a.lines:
            p.error("hook needs --lines")
        boxes = [line_box(t, font, a.size, a.ink, a.box,
                          emoji=a.emoji if i == len(a.lines) - 1 else None) for i, t in enumerate(a.lines)]
        img = stack(boxes)
    else:
        if not (a.num and a.label):
            p.error("number needs --num and --label")
        img = number_card(a.num, a.label, font, a.size, a.ink, a.box, a.accent)

    img.save(out)
    print(out, img.size)


if __name__ == "__main__":
    main()
