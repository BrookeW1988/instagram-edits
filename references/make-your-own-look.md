# Make a new look from her own reels

Trigger: she drops in links to (or files of) about three reels and says something like "analyse my editing style
frame by frame and save it as a new look".

**Whose reels?** Best is her own. If they're someone else's, copy TECHNIQUES only (sizes, positions, pacing, caption
behaviour, grade, sound density). Never their footage, logos, wordmarks, catchphrases or on-screen lines, and say so
in the look file. Never download or keep their videos longer than the analysis needs.

## 1. Get the reels onto the Mac
- Files she already has (AirDropped, saved from the Instagram app, screen recorded) are easiest. Ask for those first.
- Links: try `yt-dlp` (free downloader). If it isn't installed, ASK before running `brew install yt-dlp`. Instagram
  often blocks downloads without a login; if it fails, don't fight it, ask her to save the reels from the app or
  screen record them on her phone and AirDrop them over.
- Work in a temporary folder: `mktemp -d`. Delete it at the end.

## 2. Measure (ffmpeg + your eyes)
For each reel:
- Basics: `ffprobe` for length, size, fps.
- Cuts: `ffmpeg -i reel.mp4 -vf "select='gt(scene,0.3)',showinfo" -f null -` and count the cut times. Report cuts
  per minute and the average shot length.
- Frames: a contact sheet at 2 fps for the first 6 s (the hook) and 1 fps for the rest:
  `ffmpeg -i reel.mp4 -vf "fps=1,scale=270:-1,tile=6x5" sheet.jpg`. Look at every sheet.
- Full-size stills at 3-5 key moments to measure text: the y position of the hook and captions as a fraction of the
  height, text height in px on a 1080x1920 frame, box or no box, outline, shadow, case, words per caption,
  highlight colour on the spoken word.
- Colours: sample hex values from the stills (text, boxes, accent).
- Fonts: describe the letter shapes and name the closest FREE Google Font. Say it's a match by eye, not the real font.
- Zooms and movement: punch-ins (hard or slow), how often, how far. Split screens, cut-outs, text behind the head.
- Grade: warm/cool, contrast, saturation, filmic or clean.
- Sound: music or not, sound effects per 10 s, what kind. (You can't hear; use `ffmpeg -af astats` / loudness and
  ask her what she hears if it matters.)
- Pacing: speech speed (words per minute if there's speech), dead air left in or cut.

Only write what you measured or clearly saw. Mark guesses as "est.".

## 3. Write the look file
Save it as `my-looks/<short-name>.md` in this skill folder (create the folder if needed). Use the same sections as
the files in `styles/` so the build steps can follow it:
- Title + one line ("Looks like...") + "Inspired by" (her own reels, or the creator's techniques only)
- **Use for** and **Needs**
- **Look table** (1080x1920 sizes): hook font/size/box/position, captions, palette, cards, GIFs, zooms, grade,
  pacing, sound
- **What Edits can do natively** vs **what needs a PNG overlay** (a soft shadow, tight letter-spacing, square
  boxes or a screenshot inside a card all need a PNG: adapt `scripts/word_stacks.py` / `scripts/show_it_cards.py`)
- **Footage it needs** (any take? a take that names things? B-roll?) so Claude knows when it fits
- **Hook formulas** (3, in her voice, never someone else's catchphrases)
- **Recipe** (numbered build steps)
- **Do / don't**

Use her brand colours from `profile.md` where the reels use them; otherwise keep the measured colours.

## 4. Prove it, then show her
Build one test reel in the look, export it, and put `scripts/contact_sheet.sh` of the export next to a contact
sheet of her reference reel. Fix whatever doesn't match (caption size is the usual miss), following
`references/editing-craft.md`. Then summarise the look in plain words (5-6 lines) and show her the test. From then on,
"edit this in the <short-name> look" uses `my-looks/<short-name>.md` exactly like a built-in recipe.
