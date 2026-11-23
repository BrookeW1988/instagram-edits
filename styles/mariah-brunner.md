# Quick recipe: Mariah Brunner ("Receipts Round Your Head")

**Looks like:** she stays on screen talking like she's on FaceTime with a friend, while the receipts pop in around her
head on the exact word: a real logo, real screenshots, a reaction GIF, butter-yellow keywords and a numbered card.
One-word captions under the chin.
**Inspired by:** [Mariah Brunner](https://www.instagram.com/itsmariahbrunner/) (editing techniques only: none of her
footage, logos, captions, catchphrases or sign-offs). Every number: `LOOKS/looks/mariah-brunner/SPEC.md`.
**Use for:** tool tips, "I tried this" reels, anything with things to show. Effort: medium (mostly gathering receipts).
**Needs:** one talking-head take + her real logos and screenshots of what she names + about one reaction GIF per 10 s
(her own files or the free editing pack). Length 15-25 s.

## Look (sizes on a 1080x1920 frame)
| | Spec |
|---|---|
| Hook | Inter Black 86 px, Title Case, 3 lines (two butter `#F8F098`, one white), ink outline, no box, left-aligned above her head (x ~72, top y ~250). On from frame 0, gone at ~2 s ([Google Fonts](https://fonts.google.com/specimen/Inter)) |
| Receipts | Above her head on a close-up (y ~200-560): her logo on the tool's name; screenshot cards ~500-600 px wide in a white 4 px frame with a soft shadow; a reaction GIF ~560 px wide for ~3 s. One at a time, in on the word |
| Keywords | 1-2 keyword stacks: butter hero words (118-142 px) + white small words (70-78 px), Inter Black, ink outline, word by word, plus one 3D emoji (her files or the free editing pack) |
| Numbered card | `make_text_card.py number` with a butter badge, on the number she says, ~1.2 s |
| Captions | ONE word at a time, Inter ExtraBold 80 px, white, soft shadow, no box, lower case as spoken, centred at y ~1545. Quick pop in (86% -> 100%) |
| Zooms | Hard punch-in to 110% on the punchline, back to 100% after; 107% on a jump cut. No slow zooms |
| Palette | Butter `#F8F098` (or her brand accent), white, ink `#0C0C0E` (outlines, card text) |
| Grade | Warm and healthy: a touch of warmth, contrast +4, a little more vibrance. No filters, no vignette |
| Pacing | 1.1x; something new every 1.7-3 s, plain face holds in between |
| Sound | One tactile sound per landing, 6-10 dB under the voice: pop (logo, number card), paper slide (screenshots), mouse click (keyword taps), bubble pop (emoji), thud (GIF). ONE swipe in the whole reel. No music |

## Hook formulas
- "I Tried [Tool] / For A Week / Here's What Happened"
- "The [Tool] Feature / Nobody's Using / Yet"
- "Stop Paying For / [Thing] When / [Tool] Does It"

## Presets to save in Edits
- Text: **Receipt hook**, **Receipt keyword** (Inter Black, butter, ink outline). Captions: **One-word pop**.

## Recipe
1. `frameSheet` her take first to find her face box. Nothing ever goes in it.
2. Cut whole sentences, breaths only where really silent, `setSpeed` 1.1.
3. Hook and keywords: Edits text from the closest preset in `listTextPresets` with an outline (or a strong shadow)
   and no box, Inter Black, with the closest pop-in from Edits' text animations. Keywords land word by word.
4. Receipts: copy her files into `~/Movies/Edits-assets/<reel>/`, `addOverlay` each above her head on its word
   (y ~0.2, scale 0.45-0.55), `trim` so only one is up at a time. Real files only.
5. Numbered card: `make_text_card.py number --num ... --label "..." --accent "#F8F098"` on the spoken number.
6. Captions: `generateCaptions`, a style that shows one word at a time if `listCaptionStyles` has one (otherwise the
   shortest), `setTextFont` Inter ExtraBold, `setTextPosition` y ~0.8.
7. Punch-ins with `splitAt` + `setTransform`; a sound on every landing (`searchSoundEffects` + `addSoundEffect`).
8. Tell her in one line what was swapped: the yellow highlighter sweeping across screenshot rows (use a callout from
   her files or the free pack, or leave it out) and the number counting up.

## Do / don't
- Do keep every receipt real: her captures or a public page, pixels never edited. No mocked-up UI or invented numbers.
- Don't cover her face, take over the full screen, add music, or put the same sound twice in a row.
