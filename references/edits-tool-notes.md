# Edits automation tools: what we've learned (read before building)

Edits for Mac's automation server is young and changes about weekly. These notes come from real test sessions
(Edits build 456, November 2026). If something here stops being true, say so plainly and write the new
behaviour into the "Notes from my sessions" section of `profile.md`.

## Connecting
- The server name in Edits' copied command is `metapilot-native`, so tools show up as `mcp__metapilot-native__*`.
  Community docs call it `edits`. Don't rely on the name: look for tools like `addMedia`, `generateCaptions`,
  `export`, and count them.
- **About 32 tools** = Edits was on its home screen when the chat started. **About 270** = a project was open.
  The list never refreshes by itself: open a project in Edits, then start a NEW chat.
- The copied command contains a private access token. Never repeat it back, never write it into a file, never
  run `claude mcp get` (it can print the token). If she's screen recording, the Settings > Automation screen must
  stay out of shot, and she should press **Regenerate access token** afterwards.
- Meta can switch the server off remotely. If every tool errors, tell her; don't guess.

## Projects and files
- `newProject` while another project is open can return an ERROR ("created but the editor did not open it") even
  though the new empty project IS open. Check with `title` + `clips` before retrying. Save the old project first.
- `setTitle` renames the open project.
- Files must be inside `~/Movies` (Edits is sandboxed). Use FULL paths (`/Users/<name>/Movies/...`), never `~`.
  Run `echo $HOME` once to get the real path.
- A new project starts in **HDR (hlg), 1440x2560, 60 fps**. Set SDR first with `setProjectDynamicRange`.
  `setCanvas` takes aspect "9:16" + frameRate 30 in one call. The canvas stays 1440x2560; that's fine, the export
  is 1080x1920.
- `addMedia` puts the main clip at 0 s in an empty project. `seek` wants `seconds`, not `time`.
- `appState` returns ~60 KB of text. For quick checks use `title`, `clips` or `tracks` instead.

## Cutting
- `transcribeClip` returns a job id: call `jobStatus` straight away.
- `transcriptJumpCut` is NOT in build 456. Use `transcribeClip` + `findPauses`, then `splitAt` + `selectById` +
  `delete` (deleting ripples the main track closed).
- `setSpeed` 1.3 works. After a trim and a speed change, timeline time = (source seconds - trim in) / speed.
- Keep complete thoughts. No micro-trims under 0.15 s, and at most one cut per spoken list item (choppy cuts annoy
  viewers more than a breath does).

## Voice level (do this BEFORE cutting)
- Phone takes often come in around -22 LUFS. Do NOT use Edits' `processAudio` normalize: it's plain gain (peaks
  went to +5 dBFS, which crackles) and its `add` mode drops a new clip on the main track and ripples everything.
- Run `scripts/level_voice.sh` on the take first and import the `-levelled.mp4` it makes. Result in testing:
  -14.0 to -14.5 LUFS.
- Already built the edit on the un-levelled file? `replaceElementMedia` on each piece keeps position, speed and
  zoom but resets the source in-point to 0, so follow it with `slipClip` by the old `sourceInPoint`.
- Edits' `loudness` sample peak reads ~3 dB hotter than ffmpeg's true peak on the same audio. Don't trust it alone.

## Captions
- `generateCaptions` makes long phrases (up to 16 words) but most styles show 3-4 words at a time.
- `listCaptionStyles` returns 73 names, but only 39 are caption styles; the other 34 are text presets.
- A good base for a "pop" caption: **Word Highlight Box 2** + `setCaptionHighlightColor` (brand accent), then per
  caption `setTextFont` (brand font, by its PostScript name) and `setTextPosition` y ~0.86 (the default y ~0.73
  sits on the mouth). `captions` output is huge (~40 KB): call it once.
- Remove captions under the text hook: select them + `delete`.
- Proofread EVERY caption. Common mishears: "Claude" -> "cloud", "ChatGPT", product and brand names, her own
  name and business name. Fix with `editCaption`.
- Named caption/text presets could not be saved through the tools (no tool for it). Re-apply the settings each reel.

## Text, cards, GIFs
- Text has NO background-box setting in the tools. Boxed hooks and number cards are PNGs drawn with
  `scripts/make_text_card.py`, added with `addOverlay`. `scale` = fraction of the canvas width. Hook: y 0.14,
  scale ~0.8.
- Photos default to 3 s on the timeline; change with `trim` (a negative delta lengthens).
- GIFs: there's no GIF/sticker search. `addGif` / `addSticker` only take a file path. Use .mp4/.gif files she
  has (or the free editing pack) through `addOverlay` (y 0.15, scale 0.44 wide / 0.3 square), then `trim` to the beat.
- No opacity or blur keyframes. Fades must be baked into the overlay file itself.

## Zooms
- Punch-ins: `splitAt` the main clip at a word gap, then `setTransform` scale 1.15-1.2 on that piece (a hard cut in).
- Never zoom the main clip while a person cut-out is on screen in an overlay (it ghosts).

## Sound
- `searchSoundEffects` works by keyword or category and returns up to 20 ids. Then `seek` + `addSoundEffect` by id,
  then `setVolume` 0.3-0.45. Claude can't hear: tell her to listen.
- Most "pop" results are notification blips. Prefer real-object sounds (a lip pop, paper, a pen) and never put a
  sound on top of a comment keyword.
- **Edits library MUSIC goes silent in Claude's exports.** Leave music for her to add in the Edits window and export
  or share from the window. Her own audio files export fine.
- Unknown: whether library SOUND EFFECTS survive a Claude export. Check the first export with her and note it.

## Overlays (the premium route)
- A ProRes 4444 .mov with alpha via `addOverlay` (x 0.5, y 0.5, scale 1.0) keeps full transparency in the preview
  AND the export, soft shadows included. It lands full frame.
- Edits plays the overlay clip's own audio, so sounds can be baked into the overlay .mov.
- Don't `generateCaptions` when the overlay already has captions.

## Checking
- `frameSheet` with empty id/path + a list of times = a contact sheet of the edit. Use it on every cut.
- `loudness` on a clip id works.
- Claude only sees still frames, not playback smoothness. Say so.

## Export
- `setExportSettings` is picky: `resolutionType` = `720p` / `HD` / `2K` / `4K` (HD = 1080x1920),
  `aspectRatio` = `nineBySixteen` (not "9:16"), `quality` high, frameRate 30, dynamicRange sdr. Leave any of the
  first three out and the export silently fails.
- `export` to a full path in `~/Movies` returns straight away. Poll `exportStatus` or wait for the file size to stop
  growing (~10 s for a 15 s reel). Output in testing: HEVC 1080x1920 30 fps SDR, exact length.
- From the Edits window, exports land in `~/Movies/Edits/Exports/`.

## Posting
- There is no share or post tool in build 456 (`shareToInstagram` is not exposed). She presses Share herself.
  If a share/post/delete tool ever appears, never call it without her yes for that exact reel.
