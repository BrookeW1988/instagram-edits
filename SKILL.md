---
name: instagram-edits
description: Edit your talking-head reels inside Instagram's Edits for Mac app with Claude, through Edits' built-in automation server. Gets your newest video from Downloads ready for Edits (copied to Movies, HDR switched to SDR), cuts pauses, adds captions, a boxed text hook, picture cards, GIFs, sound effects and zooms in one of 11 looks and 8 formats, writes your Instagram caption in your voice and copies it, and helps you post (you press Share, or export and publish with Blotato). Use when someone says "/instagram-edits", "edit this in Edits", "edit this in the <look> look", "now do it in the <look> look", "grab my newest video from Downloads and get it ready for Edits", "write my caption", "analyse my editing style and save it as a new look", or "publish this with Blotato".
---

# Instagram Edits (Edits for Mac + Claude)

You edit her reel in a real Edits project. She can tweak anything by hand afterwards, and she always presses the
last button. Talk in plain English: she's a business owner, not a video editor or a developer. Australian spelling.

**Paths in this file:** `SKILL_DIR` = the folder this SKILL.md is in. Scripts live in `SKILL_DIR/scripts/`.
`LOOKS` = the shared **Reel Looks** library (the 11 looks + 8 formats, also used by the Claude Video Editor):
`$REEL_LOOKS_DIR` if it's set, else `~/.agents/skills/reel-looks`, else `~/.claude/skills/reel-looks`. Its `index.json`
lists every look and format with the names people use; each one is a folder `LOOKS/looks/<slug>/` or
`LOOKS/formats/<slug>/` with `SPEC.md` (every number), `USE.md` (how this skill uses it) and the HyperFrames code.
**Missing?** Install it (README "For Claude or Codex doing the install", step 2) before section 4.

## What she might say (and where to go)

| She says | Do |
|---|---|
| "/instagram-edits" (first time ever) | Section 1 (setup), then 2, then ask which video and which look |
| "list the tools you have in Edits" | Section 2: count them and describe the groups in plain English |
| "grab my newest video from Downloads and get it ready for Edits" | Section 3 |
| "edit this in the Full look" / "use the Codie Sanchez look" / "/instagram-edits" | Sections 4-7 |
| "now do it in the pop-up proof look" | Section 4: rebuild from the SAME take in a NEW Edits project (keep the first one) |
| "analyse my editing style frame by frame and save it as a new look" (+ reel links) | `references/make-your-own-look.md` |
| "write my caption" | Section 10 |
| "export it" | Section 11 |
| "publish this to Instagram, TikTok and YouTube with Blotato" | Section 12 |
| "update my profile" / "change my colours" | Edit `SKILL_DIR/profile.md` with her |

## 0. Hard rules (never break these)

- **Never post, share, trial-post, schedule or delete** anything without her clear yes for that exact reel. That
  includes Blotato posts and deleting Edits projects. If a share or delete tool ever shows up in Edits, don't call it
  unless she says so for this reel.
- **Files must be inside `~/Movies`** (Edits is sandboxed and can't open Downloads or Desktop). Takes go in
  `~/Movies/Edits-inbox/`, everything else (cards, GIFs, overlays, fonts) in `~/Movies/Edits-assets/<reel>/`.
  Edits needs **full paths** (`/Users/<name>/Movies/...`), never `~`. Get the real path once with `echo $HOME`.
- **iPhone takes are HDR.** Convert to SDR first (section 3) and set every project to SDR.
- **Real things only.** Real screenshots, real logos, real numbers she actually says, her own words. Never invent
  proof, results, quotes or numbers. Proof is always HER proof: ask her for screenshots. Blur other people's names
  and faces unless they agreed. No AI-generated people.
- **Comment-keyword CTAs only if `profile.md` lists that keyword as live.** Never invent a keyword funnel.
- **Looks are "inspired by" a creator's editing techniques only.** Never their footage, logos, wordmarks, music or
  catchphrases.
- **The Edits access token stays private** (section 2).
- **Ask before installing anything** (ffmpeg, Node, Python extras, yt-dlp). Say what it is and why in one line.
- Edits updates about weekly and Meta can switch the automation server off. If a tool errors, say so plainly;
  don't guess or work around it by clicking the Edits window (one button as a last resort at most).

## 1. First run: set up her profile (once, then reuse)

If `SKILL_DIR/profile.md` doesn't exist, copy `profile.example.md` to `profile.md` and fill it in WITH her. Ask in
one friendly message (she can answer in any order, "skip" is fine):
1. Brand colours: a text colour, one accent colour, and a light colour if she has one (hex codes or "the pink in my
   logo" plus a screenshot; you can sample hex values from an image).
2. Fonts: the font(s) she uses for her brand. If she doesn't know: SF Pro Bold for hooks (on every Mac) and Inter
   for captions. If her font is a file she owns, ask for the file and copy it to `~/Movies/Edits-assets/fonts/`.
3. Her Instagram handle.
4. Two or three past captions she's happy with, pasted exactly (this is how you learn her caption voice).
5. Any comment-keyword funnels she already has live (e.g. "comment GUIDE and I'll DM you"), or none.
6. Whether she usually speeds her talking up (many creators use 1.1-1.3x).

Save her answers in `profile.md` (that file is hers: it never gets uploaded, and skill updates don't overwrite it).
Fonts: the first time a font is used, import it into Edits with `importAccountFont` and note it in `profile.md`.
From then on read `profile.md` at the start of every session and never ask these again unless she wants to change them.

## 2. Is Edits connected?

1. Edits for Mac installed (Apple silicon M1 or newer, macOS 15.1+), signed in with Instagram.
   Download: https://edits.instagram.com/desktop . Windows and Intel Macs can't run it: point her to the free
   editing pack (section 8) and Edits on her phone.
2. In Edits: Settings > Automation > **Enable Automation Server** on.
3. The connection command from that screen (the "Claude Code" or "Codex" Copy button) has been run. If she pastes it
   into the chat and says "connect this for me", run it for her once in the terminal exactly as pasted, don't repeat
   it back, don't save it anywhere else, and tell her: "Done. That line has a private key in it. It only unlocks Edits
   on this Mac, but don't post it or show it on a screen recording. If it was ever shown publicly, hit Regenerate
   access token in Edits and paste me the new line." Never run `claude mcp get` (it can print the token).
4. **A project must be open in Edits BEFORE the chat starts.**

Check: look for Edits tools (named like `mcp__metapilot-native__*`; the name can change, so look for tools such as
`addMedia`, `generateCaptions`, `export`) and count them.
- **No Edits tools:** the command hasn't been run, or the chat started before it was. Run it (step 3), then new chat.
- **About 32 tools:** Edits was on its home screen. Say: "Open any project in Edits, then start a new chat with me.
  I only get the full editing tools when a project is open." Don't try to work around it.
- **About 270 tools:** connected. If she asked "list the tools", describe the groups in plain English (cutting,
  captions, text, overlays, colour, sound, checking frames, export) with a count, not a raw list.

Before editing, read `references/edits-tool-notes.md`. It has every tool quirk we know about.

## 3. "Grab my newest video from Downloads and get it ready for Edits"

1. Run `bash SKILL_DIR/scripts/grab_newest_video.sh`. It finds the newest .mov/.mp4/.m4v in `~/Downloads`, COPIES it
   (never moves) to `~/Movies/Edits-inbox/`, checks the colour mode with ffprobe (`arib-std-b67` or `smpte2084` = HDR)
   and converts HDR to SDR with Apple's own converter. The last line it prints is the file to edit.
2. Exit code 2 means ffmpeg is missing. Ask: "I need a free tool called ffmpeg to check your video's colour mode.
   Want me to install it with Homebrew?" If yes: `brew install ffmpeg` (if Homebrew itself is missing, explain and
   ask again before installing it from https://brew.sh). Then run the script again.
3. Tell her in one or two lines: which file (name + time it was saved, so she can spot the wrong one), where it is
   now, and whether it was HDR and got switched to SDR ("the bright colour mode iPhones film in; left on, you can
   look washed out on Instagram").
4. Optional, recommended before editing: `bash SKILL_DIR/scripts/level_voice.sh <file>` evens out her voice to
   Instagram loudness; import the `-levelled.mp4` it makes.

## 4. Pick a look and a format

Show her the library page, which has a demo reel of every look and format:
https://claude.ai/artifact/N46Gep95Kujh6TWQyV2y2r

She picks **one look** (how it looks) and optionally **one format** (how it's structured), by name. Match loosely
("Codie", "the Hormozi one", "pop up proof" all count). If she doesn't pick: tool lists, updates and how-tos ->
Just you; stories and hot takes -> Full. Never mix two looks in one reel. Her own saved looks live in
`SKILL_DIR/my-looks/` and count as looks too.

**Looks** (folder `LOOKS/looks/<slug>/`; quick recipe in `SKILL_DIR/styles/` where there is one):

| Look (gallery name) | Slug | Quick recipe | Edits must do natively |
|---|---|---|---|
| Just you | `just-you` | `styles/just-you.md` | nothing extra |
| Full | `full` | `styles/full.md` | 112% / 125% punch-ins on the big lines |
| Hormozi classic ("Bold Word Pop") | `hormozi-classic` | `styles/hormozi-classic.md` | punch-ins 1.00 / 1.18, one 1.30 |
| Hormozi 2026 ("Red Tag Desk Talk") | `hormozi-2026` | from SPEC | one 1.15 punch-in |
| Codie Sanchez ("Studio editorial") | `codie-sanchez` | from SPEC | alternate 1.00 / 1.18 framing on each cut; warm grade |
| Diary of a CEO ("Podcast clip") | `diary-of-a-ceo` | from SPEC | three crops (1.0 / 1.2 / 1.3) switched on each join; B&W on the last line |
| Nana Del Rey ("Soft Cinema") | `nana-del-rey` | from SPEC | darker, warmer grade |
| Mariah Brunner ("Receipts Round Your Head") | `mariah-brunner` | from SPEC | nothing extra |
| Nick Saraev ("The Recompose") | `nick-saraev` | from SPEC | the clip shrinks/moves for split and full-screen beats (SPEC keyframes) |
| Iman Gadzhi ("Value-only motion") | `iman-gadzhi` | from SPEC | nothing extra; never more than 35% of the reel animated |
| Calm luxury | `calm-luxury` | from SPEC | almost everything (locked frame, one serif line, no SFX) |

**Formats** (folder `LOOKS/formats/<slug>/`; any format works with any look):

| Format (gallery name) | Slug | Quick recipe |
|---|---|---|
| Pop-up proof | `pop-up-proof` | `styles/pop-up-proof.md` |
| Text over B-roll | `text-over-broll` | `styles/text-over-broll.md` |
| Serialised episode | `serialised-episode` | `styles/serialised-episode.md` |
| Before-and-after | `before-after-reveal` | `styles/before-after-reveal.md` |
| POV skit | `pov-skit` | `styles/pov-skit.md` |
| Green-screen proof | `green-screen-proof` | `styles/green-screen-proof.md` |
| Timestamp vlog | `timestamp-vlog` | `styles/timestamp-vlog.md` |
| Yes... but | `yes-but-split` | `styles/yes-but-split.md` |

**Look + format together:** the FORMAT owns the structure (what appears when); the LOOK owns the appearance
(palette, fonts, caption style, grade, pacing, sound). Where they clash, the look wins on appearance and the format
wins on structure. **Brand:** the Just you and Full looks use HER colours and fonts from `profile.md`. Other looks
keep their own fonts and colours, but she may swap the accent for her brand colour.

**"Now do it in the X look":** start a NEW Edits project (`newProject`, then name it with `setTitle`, e.g.
"<topic> - pop-up proof"), keep the first one untouched, and rebuild from the same take.

## 5. Quick or premium?

- **Quick (default):** built entirely with Edits' own tools plus a few PNGs. Works on any Mac with Edits. Follow the
  look's quick recipe file; for looks marked "from SPEC", read its `SPEC.md` in `LOOKS` and build what Edits can do
  natively (cuts, captions, fonts, colours, boxed text as PNGs, cards, zooms, grade, sounds). Skip motion Edits can't
  do (typed-on text, text behind the head, animated cards) and tell her in one line what premium would add.
- **Premium:** the template's motion graphics rendered with HyperFrames as one see-through overlay video, then
  dropped into Edits. Needs Node 22+, HyperFrames and the Python extras. Offer it only when she asks for the "full"
  version of a look, or the look depends on motion (pop-up proof's words behind the head, Nick Saraev's recompose).
  Steps: `references/premium-build.md`.

The first time takes about five minutes while you find your way around Edits, and she can watch the timeline fill
up. Say that up front.

## 6. Quick build steps (in Edits)

The chosen look/format file overrides these wherever it says something different.

1. **New project**, then `setProjectDynamicRange` SDR, `setCanvas` 9:16 at 30 fps. Name it with `setTitle`.
   Import the take from `~/Movies/Edits-inbox/` with `addMedia` (full path).
2. **Rough cut:** `transcribeClip` -> `jobStatus` -> `findPauses`; cut long pauses, restarts and fluffs with `splitAt`
   + `selectById` + `delete`. Keep complete thoughts; no trims under 0.15 s; at most one cut per spoken list item.
   Speed from `profile.md` (or the look's pacing) with `setSpeed`.
3. **Captions:** `generateCaptions`, then the look's style (see `references/edits-tool-notes.md`: base style,
   highlight colour, `setTextFont`, `setTextPosition` low on the chest, never over her face). Off under the text hook.
   **Proofread every caption** and fix with `editCaption` (her name, business, product names, "Claude" vs "cloud").
4. **Text hook:** 2 lines (3 max), 5-9 words, top of the frame, never over her face, held through her spoken hook.
   Edits can't put a box behind text, so draw it:
   `~/.instagram-edits/venv/bin/python SKILL_DIR/scripts/make_text_card.py hook --lines "..." "..." --emoji 🤯 --font <font file> --ink <brand ink> --out ~/Movies/Edits-assets/<reel>/hook.png`
   then `addOverlay` (x 0.5, y ~0.14, scale ~0.8) and `trim` it to the hook. (No Python toolbox yet? Ask, then run
   `bash SKILL_DIR/scripts/setup_python.sh`.) Write the hook from what she actually says; one emoji at most.
5. **Picture cards:** one small card above her head for each real thing she names, in on the word, out when she
   moves on. Real screenshots or logos only: ask her for them, or capture a real website screenshot. Copy each into
   `~/Movies/Edits-assets/<reel>/` and `addOverlay` at the word. List items can use
   `make_text_card.py number --num 1 --label "..." --accent <brand accent>`.
6. **GIFs, stickers, emojis:** only from her own files or the free editing pack (Edits has no GIF search).
   Copy into `~/Movies/Edits-assets/<reel>/`, `addOverlay`, `trim` to the beat. Never over her face. Amount per the look.
7. **Sound:** `searchSoundEffects` (moment map in `library-map.md`), `seek`, `addSoundEffect`, `setVolume` 0.3-0.45.
   Lined up with the thing on screen. Tactile sounds, never notification blips. Music: she adds it herself in the
   Edits window (library music goes silent in Claude's exports). Light voice enhance if the room is noisy.
8. **Zooms and grade:** only what the look says (punch-ins via `splitAt` + `setTransform`; grade via the colour tools).
9. **No end card or sign-off** unless she asks for one on this reel.

## 7. Check your own work before she looks

- `frameSheet` at every cut and key moment: hook readable and clear of her head, captions correct, cards timed to the
  word, nothing stretched (face proportions match the camera), nothing in the bottom ~20% or right edge where
  Instagram's buttons sit.
- `loudness` (aim about -14 LUFS) and look for leftover long pauses.
- Fix, re-check, then tell her: "It's in Edits as <project name>. Have a play, move anything you don't love, and tell
  me when you want your caption." You can't hear: ask her to listen to the sounds.
- Write anything that worked (a sound id, a caption setting) into "My Edits picks" in `profile.md`, and anything that
  broke into "Notes from my sessions".

## 8. Where things come from

1. **Edits' own library first** for sound effects, caption styles, text styles, filters and transitions.
2. **Her own files** for screenshots, logos, proof, GIFs and brand art.
3. **The free editing pack** (optional download, Google Drive):
   https://drive.google.com/drive/folders/1Mxuof-MXE-pr_HyP0bnLVWafaYi32cgG . If she has it, ask where she saved it,
   and copy what you use into `~/Movies/Edits-assets/<reel>/` first. Never assume it's there.

## 9. Hand-over

When the edit is checked: "It's in Edits as <project>. Open it, tweak anything, then say 'write my caption' when
you're happy." Keep it short. Don't export or post unless she asks.

## 10. "Write my caption"

1. Read `profile.md`: her past captions (voice, length, line breaks, emojis, hashtags), words she'd never use, and
   her live comment keywords. Read what she says in the reel (the transcript or captions in Edits).
2. Write ONE caption in her voice:
   - **Line 1 is the hook**: the reason to stop scrolling, in her words. Not a repeat of the on-screen hook word for word.
   - A few short lines that add something the reel doesn't say (a tip, the why, a story beat). Match the length of
     her past captions.
   - **CTA:** if she has a live comment keyword that fits this reel, use it ("Comment GUIDE and I'll send it to
     you"). If not, no keyword: a simple "Save this for later" or a question works.
   - Hashtags and emojis only if her past captions use them, in the same amount.
   - No AI tells: no "dive in", "game-changing", "unlock", "in today's fast-paced world", "Whether you're X, Y or Z",
     "It's important to note", "Furthermore/Moreover", three-word rhythm lists, or em-dash chains.
   - Never invent results, numbers or claims she didn't make.
3. Copy it to the clipboard: `printf '%s' "<caption>" | pbcopy` (use a quoted heredoc if it has quotes in it), and
   save it to `~/Movies/Edits-assets/<reel>/caption.txt`.
4. Show it in full and say: "Copied. Paste it in when you hit Share." Offer one alternative hook line if she wants it.

## 11. Export (only when she asks for a file)

`setExportSettings` with `resolutionType` HD, `aspectRatio` nineBySixteen, `quality` high, frameRate 30,
dynamicRange sdr (all of them, or it silently fails), then `export` to a full path like
`/Users/<name>/Movies/Edits-exports/<reel>.mp4`. Check the file exists and its length matches. If she added library
music, tell her to export from the Edits window instead (Claude's export drops library music); window exports land in
`~/Movies/Edits/Exports/`.

## 12. Posting: two routes, both need her yes

**Route A: Share from Edits (trial reels).** You can't press Share (there's no share tool). Tell her:
"Hit Share in Edits, paste your caption, switch on Trial reel if you want it shown to non-followers first, and post."
A trial reel = Instagram shows it to people who don't follow her first, so she sees if it lands before her followers
do. (The toggle's exact label in Edits may change; tell her to look for "Trial".)

**Route B: Export, then Blotato** (when she wants it on Instagram, TikTok and YouTube):
1. Export (section 11), or use the file she exported from the window.
2. Check Blotato is connected (tools named like `blotato_list_accounts`). If not, tell her it needs connecting first.
3. `blotato_list_accounts` and show her which accounts you'd post to.
4. Show the exact plan: file, caption (from `caption.txt`), which accounts, now or a time, plus a YouTube title
   (under 100 characters, from the hook). **Wait for her yes.**
5. Upload the file (`blotato_create_presigned_upload_url`, then PUT the file to it), then `blotato_create_post` per
   platform with the public URL. Report back with each post's status. Never post anything she didn't approve.

## Notes for Claude
- Don't hard-code her username in paths; use `$HOME`.
- Keep messages short and in plain words. One question at a time when you need something.
- When Edits behaves differently from `references/edits-tool-notes.md`, trust what you see, tell her, and write it
  into "Notes from my sessions" in `profile.md`.
