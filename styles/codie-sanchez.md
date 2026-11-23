# Quick recipe: Codie Sanchez ("Studio editorial")

**Looks like:** the quiet, expensive founder look. Two-line white serif captions with a soft glow, a warm grade, hard
cuts between two framings that hide every jump cut, a soft music bed, and nothing that bounces.
**Inspired by:** [Codie Sanchez](https://www.instagram.com/codiesanchez/) (editing techniques only: none of her
footage, mic flag, logos, catchphrases or music). Every number: `LOOKS/looks/codie-sanchez/SPEC.md`.
**Use for:** considered opinions, money and business lessons, anything that should feel calm and expensive. Effort: low.
**Needs:** one seated talking-head take, filmed vertical. Length 15-30 s.

## Look (sizes on a 1080x1920 frame)
| | Spec |
|---|---|
| Captions | EB Garamond Bold 94 px, white, soft dark glow (shadow with no offset), no box, no outline, 2 lines of 2-4 words, sentence case, no punctuation, max ~760 px wide ([Google Fonts](https://fonts.google.com/specimen/EB+Garamond)) |
| Caption position | Top of the block at y ~1500 on a close-up, just under the chin; y ~1100 if her chest is in shot |
| Caption motion | None: hard swap on the first word. The first caption is on screen from frame 0 (it's the hook) |
| Payoff | The last line as its own text: EB Garamond Italic ~104 px, white, a gentle 0.2 s slide in, held to the end |
| Zooms | Two "cameras" from one phone: A = 100%, B = 118%. Hard switch on phrase ends every ~2-3 s, and always on a jump cut. Never a moving zoom |
| Palette | White only, plus the soft black glow |
| Grade | Warm and rich: temperature up, saturation +12, contrast +8, highlights -15, blacks lifted a touch. No vignette, no filters |
| Pacing | 1.0x (never sped up). Cuts at phrase ends only. Stop ~0.05 s after the last word |
| Sound | No sound effects. A soft lofi or ambient bed 16-20 dB under her voice (Edits volume about 10-15%) from 0:00 to the end, no swells. She adds it in the Edits window |

## Hook formulas (the first caption IS the hook)
- "The quietest way to [result]"
- "Most [owners] get [thing] backwards"
- "What I'd do with [time or money] if I started again"

## Presets to save in Edits
- Captions: **Editorial caption** (EB Garamond Bold, white, glow, 2 lines). Text: **Payoff line** (EB Garamond Italic).

## Recipe
1. Cut at phrase ends only, keep 1.0x. Import EB Garamond (roman and italic) with `importAccountFont` if it isn't in
   Edits yet.
2. Captions: `generateCaptions`, the closest style in `listCaptionStyles` with a shadow and no box, `setTextFont`
   EB Garamond Bold, `setTextPosition` y ~0.8 (or ~0.6 with her chest in shot). Check the chin never reaches them.
3. Framing: `splitAt` on phrase ends, `setTransform` scale 1.18 on every other piece (A, B, A, B), with a B on
   every jump cut so the cut reads as a second camera.
4. Payoff: the last line as Edits text (plainest base in `listTextPresets`), EB Garamond Italic, with the gentlest
   slide-in from Edits' text animations. Delete the captions under it.
5. Grade with the colour tools. Tell her to add the music bed in the Edits window.
6. Tell her in one line what was swapped: the bold serif lead-in over a light sans line that types on word by word
   is now one serif caption block.

## Do / don't
- Do split a long caption rather than shrink it: keep every line inside ~760 px.
- Don't use coloured or highlighted words, outlines, all caps, emoji, transitions, sound effects or an end card.
