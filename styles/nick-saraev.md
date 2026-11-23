# Quick recipe: Nick Saraev ("The Recompose")

**Looks like:** the frame rearranges itself around every sentence: her face full frame, then a split with the thing
she means above her, then the real proof full screen, then back to her. A change every 2-3 s, no hard cuts between.
**Inspired by:** [Nick Saraev](https://www.instagram.com/nick_saraev/) (editing techniques only: none of his footage,
logos, branding, catchphrases or his blue). Every number: `LOOKS/looks/nick-saraev/SPEC.md`.
**Use for:** explainers ("how this tool works", "here's why"), anything with real pages to show. Effort: high.
**Needs:** one talking-head take (head and shoulders, centred) + 2-4 real screenshots or pages she names + real logos.
Length 15-30 s.

## Look (sizes on a 1080x1920 frame)
| | Spec |
|---|---|
| Beat states | **Face:** her clip 100%, full frame. **Split:** her clip shrinks to 92% and moves down ~432 px (face in the lower half), the proof or a big word above it (y ~170-850). **Full:** the screenshot fills the frame (~920 px wide) over her |
| Moves | Each change is one 0.5 s ease in/out, starting ~0.13 s before its word. Claim = face, "here's the thing" = split, anything to read = full, new subject = face again |
| Hook | Inter ExtraBold 70 px, 2 lines, ink on white boxes (PNG), top at y ~188, on from frame 0. Her real logos pop in on the tool's name ([Google Fonts](https://fonts.google.com/specimen/Inter)) |
| Big words | When there's no screenshot: one of her words in Playfair Display Italic ~150-210 px, her accent, above her clip on a split beat ([Google Fonts](https://fonts.google.com/specimen/Playfair+Display)) |
| Captions | Inter ExtraBold 58 px, 2-4 words, white + shadow, the spoken word in her accent, y ~1466 on face beats, y ~858 (the seam) on split beats |
| Proof cards | Real screenshots in a white card, rounded corners, soft shadow. A callout (her files or the free pack) on the line she reads |
| Palette | Ink `#101012`, white, her brand accent (default `#FF5A36`) |
| Grade | Natural, a touch cool: contrast +4, highlights -6, shadows +6. No filters |
| Pacing | 1.1x; a layout change every 2-3 s |
| Sound | One tactile sound per move, 6-10 dB under the voice: pop (logos), whoosh (out to a full beat and back; never the same one twice in a row), paper slide (cards), click, marker, camera shutter (a real page lands), one boom on the payoff number. No music |

## Hook formulas
- "[Tool] just replaced / my [old way]"
- "How [thing] / actually works"
- "The [task] / I stopped doing by hand"

## Presets to save in Edits
- Text: **Recompose hook** (PNG), **Big italic word** (Playfair Display Italic, accent). Captions: **Recompose caption**.

## Recipe
1. Cut a 15-30 s explanatory stretch at real pauses, `setSpeed` 1.1. Hide jump cuts inside full beats.
2. Mark every sentence face / split / full (a change every 2-3 s) and show her the short plan before building.
3. Split beats: transform keyframes on her clip (scale 92%, down ~22.5% of the frame height, 0.5 s ease in/out,
   ~0.13 s before the word), and back for face beats. If keyframes misbehave, use Edits' split screen (proof on top,
   her underneath) with a straight switch, and say so.
4. Full beats: `addOverlay` the screenshot card on the word (scale ~0.85-0.9), `trim` it to the beat.
5. Hook: `make_text_card.py hook --lines "..." "..." --box "#FFFFFF" --ink "#101012" --size 70`; logos on the name.
6. Captions: the closest style in `listCaptionStyles` that colours the spoken word without a box, plus
   `setCaptionHighlightColor` (her accent). `setTextPosition` y ~0.76, or ~0.45 for captions on split beats.
7. A sound on every move (`searchSoundEffects` + `addSoundEffect`).
8. Tell her in one line what was swapped: the paper background around her shrunk clip (Edits shows its own
   background there), the type slides and the live highlighter sweeping across the text.

## Do / don't
- Do use only real pages, screenshots and numbers she says. No proof for a sentence? A big italic word in her words.
- Don't hard-cut between beats, float or breathe anything, put text on her face, or add music.
