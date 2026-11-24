# Editing craft: think like an editor, then do it in Edits (read before every edit)

This is the editor's brain behind every edit, styled or not. It's distilled from the rules in Brooke's whole
library of editing skills (rough cuts, talking heads, shorts, clipping, captions, B-roll, sound) and from what she
approved or rejected in real edits. The style recipes in `styles/` say WHAT a look puts where. This file says HOW
a good editor decides, in what order, and what to check. `edits-equivalents.md` says which Edits tools do each move.

## The order (never skip a step, never change the order)
1. **Watch it** (read every word).
2. **Write the edit plan** and show it to her (below).
3. **Rough cut** in Edits.
4. **Captions** (straight after the rough cut, before any other split).
5. **Pacing pass:** punch-ins, cutaways, B-roll, on the plan's times.
6. **Graphics** (only what the style uses), each landing on its word.
7. **Sound and grade.**
8. **Check the EXPORT**, fix, re-export, check again.

## 1. Watch it
- `transcribeClip` and read the WHOLE transcript before deciding anything.
- Find two lines: the **payoff** (the line the reel exists for) and the **hook** (the line that makes someone
  want the payoff). The hook must be in the first 2 seconds; the payoff sits late; end the moment it lands.
- Note every thing she NAMES (a tool, a file, a number, a place): each one is a chance to SHOW it instead of
  describing it. "When I say PDFs and slide decks it should show those things."
- Note every false start, repeat, "um", and any line that wanders off the hook-to-payoff thread.
- Pick the style from the footage (table in section 9).

## 2. The edit plan (write it, show her in plain English, then build)
A short timeline she can read, from the word times:
```
Hook (0-3.2s): "If I had to learn Claude in one day..."  -> text hook on, no cuts inside it
Cut: false start "Quest... ask" (9.9-12.1s), 3 long pauses
1.9s  "9am"        -> card: About Me doc (real Claude chat screen)
...
Punch-ins: 14.9s "11am" (1.08), 32.5s "3pm" (1.08)
Ends: 0.35s after "...without the overwhelm."
```
One line per moment: time, what she says, what happens on screen. Ask nothing unless something's missing
(B-roll, a screenshot only she has). Then build exactly that.

## 3. Rough cut
- **Always first.** An edit without a rough cut isn't an edit ("you didn't edit it... take out the dead space").
- Cut from the WORD times, not a silence detector (room noise hides dead space).
- **Cut:** false starts and restarts (keep the cleaner take), repeated sentences (keep the better one), the "um"
  before a sentence, any line off the hook-to-payoff thread, and silences BETWEEN sentences over ~0.35 s, cut down to
  ~0.15 s (leave 0.08 s after the last word, 0.07 s before the next).
- **Keep:** pauses INSIDE a sentence (emphasis is content), a beat after a big line or a number, natural breaths,
  her sign-off (never trim "make sure you save this..."), a pulled face or reaction.
- **Never:** a trim under 0.15 s (reads as a glitch), a cut inside a word or on a soft word ending ("credits"
  becoming "credit"), more than one cut inside a spoken list (play the list as one run).
- Before cutting a "repeat", check it really is one (a word split into two tokens looks like a stutter).
- **False starts:** keep the LAST clean go. Cut from the end of the last good word before the stumble to the start
  of the clean restart. If the transcript stretches a word over ~1 s ("ask" lasting 1 s), the stumble is inside
  it: cut to the start of the next word after it, then `captureFrame` and read the caption at that join to check.
- **Words closer than 0.15 s at a cut point:** move the cut to the nearest gap of 0.15 s or more, or skip that cut.
  After cutting, look for one-frame caption or sound fragments at each join and remove or merge them
  (`mergeCaptions`, `deleteSoundEffect`).
- Cut BEFORE an off-camera glance, not after. First word within 0.5 s of the start. End ~0.35 s after the last word
  (if the take ends sooner, leave it).
- Her spoken CTA with a keyword that isn't live: see SKILL.md section 0 (ask in the plan; otherwise cut the CTA
  line, keep the sign-off).
- Speed: only if she likes it (`profile.md`), 1.1-1.3x, never more.

## 4. Pacing
- **Something changes about every 2 seconds** on average: a cut, a punch-in, a card, a stack, a B-roll shot.
  Nothing on her face holds more than ~4 s without a change; no beat runs past 5 s. ("It's very SLOW, not enough beats.")
- **No cut, punch-in or layout change inside the spoken hook.** The first change comes after it.
- Changes land ON a word (the word that names the thing), never at a random time. Cut to B-roll on the key noun.
- Leave MORE room after a big line, not less.
- Her voice keeps running under graphics and B-roll (J and L cuts). Never a silent text block.
- Hard cuts only. **We don't use** Edits transitions, shakes, spins, glitches, zoom-bounces or vignettes.
- Never the same graphic or GIF twice in a row.
- End on the payoff, never a trail-off.

## 5. Punch-ins
- Standard punch-in: **1.06-1.10**, on real emphasis (a key word, a number, a turn like "But..."), or to break up
  more than ~3-4 s on her face. Clean uses a two-camera rhythm (1.00 / 1.18) and ONE 1.30 on the biggest line.
- Anchor on her chin so her face doesn't jump (`edits-equivalents.md`). Check her face and hands aren't cut off at
  the punched-in size; her phone footage goes soft above ~1.3x.
- When she pulls a face: punch in hard (1.3) and hold it.
- **Never:** constant zoom breathing, drift or tilt; a sound effect on a punch-in (Clean's single 1.30 whoosh is
  the one exception); more than one slow push-in per reel.

## 6. Captions and on-screen text
| Style | Font (pairing) | Size in Edits | Case | Position | Chunk |
|---|---|---|---|---|---|
| Clean | Montserrat Black | 84 | CAPS | y 0.77, centred | 2-3 words, spoken word in yellow |
| Show it | Inter ExtraBold | 100 | as spoken | y 0.75 | ONE word at a time |
| B-roll story | Inter Tight Regular | 54 | lowercase | y 0.88, x cycling 0.22 / 0.5 / 0.78 | 1-4 words |
| Minimal | Newsreader | default | as spoken | y 0.80 | one short line |

- Always set y with `setTextPosition` (Edits' default can land on her mouth). The table's y is a starting point:
  `captureFrame` one frame, find her chin, and put captions at chin + ~0.05 (between 0.72 and 0.88). Tight framing
  needs them lower. Never over her eyes or mouth, never
  behind her head, nothing in the bottom ~20% or right edge (Instagram's buttons).
- **Captions go on straight after the rough cut, BEFORE any other split.** Captions generated over a clip that's
  already in pieces double the words at every join ("Ask ask"). Read the caption at every rough-cut join and fix
  doubles with `editCaption`. Splits made after the captions exist don't touch them.
- Set fonts LAST: `setCaptionStyle`, `editCaption` AND `splitCaption` all reset font and size (a split piece comes
  back in the style's own font, e.g. ATP-PleasurizeRegular 144), so after ANY of them re-apply font, size and
  position to the captions it touched. The order is generate ->
  `splitCaption` -> style -> highlight colour -> edit text -> `setTextFont` + `setTextStyle` + `setTextPosition`.
- **Proofread every caption** against what she said: product names ("Claude" not "cloud"), times ("9am" not
  "9:00 a.m."), her name, doubled words.
- Hide captions under the hook, full-screen graphics and big word stacks (`setTextStyle` size 1).
- **Text hook:** 2 lines (3 max), 5-9 words, readable in under a second, top of frame, held through the spoken
  hook. Don't restate the spoken line word for word; it can be bolder than the line ("don't stress about hooks
  overpromising: they're meant to stop the scroll"), but the reel must deliver it.
- Other on-screen text only earns its place for the hook, facts (prices, dates, numbers), the CTA, or a word
  stack the style uses. If it just repeats what she said, cut it.
- A number lands as the word ENDS (+0.1 s), not as it starts.

## 7. Graphics, proof, B-roll
- **Show, don't describe.** A card or B-roll shot shows the actual thing she names: her screenshot, the official
  image from the maker's own site (`scripts/grab_page_images.py`), or her own footage. Never an empty styled box,
  a mock-up, invented replies or AI people.
- **The screen must show THAT thing, not something nearby.** "Connect your apps like Gmail" needs a connectors
  screen with Gmail on it, not any Claude screen and never a pricing page. If no image you can find shows it, ask
  her for a screenshot in the plan, or swap that beat for a word stack. A loosely related screen is worse than none.
- Lists: one visual per spoken item, landing on its word.
- One new element at a time. Proof shows before or as the claim is spoken.
- Holds: cards and screenshots ~2-3 s; full-screen beats 2-3 s max; GIFs 1.2-2 s; graphics on screen less than
  half the reel. Claims, numbers and proof get graphics; stories and promises stay on her face.
- B-roll matches the meaning of the line (good examples under praise, bad under criticism), changes on the noun,
  and goes back to her face between ideas. No slivers of face (under ~1 s) between two cutaways.
- **Never use Edits' subject cut-out (`addStickerFromCutout`) on talking-head footage**: it's one still frame of
  her, so it ghosts the moment she moves.

## 8. Sound and look
- Sound effects: one per visible event (a card landing, a split opening), aligned to the moment it lands.
  Tactile clicks and pops (lip pop, page flip, paper), never notification blips or dull whooshes. At least ~1 s
  apart (pops ~3 s). Volume 0.3-0.35. Never on captions, punch-ins or the comment keyword. Pause playback before
  adding one (sounds added while it plays land ~0.5 s late).
- Music: none by default (Clean, Show it). B-roll story and Minimal get a soft royalty-free bed from Edits'
  library at ~0.15-0.2, under her voice, never over it.
- Loudness: about -14 LUFS for the whole reel (`scripts/level_voice.sh` on the take first).
- **Grade** = `addAdjustmentLayer` (the first one covers the whole reel) then `applyAdjust` per slider. Gentle.
- Fonts: one pairing per style (table above), never more than two fonts. Colours: two plus white. Light text on
  a light wall needs a soft shadow (the stack PNGs have one) or a faint outline (`setEmphasis` outline `#00000080`).

## 9. Which style fits which footage
| She filmed... | Style |
|---|---|
| Any talking-head take, nothing else | **Clean** (or just the editor pass: rough cut, punch-ins, captions) |
| A take where she NAMES things (tools, steps, "5 things...") | **Show it** |
| A voice take + 3-6 clips of her doing things | **B-roll story** |
| A calm, considered take (story, reflection, premium offer) | **Minimal** |

## 10. The check (on the exported file)
Export, then `bash scripts/contact_sheet.sh <file>` (40 frames across the whole reel). Look at it next to the
style's description in its recipe (and the creator's real reel if the recipe links one and you can open it). Then go
through this list out loud and fix anything that fails (three passes at most, then tell her what's left):
- [ ] Hook readable in frame 1, clear of her face; no cut inside the spoken hook.
- [ ] Every caption readable at phone size, spelled right, not over her eyes or mouth, no doubled words.
- [ ] Nothing clipped at any edge; nothing in the bottom 20% / right-edge button zone.
- [ ] Something changes about every 2 s; nothing on her face over ~4 s without a change.
- [ ] Every card or cutaway shows the REAL thing, landing on its word.
- [ ] No orphan words (a lone "a" or "the" left on screen with nothing after it; one-word-at-a-time caption
  styles are fine), no trims under 0.15 s, sign-off intact.
- [ ] No ghosting, no frozen cut-outs, no transitions or shakes.
- [ ] Length matches what the plan expected (rough cut removed what it said it would).
- [ ] Sound: you can't hear it, so ask her to listen to the music level and the pops on her phone speaker.
