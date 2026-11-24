# B-roll story (inspired by Nana Del Rey)

**What it is:** a soft, cinematic reel that's mostly B-roll of her life and work, with her voice over the top.
Small lowercase subtitles hop across the bottom, and only two or three times giant words build up on screen in
butter and lilac as she says them. Her face appears two or three times, never for long.
**Needs:** her voice take PLUS 3-6 short clips from her camera roll of her doing things (working, walking, the
view, her pet, her desk). No B-roll = use Clean or Minimal instead; ask her to AirDrop a few clips.
**Inspired by** Nana's editing technique only: never her footage or phrases.
**Read first:** `references/editing-craft.md`. Fonts: `InterTight-ExtraBold.ttf`, `InterTight-Regular.ttf`.

## 1. Plan the shots (write it down before building)
Match each line she says to the clip that SHOWS it ("thousands of ideas" -> typing; "stuck" -> the laptop shut,
the cat asleep; "anything is possible" -> the plane wing). Open on B-roll or on her face for the first half-line,
then cut to B-roll ON the key word. Her face only where she speaks straight to camera. Clips must be in
`~/Movies` (copy them in, convert HDR to SDR with `scripts/hdr_to_sdr.sh` if they came from an iPhone).

## 2. Build in Edits
1. `addMedia` the take -> rough cut (editing-craft) -> **`generateCaptions` now, before any B-roll split** (check
   the rough-cut joins for doubled words).
2. `extractAudio` on the take (her voice moves to its own track, so the video can be swapped).
3. `splitAt` at every shot change -> `replaceElementMedia` each B-roll piece with its clip (keeps the timing)
   -> `setVolume` 0 on EVERY video piece (her voice plays from the extracted track).
4. **Subtitles:** `splitCaption` into 1-4 word chunks (splits snap to real word gaps, which also tells you exact
   word times) -> `setCaptionStyle` "Simple V0" -> `editCaption` to lowercase -> on each: `setTextFont`
   `InterTight-Regular`, `setTextStyle` size 54 white, `setEmphasis` outline `#00000080` (keeps it readable on
   bright B-roll), `setTextPosition` y 0.88 with x cycling 0.22 / 0.5 / 0.78.
5. **Giant words (2-3 moments only: the opening line and the closing line):** `scripts/word_stacks.py` kind
   `broll-story`, one line per spoken chunk ("moves" / "as fast as our" / "brain"). It saves build frames
   (-1, -2, -3). `addOverlay` each frame back to back, starting on the word that line starts on, x ~0.5,
   y 0.22-0.30, scale ~0.82-0.86, `trim` each to the next word. Hide the subtitles underneath (`setTextStyle`
   size 1 on those captions).
6. **Music:** `listMusicTracks` (query e.g. "soft lofi", license royaltyFree) -> `seek` 0 ->
   `addSongToComposition` -> `setVolume` ~0.18.
7. **Grade:** `addAdjustmentLayer` + `applyAdjust` temperature +7, highlights -12, saturation -6. No transitions, no sound effects.

## Check
Next to a real Nana reel (e.g. instagram.com/reel/DflIEOYqWHx): mostly B-roll; small subtitles you can still read; giant words only
2-3 times and never with subtitles under them; cuts land on words; music under, not over, her voice.
