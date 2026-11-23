# Premium build: the template's motion graphics, rendered, then dropped into Edits

The quick route builds everything with Edits' own tools. The premium route renders the look's motion graphics
(typed-on hooks, words behind the head, proof cards flying in, counting numbers) as ONE see-through video with
HyperFrames, and drops it on top of her take in Edits. Edits keeps the transparency, so she can still move
captions, swap things and Share from Edits.

## Is it available?
Check, and only offer premium if all of these are true (otherwise use the quick route and say why in one line):
- `node -v` is 22 or newer (HyperFrames needs it). Not installed? Offer: "Premium needs Node.js. Want me to install it
  with Homebrew (`brew install node`)?" Ask first.
- `npx --yes hyperframes@0.9.83 --help` runs (first run downloads it; ask before that download).
- `ffmpeg` is installed.
- The skill's Python toolbox has the premium extras: `bash scripts/setup_python.sh --premium` (ask first; it
  downloads a speech model the first time it transcribes).

## Steps
1. **Footage.** Her take in `~/Movies/Edits-inbox/`, already SDR (`scripts/hdr_to_sdr.sh`) and levelled
   (`scripts/level_voice.sh`).
2. **Working copy.** Copy `templates/<slug>/` to `~/Movies/Edits-builds/<YYYY-MM-DD>-<slug>-<topic>/` AND copy
   `templates/_shared/` to `~/Movies/Edits-builds/_shared/` (several templates import `../_shared/reeltools.py`).
   Keep builds out of the skill folder (they're big, and updates would clash with them).
3. **Read the template.** Its `SPEC.md` (the "Using this template" block, "How a member's version differs", every
   number) and the usage notes at the top of its `cut.py` and `build.py`. The commands and config file differ per
   template. Templates were first written for one demo take, so Claude adapts the example values to her take.
4. **Fonts.** `bash scripts/get_fonts.sh <slug> <build folder>`.
5. **Brand.** Where build.py has a `BRAND` block, fill it from `profile.md` (ink, accent, light, fonts).
6. **Rough cut + words.** Run the template's cut step with `~/.instagram-edits/venv/bin/python`. Some templates read
   a words file made by a one-line mlx_whisper command in their SPEC/docstring. Proofread every word (brand names,
   "Claude"/"cloud", her name and business).
7. **Config.** Fill the template's config with THIS reel's hook, cards, labels and proof. Real things only: her real
   screenshots, real logos, real numbers she says, her own words. Proof = HER screenshots (ask for them); blur other
   people's names and faces unless they agreed. Comment-keyword CTA only if `profile.md` lists that live keyword.
8. **Build + check.** Run the build, then `npx --yes hyperframes@0.9.83 check --json`, look at snapshots of the key
   moments, fix, repeat. Missing sounds and images are skipped with a note; that's expected.
9. **Render the overlay.** Run the template's overlay build, then `bash scripts/prep_overlay.sh <build folder>
   <overlay folder name>` (fills in any missing project files), then the template's render command with
   `--format mov` (ProRes 4444 with alpha). Use `--workers 2` so the Mac stays usable.
10. **Into Edits.** Copy the cut base clip (the template's `assets/cut.mp4` or equivalent) and the overlay .mov to
    `~/Movies/Edits-assets/<reel>/`. In Edits: SDR, 9:16, 30 fps. Import the cut base clip as the main clip at 0 s
    (no trims or speed changes: the cut already did that). `addOverlay` the .mov at 0 s, x 0.5, y 0.5, scale 1.0.
    Then do the look's camera moves natively (punch-ins with `splitAt` + `setTransform`; see the SPEC). Never zoom the
    main clip while a person cut-out is on screen in the overlay. Don't `generateCaptions` if the overlay has captions.
11. **Sound.** Sounds aren't shipped with the templates. Either she adds her own files to the build's `assets/sfx/`
    (named as the SPEC says) before rendering, or you add them natively in Edits with `searchSoundEffects` +
    `addSoundEffect` at the SPEC's moments. Music: she adds it in the Edits window.
12. **Check** with `frameSheet` at the SPEC's key moments, then hand over (SKILL.md section 9).

## Rendering takes a while
A 15-30 s reel takes a few minutes to render. Tell her before you start, and don't run two renders at once.
