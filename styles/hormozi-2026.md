# Quick recipe: Hormozi 2026 ("Red Tag Desk Talk")

**Looks like:** a red label tag above the head for the first 4.5 s, small sentence-case captions that hard-swap with
one heavier word, a word-tight cut, one hard punch-in near the end, no transitions, and it stops dead on the last word.
**Inspired by:** [Alex Hormozi](https://www.instagram.com/hormozi/) (editing techniques only: none of his footage,
logos, tag wording or catchphrases). Every number: `LOOKS/looks/hormozi-2026/SPEC.md`.
**Use for:** direct teaching, best on a spoken list ("here's why: one... number two..."). Effort: low.
**Needs:** one talking-head take, filmed vertical. Length 12-40 s.

## Look (sizes on a 1080x1920 frame)
| | Spec |
|---|---|
| Label tag | Montserrat Black Italic, 53 px, CAPS, white on a red `#FF0000` box (PNG), 3-4 words, centred, top at y ~262, above her head. Frame 0 to 4.5 s, hard on and off ([Google Fonts](https://fonts.google.com/specimen/Montserrat)) |
| Captions | Poppins Regular 72 px, white, soft shadow, no box, ONE line of 2-3 words, sentence case, no full stops or commas, centred at y ~1478 (just under the chin; y ~940 on a wider desk shot) ([Google Fonts](https://fonts.google.com/specimen/Poppins)) |
| Caption motion | None: hard swap, on at the first word, off when the next caption starts. One heavier (bold) word in about half the captions |
| List points | One number card per spoken point, top of the frame once the tag has gone, in on its word, out when she moves on |
| Zooms | Locked off. ONE hard punch-in to 115% near the end, held to the last word. No other zooms |
| Palette | Red `#FF0000` (tag only; or her loud brand colour), white, ink `#111114` (card text) |
| Grade | High-key and clean: exposure and highlights up a little, contrast +3, saturation -8. No filters |
| Pacing | 1.15x, every pause out, zero dead air |
| Sound | Voice only. No sound effects, no music |

## Hook formulas (the tag is a LABEL in her words, not a sentence)
- "PRICING MISTAKE" / "STOP DOING THIS"
- "[NUMBER] REASONS WHY"
- "THE [THING] FIX"

## Presets to save in Edits
- Text: **Red tag** (PNG). Captions: **Desk captions** (Poppins, white, no box, no animation, y ~0.77).

## Recipe
1. Cut word-tight (no trims under 0.15 s), `setSpeed` 1.15.
2. Tag: `make_text_card.py hook --lines "..." --box "#FF0000" --ink "#FFFFFF" --size 53 --font <Montserrat Black
   Italic file>`, then `addOverlay` (x 0.5, y ~0.16) and `trim` it to 0-4.5 s.
3. Captions: `generateCaptions`, then the plainest style in `listCaptionStyles` (no box, no highlight, no pop),
   `setTextFont` Poppins, `setTextPosition` y ~0.77. Split long captions down to 2-3 words. If the style can make one
   word heavier, do it on the stressed word in about half of them; if it can't, leave it.
4. List points (only if the take IS a list): `make_text_card.py number --num 2 --label "..." --accent "#FF0000"`,
   `addOverlay` at y ~0.2 on the spoken word.
5. Punch-in: `splitAt` at a word gap near the end, `setTransform` scale 1.15 on that last piece.
6. Grade with the colour tools. End on the last word: no end card.
7. Tell her in one line what was swapped: the redacted list card that clears point by point and the progress meter
   are now plain number cards.

## Do / don't
- Do proofread every caption: they're small, but they carry the reel.
- Don't add pops, bounce, karaoke colour, all-caps captions, transitions, slow pushes, music or a second punch-in.
