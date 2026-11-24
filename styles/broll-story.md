# B-roll story (inspired by Nana Del Rey)

**What it is:** a soft, cinematic reel that's mostly B-roll of her life and work, with her voice over the top.
Small lowercase subtitles hop across the bottom, and only two or three times giant words build up on screen in
butter and lilac as she says them. Her face appears two or three times, never for long.
**Needs:** her voice take PLUS 3-6 short clips from her camera roll of her doing things (working, walking, the
view, her pet, her desk). No B-roll = use Clean or Minimal instead; ask her to AirDrop a few clips.
**Inspired by** Nana's editing technique only: never her footage or phrases.
**Read first:** `references/editing-craft.md`. Fonts: `InterTight-ExtraBold.ttf`, `InterTight-Regular.ttf`.

## 1. Plan the shots (write it down before building)
Keep ONE shot for the whole spoken hook: open on her face OR straight on B-roll, but don't cut inside the hook
(the giant words do the work there). After the hook, match each line she says to the clip that SHOWS it ("thousands of ideas" -> typing; "stuck" -> the laptop shut,
the cat asleep; "anything is possible" -> the plane wing). Open on B-roll or on her face for the first half-line,
and cut to B-roll ON the key word. Her face only where she speaks straight to camera. Clips must be in
`~/Movies` (copy them in, convert HDR to SDR with `scripts/hdr_to_sdr.sh` if they came from an iPhone).

## 2. Build in Edits
1. `addMedia` the take -> rough cut (editing-craft) -> **`generateCaptions` now, before any B-roll split** (check
   the rough-cut joins for doubled words).
2. `extractAudio` on EACH main-track piece left after the rough cut (one call per piece). Each extracted voice
   clip matches its piece exactly (same cut points and speed); extracting from an uncut clip copies the WHOLE
   original file and goes out of sync. Check in `elements` (`clips` doesn't list audio) that the voice clips end
   where the video ends.
3. `splitAt` at every shot change -> `replaceElementMedia` each B-roll piece with its clip (keeps the timing)
   -> `setVolume` 0 on EVERY video piece (her voice plays from the extracted track).
4. **Subtitles:** `splitCaption` into 1-4 word chunks (splits snap to real word gaps, which also tells you exact
   word times) -> `setCaptionStyle` "Simple V0" -> `editCaption` to lowercase -> on each: `setTextFont`
   `InterTight-Regular`, `setTextStyle` size 56 white, `setEmphasis` outline `#000000CC` (readable on bright
   B-roll), `setTextPosition` y 0.85 with x cycling 0.27 / 0.5 / 0.72. Lowercase everything, acronyms too
   ("ai", "adhd"). Keep chunks to 1-3 words so the side slots never run off the edge; on a very bright patch move
   that chunk to the centre slot.
5. **Giant words (2-3 moments only: the opening line and the closing line):** `scripts/word_stacks.py` kind
   `broll-story`, one line per spoken chunk ("moves" / "as fast as our" / "brain"). It saves build frames
   (-1, -2, -3). `addOverlay` each frame back to back, starting on the word that line starts on, x ~0.5,
   y 0.22-0.30, scale ~0.82-0.86, `trim` each to the next word. Then check every frame's start and end in `elements`: Edits snaps to whole frames,
   so make each frame end exactly where the next starts (no one-frame gap = no flicker). Hide the subtitles underneath (`setTextStyle`
   size 1 on those captions).
6. **Music:** `listMusicTracks` (query e.g. "soft lofi", license royaltyFree) -> `seek` 0 ->
   `addSongToComposition` -> `setVolume` ~0.18. The song comes in at the take's ORIGINAL length: `trim` its right
   side so it ends with the reel.
7. **Grade:** `addAdjustmentLayer` + `applyAdjust` temperature +7, highlights -12, saturation -6. No transitions, no sound effects.

## Check
Next to a real Nana reel (e.g. instagram.com/reel/DflIEOYqWHx): mostly B-roll; small subtitles you can still read; giant words only
2-3 times and never with subtitles under them; cuts land on words; music under, not over, her voice.
