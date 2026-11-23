# Quick recipe: Diary of a CEO ("Podcast clip")

**Looks like:** a dark, moody podcast clip. The hook is on screen from the first frame in white caps on black boxes,
short captions sit under the chin, a profile card says who she is, three crops from one camera hide every cut, and the
last line turns black and white.
**Inspired by:** [The Diary of a CEO](https://www.instagram.com/thediaryofaceo/) (editing techniques only: no footage,
logo, end card, ID-card art or hook wording). Every number: `LOOKS/looks/diary-of-a-ceo/SPEC.md`.
**Use for:** a strong opinion or a story from a podcast, interview, live or seated take. Effort: medium.
**Needs:** one talking-head take with a 2 s closed-mouth "listening" moment in it, plus her own photo. Length 20-40 s.

## Look (sizes on a 1080x1920 frame)
| | Spec |
|---|---|
| Hook | Inter Black ~60 px, CAPS, white `#FCFCFC` on black boxes (PNG), 2 lines of 3-6 words, top at y ~292. On from frame 0, no entrance, gone on a hard cut at ~2.2 s ([Google Fonts](https://fonts.google.com/specimen/Inter)) |
| Name label | Inter Bold 38 px, amber `#F2B840` on a black box (PNG), her real name, at y ~548 under the hook, same timing |
| Hook frame | Optional, 0-2.2 s: split screen side by side, her speaking on the left, the listening moment on the right |
| Captions | Inter Bold 66 px, white, soft shadow, no box, 1-3 words, as spoken, no end punctuation, centred at y ~1545. Hard switch, no animation, never on screen with the hook |
| Profile card | At 21-33% of the reel, ~3 s: her own photo (~80% frame width, centred) + a label with her real name and one real fact. Hard in and out on a join |
| Crops | One camera, three crops: W 100%, M 120%, T 130%. Switch on every join (it hides the jump cut). Never M straight to T. Shots 1.7-3.9 s |
| B&W beat | From a word in the last line to the end: black and white |
| Palette | Black, white, amber `#F2B840` (name label only) |
| Grade | Dark and moody: exposure down, contrast up, highlights and shadows well down, saturation down a touch, a light vignette if Edits' filters have one |
| Pacing | 1.1x. Keep tiny ~0.1 s breaths (one camera can't hide micro jump cuts). Drop list signposts ("number two is") |
| Sound | Nothing on cuts. Profile card only: a paper slide as the photo lands, rubber stamps on the label (`searchSoundEffects`: "paper slide", "stamp"), 6-10 dB under the voice. No music |

## Hook formulas (from her first sentence: a claim, a "how" or a question)
- "NOBODY TALKS ABOUT / THIS PART"
- "HOW I [RESULT] / WITHOUT [THING]"
- "IS [BELIEF] / ACTUALLY WRONG?"

## Presets to save in Edits
- Text: **Podcast hook**, **Name label** (PNGs). Captions: **Podcast caption** (Inter Bold, white, hard switch).

## Recipe
1. Cut one self-contained stretch, drop list signposts, `setSpeed` 1.1. Find the 2 s listening moment.
2. Hook: `make_text_card.py hook --lines "..." "..." --box "#000000" --ink "#FCFCFC" --size 60 --font <Inter Black
   file>`; name label the same way with `--ink "#F2B840" --size 38`. `addOverlay` both at 0 s, `trim` to ~2.2 s.
3. Hook frame: Edits split screen with her speaking piece and the listening piece side by side. If it only stacks
   top and bottom, skip it and open full frame.
4. Captions from 2.2 s: `generateCaptions`, plainest style in `listCaptionStyles`, `setTextFont` Inter Bold,
   `setTextPosition` y ~0.8.
5. Crops: `splitAt` on every join, `setTransform` 1.0 / 1.2 / 1.3 in turn, never 1.2 straight to 1.3.
6. Profile card: her photo + a label PNG (`make_text_card.py hook`), `addOverlay` at 21-33%, sounds on the landings.
7. B&W: `splitAt` on a word in the last line, a black-and-white filter on the last piece (a short dissolve
   transition between the two if Edits has one, otherwise a straight switch).
8. Tell her in one line what was swapped: the red hook word and red caption words, the dossier-style card (now her
   photo and a label) and the slow fade into black and white.

## Do / don't
- Do use only real facts on the profile card: no invented titles, numbers or awards.
- Don't animate the hook in, show a caption with the hook, put sounds on cuts, creep a zoom or brighten the grade.
