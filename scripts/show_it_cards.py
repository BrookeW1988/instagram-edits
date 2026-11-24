"""show_it_cards.py: the numbered cards and small 'receipt' screens for the Show it style.

WHY a PNG: Edits' text boxes are always rounded pills and wrap long words, and Edits can't put a screenshot
inside a panel. So the card is drawn here once and dropped into Edits as ONE overlay. Rendered at 2x so it stays
crisp when Edits scales it.

What a card looks like: a lavender panel (purple on the left fading to near-white), a white pill with the number
or time ("1", "9AM"), a short label and sub-label in white, and the REAL screenshot of the thing she names on the
right, in a white frame, bleeding off the card edge. A 'receipt' is just the screenshot in a white frame.

usage:  ~/.instagram-edits/venv/bin/python show_it_cards.py spec.json
spec.json (valid JSON; replace NAME and REEL):
{
  "out": "/Users/NAME/Movies/Edits-assets/REEL/cards",
  "accent": "#8E7CF0",
  "cards": [
    {"name": "1-projects", "badge": "1PM", "label": "Move work into Projects",
     "sub": "One per part of your business", "shot": "/Users/NAME/Movies/Edits-assets/REEL/crops/projects.png"}
  ],
  "receipts": [ {"name": "doc", "shot": "/Users/NAME/Movies/Edits-assets/REEL/crops/doc.png"} ]
}
"accent" is optional (the lavender; swap in her brand colour). "sub" and "receipts" are optional.
Keep labels to 2-5 words and sub-labels short: anything that won't fit is reported, never silently dropped.
"""
import json, os, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

FONTS = os.path.expanduser("~/Movies/Edits-assets/fonts")
W, H, R = 1640, 900, 56          # card size at 2x and corner radius
PAD = 110                         # room around the card for its soft shadow


def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)


def hex_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def mix(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def gradient(accent):
    # accent on the left -> a pale tint at 45% -> near-white on the right (the screenshot side stays clean)
    pale, white = mix(accent, (255, 255, 255), 0.55), mix(accent, (255, 255, 255), 0.92)
    g = Image.new("RGB", (W, H))
    px = g.load()
    for x in range(W):
        t = x / (W - 1)
        col = mix(accent, pale, t / 0.45) if t <= 0.45 else mix(pale, white, (t - 0.45) / 0.55)
        for y in range(H):
            px[x, y] = col
    return g


def rounded_mask(size, r):
    m = Image.new("L", size, 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, size[0] - 1, size[1] - 1], r, fill=255)
    return m


def framed(shot, max_w, max_h, border=6, radius=30):
    s = Image.open(shot).convert("RGB")
    s.thumbnail((max_w, max_h), Image.LANCZOS)
    f = Image.new("RGBA", (s.width + border * 2, s.height + border * 2), (255, 255, 255, 255))
    f.paste(s, (border, border))
    f.putalpha(rounded_mask(f.size, radius))
    return f


def with_shadow(img, pad, alpha=95, blur=34, offset=(18, 30)):
    out = Image.new("RGBA", (img.width + pad * 2, img.height + pad * 2), (0, 0, 0, 0))
    sh = Image.new("RGBA", out.size, (0, 0, 0, 0))
    sh.paste((20, 10, 40, alpha), (pad + offset[0], pad + offset[1]), img.split()[3])
    out = Image.alpha_composite(out, sh.filter(ImageFilter.GaussianBlur(blur)))
    out.alpha_composite(img, (pad, pad))
    return out


def wrap(draw, text, f, max_w):
    lines, cur = [], ""
    for word in text.split():
        test = (cur + " " + word).strip()
        if draw.textlength(test, font=f) <= max_w:
            cur = test
        else:
            lines.append(cur)
            cur = word
    lines.append(cur)
    return lines


def card(c, accent, out_dir):
    img = gradient(accent).convert("RGBA")
    # screenshot on the right, clipped by the card edge
    fr = framed(c["shot"], 1000, int(H * 0.78))
    sx, sy = int(W * 0.47), (H - fr.height) // 2
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
    sh.paste((40, 20, 90, 90), (sx + 10, sy + 22), fr.split()[3])
    img = Image.alpha_composite(img, sh.filter(ImageFilter.GaussianBlur(26)))
    img.alpha_composite(fr, (sx, sy))
    d = ImageDraw.Draw(img)
    # badge: white pill, accent-coloured text
    fb = font("Inter-ExtraBold.ttf", 44)
    bw = int(d.textlength(c["badge"], font=fb)) + 56
    d.rounded_rectangle([72, 76, 72 + bw, 154], 39, fill="white")
    d.text((100, 90), c["badge"], font=fb, fill=mix(accent, (0, 0, 0), 0.2))
    # label + sub-label in the left column
    fl = font("Inter-ExtraBold.ttf", 80)
    lines = wrap(d, c["label"], fl, 640)
    if len(lines) > 3:
        print(f"WARNING {c['name']}: label too long, shorten it: {c['label']!r}")
    y = 196
    for line in lines[:3]:
        d.text((72, y), line, font=fl, fill="white")
        y += 92
    if c.get("sub"):
        fs = font("Inter-Bold.ttf", 38)
        subs = wrap(d, c["sub"], fs, 640)
        if len(subs) > 2:
            print(f"WARNING {c['name']}: sub-label too long, shorten it: {c['sub']!r}")
        y += 18
        for line in subs[:2]:
            d.text((74, y), line, font=fs, fill=(255, 255, 255, 215))
            y += 48
    img.putalpha(rounded_mask(img.size, R))
    with_shadow(img, PAD).save(os.path.join(out_dir, c["name"] + ".png"))


def receipt(r, out_dir):
    fr = framed(r["shot"], 900, 900, border=12, radius=34)
    with_shadow(fr, 60, alpha=100, blur=22, offset=(10, 18)).save(os.path.join(out_dir, "receipt-" + r["name"] + ".png"))


if __name__ == "__main__":
    spec = json.load(open(sys.argv[1]))
    out = spec["out"]
    os.makedirs(out, exist_ok=True)
    accent = hex_rgb(spec.get("accent", "#8E7CF0"))
    for c in spec.get("cards", []):
        card(c, accent, out)
    for r in spec.get("receipts", []):
        receipt(r, out)
    print(out)
