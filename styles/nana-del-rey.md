# Quick recipe: Nana Del Rey ("Soft Cinema")

**Looks like:** slow, warm and filmic. Giant butter-yellow words land one at a time in the air above her head, thin
cream lowercase subtitles sit in that same air, a darker warm grade, a quiet music bed, hard cuts only.
**Inspired by:** [Nana DelRey](https://www.instagram.com/nanadelrey/) (editing techniques only: none of her footage,
rooms, names, keywords or catchphrases). Every number: `LOOKS/looks/nana-del-rey/SPEC.md`.
**Use for:** reflective, personal, slow-burn thoughts and soft sells. Effort: medium.
**Needs:** one talking-head take with some room above her head (the words live there), filmed vertical. Length 15-25 s.

## Look (sizes on a 1080x1920 frame)
| | Spec |
|---|---|
| Giant words | Inter Tight ExtraBold, hero word up to ~236 px (fitted to ~900 px wide), butter `#F8F49C`, with a 76 px Bold connector line above it. 2-3 stacks per reel. Above her head (baseline y ~540-718), never on her face ([Google Fonts](https://fonts.google.com/specimen/Inter+Tight)) |
| Payoff word | One word per stack at most in lilac `#E4C8EC` (the opening and closing stacks) |
| Subtitles | Inter Tight Regular 48 px, cream `#FCF4AC`, lowercase, no full stops or commas, no box, outline or shadow, baseline y ~480 (the air above her head). Off while a giant word is up |
| Motion | Everything hard-cuts. Each giant word appears in one frame on its spoken word. No fades, slides, pops or typewriter |
| Zooms | None. No punch-ins, no camera moves |
| Palette | Butter `#F8F49C`, lilac `#E4C8EC`, cream `#FCF4AC`. Never more than two colours in a stack |
| Grade | Darker and warmer: exposure down, highlights well down, temperature up, saturation down a touch, so yellow reads even on a bright wall. Her face warm and natural. No vignette, no grain |
| Pacing | 1.0x (slow is the point). One or two hard cuts, at sentence ends only |
| Sound | No sound effects. A soft instrumental bed about 14 dB under her voice (Edits volume about 15-20%), added by her in the Edits window |

## Hook formulas (the opening stack is the hook; her own words, lowercase connectors)
- "the [thing] / I stopped [doing]"
- "you don't need / more [thing]"
- "what I'd tell / [my younger self]"

## Presets to save in Edits
- Text: **Giant word** (Inter Tight ExtraBold, butter), **Payoff word** (lilac). Captions: **Soft subtitle** (cream).

## Recipe
1. Cut long pauses only, 1.0x, one or two cuts at sentence ends. No punch-in to hide them.
2. Pick the 2-3 phrases she leans on. Each one: a connector line + a hero word as Edits text (plainest base in
   `listTextPresets`: no box, no outline, no animation), `setTextFont` Inter Tight, butter (the payoff word lilac),
   on its word, held ~0.8-1.3 s past the last word. A stack is up from frame 0 if she starts talking straight away.
3. Subtitles: `generateCaptions`, plainest style in `listCaptionStyles` (no box, no highlight, no pop),
   `setTextFont` Inter Tight Regular, cream, `setTextPosition` y ~0.25. Lowercase them with `editCaption`. Delete
   the ones that fall under a giant word.
4. Grade darker and warm. If her head is near the top of the frame, make the words smaller or sit them beside her.
5. Tell her in one line what was swapped: the giant words sit above her head instead of tucked behind it, and the
   subtitles are one centred line instead of three spaced chunks. If Edits' subject cut-out can put text behind her,
   try it on one stack and note in `profile.md` whether it worked.

## Do / don't
- Do check every frame with `frameSheet`: no text on her face, every word clear of her hair.
- Don't add pops, slides, strokes, boxes, shadows, capitals in subtitles, sound effects, punch-ins or an end card.
