# Show it (inspired by Mariah Brunner)

**What it is:** a chatty talking head where every tool or step she names pops up as a REAL screen on a numbered
lavender card, with the background blurred behind it. One-word captions, yellow-and-white keyword stacks around
her head, and one "split" where the app screen fills the top half and she slides down underneath.
**Needs:** a take where she NAMES things: "5 tools", "my 3 settings", "9am... 11am...". If nothing is named,
there's nothing to show: use Clean. Framing with some room above her head is best (cards sit there).
**Inspired by** Mariah's editing technique only: never her footage, logo, phrases or sign-offs.
**Read first:** `references/editing-craft.md`. Fonts: `Inter-Black.ttf`, `Inter-ExtraBold.ttf`, `Inter-Bold.ttf`.

## 1. Find the screens (Claude does this, she doesn't need a library)
For each thing she names: her own screenshot if she has one; otherwise the official image from the maker's own
site. `~/.instagram-edits/venv/bin/python SKILL_DIR/scripts/grab_page_images.py <official page> <folder>`
(e.g. the product's news or help page), LOOK at what came down, pick the one that shows the thing, and crop it to
just the app window with Pillow. Save crops in `~/Movies/Edits-assets/<reel>/crops/`. Never mock up a screen.

## 2. Make the graphics
- **Cards:** write a spec (see the top of `scripts/show_it_cards.py`): one card per named thing, badge = the number
  or time she says ("1", "9AM"), label = 2-5 words of what she says, sub-label = a few words more. Run it.
  Optional: `accent` = her brand colour instead of the lavender.
- **Hook + keyword stacks:** `scripts/word_stacks.py`, kind `show-it`. The hook = 2 big lines + 1 small line from
  her opening ("Learn Claude / In One Day / Hour By Hour"). Stacks = 2-4 words she says that land a point
  ("Every Chat / Already Knows"), Title Case, big word in butter, small in white. 4-7 stacks per minute.
- **Receipts (optional):** a small framed real screen without a card, for a "proof" moment ("receipts" in the spec).

## 3. Build in Edits (after the rough cut)
1. **Captions FIRST** (before splitting for cards): `generateCaptions` -> `setCaptionStyle` "Short Pop 3" (one
   word at a time) -> fix doubled words at the rough-cut joins and times ("9am") with `editCaption` -> on every
   caption `setTextFont` `Inter-ExtraBold` + `setTextStyle` size 100, white + `setTextPosition` y 0.75.
2. `splitAt` the main clip at every card's in and out time AND the split demo's in and out (cards start ON the
   number she says, ~3 s each). `applyEffect` `video_simple_blur` on each piece that sits under a card.
3. **Hook:** `addOverlay` hook.png at 0, x 0.36, y 0.15, scale 0.62, `trim` to the end of her first line.
4. **Cards:** `addOverlay` each at its start, x 0.5, y 0.37, scale 0.95; photos default to 3 s, `trim` to fit.
5. **Split demo (once):** on the line about using the thing ("so it can work inside your tools"), `setTransform`
   the piece you split out y 0.68 scale 1 with `allowBeyondCanvas` true (she slides down), and
   `addOverlay` the plain crop at x 0.5, y 0.255, scale 1 (fills the top half). Put that line's caption on the seam:
   `setTextPosition` y 0.52, then `moveToLayer` the screenshot to a free low layer and the caption above it.
6. **Stacks:** `addOverlay` each on the words, y 0.19-0.24, alternate x (0.33 / 0.5 / 0.6), scale 0.4-0.76,
   1.5-5 s. Keep the whole stack inside the frame (check the right edge).
7. **Sound:** `pause`, `seek` to each card, `addSoundEffect` "Lip pop (sharp)", volume 0.35. "Page flip 1" at
   0.3 on the split. No music needed (add a royalty-free bed only if she wants one).
8. **Grade:** `addAdjustmentLayer` + `applyAdjust` temperature +8, exposure +3.

## Check
Next to a Mariah reel (instagram.com/itsmariahbrunner): one big word at a time; a real screen on every card; her
face blurred under the cards; a change every 2-4 s; nothing past the edges; stacks never over her face.
