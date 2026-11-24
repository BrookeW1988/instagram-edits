# Minimal (calm luxury)

**What it is:** her face (or her calm B-roll) held still, one small serif caption line, a warm grade, and nothing
else. The restraint IS the look: no punch-ins, no cards, no sound effects.
**Needs:** a calm take (a story, a reflection, a premium offer). Optional: a few slow B-roll clips (then build it
like B-roll story steps 1-3, without the giant words).
**Read first:** `references/editing-craft.md`. Font: `Newsreader-Regular.ttf` (Edits calls it
`Newsreader16pt16pt-Regular`).

## Build (after the rough cut; keep more breathing room than usual: pauses down to ~0.3 s, not 0.15 s)
1. **Captions:** `generateCaptions` -> `setCaptionStyle` "Simple V0" (one short line, hard on/off) -> fix text with
   `editCaption` -> `setTextFont` `Newsreader16pt16pt-Regular` on every caption, default size, white,
   `setTextPosition` y 0.80. No box, no highlight.
2. **Frame:** locked. No punch-ins, no transitions.
3. **Music (optional):** a soft royalty-free piano or ambient track from Edits' library at ~0.15.
4. **Grade:** `addAdjustmentLayer` + `applyAdjust` temperature +10, exposure -3, tint -3.

## Check
One line of small serif text at a time, never over her mouth; nothing else moves; the reel feels slow on purpose.
