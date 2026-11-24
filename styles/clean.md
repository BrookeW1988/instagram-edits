# Clean (inspired by Alex Hormozi's classic captions)

**What it is:** her face, cut tight, with big bold caps captions where the word she's saying lights up yellow, and
punch-ins on the big lines. No boxes, no cards. Works on ANY talking-head take.
**Needs:** just her take. **Inspired by** Hormozi's editing technique only: never his footage, logo or phrases.
**Read first:** `references/editing-craft.md`.

## Build (after the rough cut)
1. **Fonts:** `importAccountFont` `Montserrat-Black.ttf` (Edits calls it `MontserratThin-Black`).
2. **Captions:** `generateCaptions` -> `splitCaption` into 2-3 word groups (break at commas and pauses) ->
   `setCaptionStyle` "Word Highlight 3" -> `setCaptionHighlightColor` `#FFE600` -> `editCaption` each to CAPS ->
   on every caption `setTextFont` `MontserratThin-Black` + `setTextStyle` size 84, centred + `setTextPosition` y 0.77.
3. **Hook (0 to the end of her first line, ~3 s):** `addText` her hook in 2 short lines, CAPS, 5-9 words ->
   `setTextFont` `MontserratThin-Black`, size 38, white -> `setEmphasis` outline `#000000` -> `setTextPosition`
   y 0.16 -> no animation. Hide the captions under it (`setTextStyle` size 1).
4. **Punch-ins (the cut grammar of this look):** `splitAt` at sentence starts, then alternate 1.00 / 1.18 with
   `setTransform`. ONE 1.30 on the biggest line. Anchor on her chin so her face stays put:
   y = 0.5 - (c - 0.5) x (s - 1), where c = her chin height in the frame (often ~0.73) and s = the scale.
   (c 0.73: 1.18 -> y 0.459, 1.30 -> y 0.431.)
5. **Hero word (optional, once):** on the 1.30 punch-in, a separate `addText` of the one big word or number,
   Montserrat Black size 110 (fine for a short word or number; a longer word wraps, so use size ~38 plus
   `setTransform` scale ~2.8), `#FFE600`, outline black, animation `fligPop` (check `listTextAnimations`), 1-1.5 s.
6. **Sound:** ONE whoosh ("Whoosh (airy) 6", trimmed to ~1 s, volume 0.35) on the 1.30. Nothing else.
7. **Grade:** `addAdjustmentLayer` + `applyAdjust`: contrast +10, saturation -5, temperature -6.

## Check
Captions 2-3 words, never over her mouth; yellow word = the word being said; punch-ins on sentence starts, never
mid-word; the hook gone before the first caption shows.
