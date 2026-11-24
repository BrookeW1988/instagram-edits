"""grab_page_images.py: download the big images from an official product page, so Claude can show the REAL thing.

WHY: the Show it style puts the actual screen of each tool she names on a card. Most makers publish clean product
screenshots on their own news / product / help pages (for example anthropic.com/news/projects). This grabs every
large image on a page, so Claude can look at them, pick the right one and crop it. Nothing is invented or mocked up.

usage:  ~/.instagram-edits/venv/bin/python grab_page_images.py <page url> <output folder>
Prints each saved file with its size. Images under 600 px wide (icons, logos, avatars) are skipped.
Only use images from the maker's OWN site, for showing their product; never other creators' content.
"""
import os, re, sys, urllib.parse, urllib.request
from io import BytesIO
from PIL import Image

url, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")

# every image link on the page: absolute ones, relative ones (/images/x.png) and Next.js image links
# (/_next/image?url=<real url>), de-duplicated
found = re.findall(r'https://[^"\'\s\\)]+?\.(?:png|jpe?g|webp)', html)
for rel in re.findall(r'(?:src|href)=["\'](/[^"\']+?\.(?:png|jpe?g|webp))', html):
    found.append(urllib.parse.urljoin(url, rel))
for nxt in re.findall(r'/_next/image\?url=([^&"\'\s]+)', html):
    found.append(urllib.parse.urljoin(url, urllib.parse.unquote(nxt)))
seen, n = set(), 0
for link in found:
    if link in seen:
        continue
    seen.add(link)
    try:
        data = urllib.request.urlopen(urllib.request.Request(link, headers={"User-Agent": "Mozilla/5.0"}), timeout=30).read()
        im = Image.open(BytesIO(data))
    except Exception:
        continue
    if im.width < 600:
        continue
    n += 1
    path = os.path.join(out, f"{n:02d}.png")
    im.convert("RGB").save(path)
    print(f"{path}  {im.width}x{im.height}  {link}")
print(f"{n} images saved to {out}")
