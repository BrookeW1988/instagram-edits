# Quick recipe: Calm luxury

**Looks like:** the camera never moves, only she does. One small white serif line that swaps on the phrase, warm
window light, hard cuts, no effects, and it loops.
**Inspired by:** [Jess Bergeron](https://www.instagram.com/jkb.journal/) (editing techniques only: none of her footage,
wording, product, logos or styling). Every number: `LOOKS/looks/calm-luxury/SPEC.md`.
**Use for:** high-end or slow-living brands, coaches and makers who want to look expensive and unhurried. Effort: low.
**Needs:** one locked-off take (phone on a stand, soft window light, a dark top), calm, one thought, no spoken CTA.
Hands or product footage is even better. Length 10-20 s.

## Look (sizes on a 1080x1920 frame)
| | Spec |
|---|---|
| Caption line | Newsreader Regular 51 px, white, ONE line of 3-6 words (max ~32 characters), sentence case, centred at y ~1480, sitting on her dark top ([Google Fonts](https://fonts.google.com/specimen/Newsreader)) |
| Caption treatment | 100% white. No box, outline, shadow, highlight or accent colour, ever |
| Caption motion | None: hard on, hard off, swapping on the phrase. The first line is on screen from frame 0 |
| Framing | Locked. One fixed 112% crop for the whole reel (anchored low), only if it lifts her chin clear of the caption line. Never animated |
| Zooms | None. No punch-ins, not even on a jump cut |
| Palette | White text only. The window light and her dark top do the rest |
| Grade | Warm window light: Warmth +10, Exposure -3, Tint a touch toward green, everything else 0 (an estimate: check it by eye). No vignette, grain, LUT or filters |
| Pacing | 1.0x (her natural speed). One long hold of 8-15 s, cuts only in real pauses (1-2 in the whole reel) |
| Sound | Voice only, no sound effects. Optional soft instrumental (piano, acoustic, ambient) 18 dB under her voice (Edits volume about 12%), added by her in the Edits window |
| End | Ends on a closing line that leads back into the opening line, so it loops. No end card, no CTA on screen |

## Hook formulas (the first caption line is the hook: calm, not hype)
- "I used to think [thing] was the goal"
- "Some days the work is just [small thing]"
- "This is how I [do the thing] now"

## Presets to save in Edits
- Captions: **Quiet serif** (Newsreader, white, no box, no animation, y ~0.77).

## Recipe
1. Cut: one long hold, cuts only in real pauses, keep 1.0x. Check the closing line can loop back into the first.
2. If her chin sits where the caption goes, `setTransform` scale 1.12 on the whole clip, anchored low, once. It's a
   fixed crop, not a zoom.
3. Captions: import Newsreader with `importAccountFont`, `generateCaptions`, the plainest style in
   `listCaptionStyles` (no box, shadow, highlight or pop), `setTextFont` Newsreader, `setTextPosition` y ~0.77.
   One line per caption: split any that wrap.
4. Grade with the colour tools (numbers above). Nothing else.
5. Hands or product footage: one 8-15 s hold with her voice, then 0.6-1.9 s detail shots (muted), and end on the same
   shot it opened on so the loop is invisible.
6. Tell her in one line: Edits picks its own caption breaks and line spacing, so a few lines may split differently
   from the SPEC. Any CTA goes in her Instagram caption, never on screen.

## Do / don't
- Do film for it: locked off, eye level, window at 45° to one side, dark top.
- Don't add zooms, text animation, coloured words, caps, emoji, sound effects, vignette, grain or an on-screen CTA.
