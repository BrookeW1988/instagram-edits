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
site. Where to look: the maker's announcement for that FEATURE (search "<maker> <feature> announcement", e.g.
"Claude projects", "Claude connectors Gmail", "Claude skills") and its help-centre article; product home pages are
mostly decorative art. Run `~/.instagram-edits/venv/bin/python SKILL_DIR/scripts/grab_page_images.py <page> <folder>`,
LOOK at every image, and keep only one that clearly shows the named thing (the feature's own screen). Crop it to
just the app window with Pillow and save it in `~/Movies/Edits-assets/<reel>/crops/`.
- An abstract step ("build an About Me doc", "set up a folder") has no product page: use the screen where it
  happens (a Claude chat asking questions; a folder in Claude's file view), or ask her for a screenshot.
- Nothing shows it? Ask her in the plan, or make that beat a word stack instead. Never a loosely related screen,
  never a mock-up.
- **The split-demo crop** must be roughly square (about 1.1 wide : 1 tall) so at scale 1 it fills the top half;
  a normal wide screenshot only fills a quarter. Crop the part of the screen that matters.

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
   On stretches of her face longer than ~4 s with no card or stack, add a 1.06-1.08 punch-in (chin-anchored) on
   the next sentence start.
3. **Hook:** `addOverlay` hook.png at 0, x 0.36, y 0.15, scale 0.62, `trim` to the end of her first line.
4. **Cards:** `addOverlay` each at its start, x 0.5, y 0.37, scale 0.95; photos default to 3 s, `trim` to fit.
5. **Split demo (once):** on the line about using the thing ("so it can work inside your tools"), `setTransform`
   the piece you split out y 0.68 scale 1 with `allowBeyondCanvas` true (she slides down), and
   `addOverlay` the plain crop at x 0.5, y 0.255, scale 1 (fills the top half). Put that line's caption on the seam:
   `setTextPosition` y 0.52 (if the split starts mid-caption, `splitCaption` at the split time first and re-apply
   font/size), then `moveToLayer` the screenshot to a free low layer and the caption above it: every `addOverlay`
   makes its own track, `tracks` lists them in order (0 = main video, 1 = captions), and a "free" layer is an
   overlay track with nothing on it at that time (e.g. the hook's track after the hook ends).
6. **Stacks:** `addOverlay` each on the words, alternate x (0.33 / 0.5 / 0.6), 1.5-5 s. Size and height depend on
   her framing: `captureFrame` and place the stack ABOVE the top of her head (often y 0.15-0.22) at the biggest
   scale that stays inside the frame (often 0.6-0.9 for 2-line stacks). It must not sit on her hair or face, and
   no part may run past an edge.
7. **Sound:** `pause`, `seek` to each card, `addSoundEffect` "Lip pop (sharp)", volume 0.35. "Page flip 1" at
   0.3 on the split. No music needed (add a royalty-free bed only if she wants one).
8. **Grade:** `addAdjustmentLayer` + `applyAdjust` temperature +8, exposure +3.

## Check
Next to a Mariah reel (instagram.com/itsmariahbrunner): one big word at a time; a real screen on every card; her
face blurred under the cards; a change every 2-4 s; nothing past the edges; stacks never over her face.
