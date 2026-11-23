# Quick recipe: Iman Gadzhi ("Value-only motion")

**Looks like:** her face does most of the talking; graphics only fire on the claims, numbers and numbered steps, so
each one feels like a reward. One accent colour, condensed caps on black tape, short handwritten notes, a 1-2-3 count.
**Inspired by:** [Iman Gadzhi](https://www.instagram.com/imangadzhi/) (editing techniques only: none of his footage,
logos, chapter objects, product names or catchphrases). Every number: `LOOKS/looks/iman-gadzhi/SPEC.md`.
**Use for:** "three reasons", "the steps", a claim with a real number in it. Effort: medium.
**Needs:** one talking-head take, ideally with a spoken list ("one... number two..."). Length 30-45 s.

## Look (sizes on a 1080x1920 frame)
| | Spec |
|---|---|
| Hook | Anton ~134 px, CAPS, white on an ink `#0B0B0D` tape (PNG), 1-3 words, in the top band (y ~280-535) above her head, frame 0 to ~1.8 s. A short note above it in Caveat Bold 86 px, accent ([Google Fonts](https://fonts.google.com/specimen/Anton), [Caveat](https://fonts.google.com/specimen/Caveat)) |
| Chapters | On "one / number two / number three": a number card + a 1-2 word title in Anton on ink tape, in the top band, in on the word, out at the end of that point's value sentence |
| Big moments | The hook claim and the biggest number she says: Anton, big (the number ~250 px), white with the accent, in the top band. Hard in, hard out |
| Captions | Inter ExtraBold 62 px, white, ink outline, the spoken word on an accent box, max 3 words, top at y ~1440. Off during the big moments |
| Budget | A graphic on screen for at most 35% of the reel (3-6 moments in 30-45 s). Stories, caveats and warm-ups stay on her bare face |
| Zooms | Hard punch-ins only, alternating 108% / 100% / 106% / 100% at each jump cut. Never a creep |
| Palette | One accent (`#2230E8`, or her brand colour), ink `#0B0B0D`, white. Nothing else |
| Grade | Clean with a little bite: contrast +10, blacks down a touch, a touch cool (warm if her accent is warm), a light vignette if Edits' filters have one |
| Pacing | 1.1x. Keep the hook, the claim, each point's value sentence and the close; drop the waffle between points |
| Sound | One hit per graphic, ~8 dB under the voice: stamp (hook, number), page turn, pen writing (notes), a DIFFERENT whoosh on each chapter, thud on the number. No music |

## Hook formulas (a number only if she really says it)
- "[NUMBER]X YOUR [THING]" + note "here's how"
- "STOP [HABIT]" + note "three reasons"
- "[RESULT] IN [TIME]" + note "the steps"

## Presets to save in Edits
- Text: **Value tape** (PNG), **Pen note** (Caveat, accent). Captions: **Value caption** (accent box on the word).

## Recipe
1. Read the transcript and tag only the value sentences: a bold claim, a definition, any number, "number two", a
   promise, real proof. Test: would it still be useful written on a sticky note?
2. Cut to those plus the hook and the close, `setSpeed` 1.1. Punch-ins alternate at each jump cut (`splitAt` +
   `setTransform`).
3. Hook: `make_text_card.py hook --lines "..." --box "#0B0B0D" --ink "#FFFFFF" --size 134 --font <Anton file>`,
   `addOverlay` at y ~0.21. The note as Edits text in Caveat, accent, with the closest write-on or typewriter from
   Edits' text animations.
4. Chapters: `make_text_card.py number --num 1 --label "..." --accent <accent>` + a title tape PNG on each point.
5. Captions: **Word Highlight Box 2** + `setCaptionHighlightColor` (accent), `setTextFont` Inter ExtraBold,
   `setTextPosition` y ~0.77. Delete them under the big moments.
6. Add up the seconds with a graphic on screen. Over 35%? Cut the weakest claim, never the number.
7. One sound per graphic (`searchSoundEffects` + `addSoundEffect`), a different whoosh each time.
8. Tell her in one line what was swapped: the full-screen textured fields (now big type in the top band), the
   letter-by-letter write-on, the number counting up and the dropping bills.

## Do / don't
- Do let long stretches be just her face: the bare face is what makes the graphics land.
- Don't put a graphic on a story sentence, use a second colour, invent a stat, or reuse the same whoosh.
