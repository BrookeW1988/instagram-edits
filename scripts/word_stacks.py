"""word_stacks.py: big stacked words, drawn as see-through PNGs for Edits.

WHY a PNG: Edits text has no soft shadow and no letter-spacing control, and a big Edits text box wraps long words.
Both styles below depend on those, so the words are drawn here and dropped into Edits with addOverlay.

Two kinds:
  "show-it"     Show it keyword stacks + hook: Inter Black, Title Case, butter yellow + white, soft dark shadow,
                second line nudged right. One PNG per stack.
  "broll-story" B-roll story giant words: Inter Tight ExtraBold, lowercase, tight letter-spacing, butter / lilac /
                white, mixed sizes. Saved as BUILD frames (<name>-1.png, -2.png ...): line 1, then lines 1-2, and so
                on, so in Edits the words appear as she says them (put the frames back to back).

usage:  ~/.instagram-edits/venv/bin/python word_stacks.py spec.json
spec.json (valid JSON; replace NAME and REEL; "kind" is "show-it" or "broll-story"):
{
  "out": "/Users/NAME/Movies/Edits-assets/REEL/stacks",
  "kind": "show-it",
  "stacks": {
    "hook":    [["Learn Claude", "butter", "big"], ["In One Day", "butter", "big", 60], ["Hour By Hour", "white", "small", 10]],
    "the-lot": [["Hand Claude", "white", "small"], ["The Lot", "butter", "big", 70]]
  }
}
Each line = [text, colour, size, optional nudge-right in px]. Colours: butter, lilac, white, or a hex like "#FF5A36".
Sizes: "big" / "medium" / "small" (or a number of px at 2x).
"""
import json, os, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

FONTS = os.path.expanduser("~/Movies/Edits-assets/fonts")
COLOURS = {"butter": (248, 240, 152), "lilac": (213, 184, 246), "white": (255, 255, 255)}
KINDS = {
    #             font file                  big  medium small  tracking  leading  shadow alpha / blur
    "show-it":     ("Inter-Black.ttf",        168, 140,   112,   0.0,      0.98,    150, 14),
    "broll-story": ("InterTight-ExtraBold.ttf", 300, 150, 110,  -0.045,    0.86,    90, 18),
}


def colour(c):
    if c in COLOURS:
        return COLOURS[c]
    c = c.lstrip("#")
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))


def size_px(s, kind):
    if isinstance(s, (int, float)):
        return int(s)
    big, med, small = KINDS[kind][1:4]
    return {"big": big, "medium": med, "small": small}[s]


def text_w(d, text, f, size, track):
    return sum(d.textlength(ch, font=f) + track * size for ch in text)


def draw_text(d, x, y, text, f, fill, size, track):
    if track == 0:
        d.text((x, y), text, font=f, fill=fill)
        return
    for ch in text:          # letter by letter so the spacing can be tightened
        d.text((x, y), ch, font=f, fill=fill)
        x += d.textlength(ch, font=f) + track * size


def render(lines, kind, upto):
    font_file, _, _, _, track, leading, sh_alpha, sh_blur = KINDS[kind]
    probe = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    rows = []
    for ln in lines:
        text, col, sz = ln[0], colour(ln[1]), size_px(ln[2], kind)
        dx = ln[3] if len(ln) > 3 else 0
        if kind == "broll-story":
            text = text.lower()
        rows.append((text, col, sz, dx, ImageFont.truetype(os.path.join(FONTS, font_file), sz)))
    pad = 80
    W = int(max(text_w(probe, t, f, s, track) + dx for t, _, s, dx, f in rows)) + pad * 2
    H = int(sum(s * leading for _, _, s, _, _ in rows)) + pad * 2
    txt = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(txt)
    y = pad
    for t, col, s, dx, f in rows[:upto]:
        draw_text(d, pad + dx, y - int(s * (0.2 if kind == "broll-story" else 0.12)), t, f, col + (255,), s, track)
        y += int(s * leading)
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sh.paste((10, 10, 14, sh_alpha), (8, 12), txt.split()[3])
    return Image.alpha_composite(sh.filter(ImageFilter.GaussianBlur(sh_blur)), txt)


if __name__ == "__main__":
    spec = json.load(open(sys.argv[1]))
    out, kind = spec["out"], spec.get("kind", "show-it")
    os.makedirs(out, exist_ok=True)
    for name, lines in spec["stacks"].items():
        if kind == "broll-story":
            for n in range(1, len(lines) + 1):      # build frames, all the same size so they line up in Edits
                render(lines, kind, n).save(os.path.join(out, f"{name}-{n}.png"))
        else:
            render(lines, kind, len(lines)).save(os.path.join(out, f"{name}.png"))
        print(name)
    print(out)
