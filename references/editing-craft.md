# Editing craft: how to make a reel that's actually good (read before every edit)

This is the editor's brain behind all four styles. The recipes in `styles/` say WHAT goes where; this file says
HOW a good editor thinks, in what order, and what to check. Every rule here came from a real edit being rejected
or approved (24/11/2026).

## The order (never skip a step, never change the order)
1. **Watch it first.** Transcribe the take (`transcribeClip`). Read every word. Note: the hook line, each thing
   she names, the payoff line, the CTA, and every false start.
2. **Pick the style from the footage, not from taste.** The style has to fit what she filmed (table below). If
   the footage can't carry the style she asked for, say so in one line and suggest the one that fits, or tell her
   what to film / send.
3. **Rough cut** (inside Edits). Story first, polish later.
4. **Pacing pass.** Decide where something changes on screen.
5. **Captions.** Size, position, chunking and case for the style.
6. **Graphics.** Only what the style uses, each one timed to a spoken word.
7. **Sound and grade.** Quiet, and only where the style uses them.
8. **Check the EXPORT**, not the preview, against the real creator's frames. Fix, re-export, check again.

## Which style fits which footage
| She filmed... | Style | Why |
|---|---|---|
| Any talking-head take, no extra footage | **Clean** | Works on anything. Cuts, punch-ins and captions do the work. |
| A take where she NAMES things (tools, steps, features, "5 things...") | **Show it** | Every named thing gets its real screen. Nothing named = nothing to show. |
| A voice take + 3-6 clips of her doing things (camera roll) | **B-roll story** | The B-roll carries it. Without B-roll it's just a face with big words. |
| A calm, considered take (story, reflection, premium offer) | **Minimal** | One small serif line. The restraint is the look. |

## 1. Rough cut (in Edits)
- `transcribeClip` -> `jobStatus` gives every word with its start and end.
- **Cut:** false starts and restarts (keep the clean second go), repeated words, the "um" before a sentence,
  any pause over ~0.35 s (cut it down to ~0.15 s: leave 0.08 s after the last word, 0.07 s before the next).
- **Keep:** complete thoughts, natural breaths, a beat after a big line or a number.
- **Never** make a trim under 0.15 s (it reads as a glitch) or cut inside a word.
- Do it as: `splitAt` at every cut point (one call) -> `selectById` each dead piece (`addToSelection` true) ->
  `delete`. The main track closes the gaps by itself. Check `clips`: the new length should be the old length minus
  what you cut.
- Speed: only if `profile.md` says so (1.1-1.3x for fast talkers' content). `setSpeed` on every piece.
- **Captions go on straight after the rough cut, BEFORE any other split** (punch-ins, card in/outs, B-roll
  shots). Captions generated over a clip that's already in pieces double the words at every join ("Ask ask").
  The rough-cut joins themselves can do it too: after `generateCaptions`, read the caption at every join and fix
  doubles with `editCaption`. Splits made AFTER the captions exist don't touch them.

## 2. Pacing
- **Something must change every 2-4 seconds**: a cut, a punch-in, a card, a stack, a B-roll shot. Make a list of
  the change times before adding anything; any gap over 5 s needs something.
- Changes land **on a word** (the word that names the thing), never at a random time. Cut to B-roll ON the key word.
- The first 2 seconds carry the hook: text on screen from frame 1.
- **Cut grammar we use:** hard cut (jump cut), punch-in (a hard scale cut to 1.06-1.30 on the same shot),
  hard on / off text, hold, J/L cut (the voice carries over a cut). **We don't use** Edits transitions, shakes,
  spins, glitches or zoom effects: none of the creators we copy use them and they look cheap.

## 3. Captions (size is the most common failure)
| Style | Font (pairing) | Size in Edits | Case | Position | Chunk |
|---|---|---|---|---|---|
| Clean | Montserrat Black | 84 | CAPS | y 0.77, centred | 2-3 words, spoken word in yellow |
| Show it | Inter ExtraBold | 100 | as spoken | y 0.75 | ONE word at a time |
| B-roll story | Inter Tight Regular | 54 | lowercase | y 0.88, x cycling 0.22 / 0.5 / 0.78 | 1-4 words |
| Minimal | Newsreader | default | as spoken | y 0.80 | one short line |

Always set y with `setTextPosition` (Edits' default height changes with the style and can land on her mouth).

- Set fonts LAST: `setCaptionStyle` and `editCaption` both reset font and size, so the order is generate ->
  `splitCaption` -> style -> highlight colour -> edit text -> `setTextFont` + `setTextStyle` + `setTextPosition`
  on every caption.
- **Proofread every caption** against what she said: product names ("Claude" not "cloud"), times ("9am" not
  "9:00 a.m."), her name, doubled words at split points.
- Captions never cover her mouth or eyes. Check at phone size: if you have to squint, it's too small.
- To hide a caption under a big graphic: `setTextStyle` size 1. (A transparent colour doesn't work; deleting a
  caption can leave a ghost.)
- Edits keeps captions on the LOWEST overlay layer, so any overlay covers them. If a caption must sit on top of a
  screenshot, `moveToLayer` the screenshot to a free low layer and the caption to a layer above it.

## 4. Fonts and colour
- One pairing per style (table above), never more than two fonts in a reel. Pairings that work: one family in two
  extreme weights (Inter Tight ExtraBold + Regular), or a heavy sans with the same family's caption weight
  (Inter Black + Inter ExtraBold).
- Two colours plus white, max. Yellow `#F8F098` / lilac `#D5B8F6` / white for the soft styles; `#FFE600` for
  Clean. Her brand accent can replace the yellow or the lavender.
- **Grade** = `addAdjustmentLayer` (no start/length: the first one covers the whole reel) then `applyAdjust`
  with `{id, adjust, value}` once per slider (temperature, exposure, contrast, saturation, highlights, tint...).
- Light text on a light wall disappears: the stack PNGs carry a soft shadow; captions get an outline when the
  background is bright (`setEmphasis` outline `#00000080`).

## 5. Graphics
- **Real things only.** A card shows the actual screen of the thing she names: her own screenshot, or the
  official image from the maker's own site (`scripts/grab_page_images.py`), cropped to the app. Never an empty
  styled box, never a mock-up.
- One graphic at a time. Never over her face. Nothing in the bottom 20% or the right edge (Instagram's buttons).
- **Never use Edits' subject cut-out (`addStickerFromCutout`) on talking-head footage.** It makes ONE still frame
  of her head, so when she moves there's a frozen ghost head and chopped words behind it.
- No GIF unless it's a real reaction to a real line, in a white frame (`applyEffect video_plain_frame`), muted,
  1.5-2.5 s. When unsure, leave it out.

## 6. Sound and music
- Sound effects: tactile, real-object sounds (lip pop, page flip, paper), volume 0.3-0.35, on the frame the
  thing lands. One per landing, not one per word. Never notification blips. Pause playback before adding (sounds
  added while it plays land ~0.5 s late).
- Music: a royalty-free song from Edits' own library (`listMusicTracks` with `license` royaltyFree ->
  `addSongToComposition`), volume ~0.18 under her voice. It survives Claude's export (tested 24/11). Licensed
  (non-royalty-free) songs: she adds those in the Edits window herself.

## 7. The check (on the exported file)
Export, then `bash scripts/contact_sheet.sh <file>` (40 frames across the whole reel), and look at the sheet next
to the style's description in its recipe (and the creator's real reel if the recipe links one and you can open
it). Go through this list out loud and fix anything that fails:
- [ ] Hook readable in frame 1, clear of her face.
- [ ] Every caption readable at phone size, spelled right, not over her mouth or eyes.
- [ ] Nothing clipped at any edge; nothing in the bottom 20% / right-edge button zone.
- [ ] Something changes at least every 4 s.
- [ ] Every card shows a REAL screen, landed on the word.
- [ ] No orphan words (a lone "a" or "the" on screen).
- [ ] No ghosting, no frozen cut-outs, no transitions or shakes.
- [ ] Same structure as the style describes (and the creator's reel, if you could open it).
- [ ] Sound: tell her you can't hear, and ask her to listen to the music level and the pops.
