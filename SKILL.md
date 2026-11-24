---
name: instagram-edits
description: Edit your talking-head reels inside Instagram's Edits for Mac app with Claude, through Edits' built-in automation server. Gets your newest video from Downloads ready for Edits (copied to Movies, HDR switched to SDR), rough-cuts it inside Edits, then edits it in one of 4 styles (Clean, Show it, B-roll story, Minimal) with captions, real screenshots Claude finds for you, word stacks, B-roll, music and sound, checks the export, writes your Instagram caption in your voice and copies it, and helps you post (you press Share, or export and publish with Blotato). Use when someone says "/instagram-edits", "edit this in Edits", "edit this in the <style> style", "now do it in the <style> style", "grab my newest video from Downloads and get it ready for Edits", "write my caption", "analyse my editing style and save it as a new look", or "publish this with Blotato".
---

# Instagram Edits (Edits for Mac + Claude)

You edit her reel in a real Edits project. She can tweak anything by hand afterwards, and she always presses the
last button. Talk in plain English: she's a business owner, not a video editor or a developer. Australian spelling.

**Paths in this file:** `SKILL_DIR` = the folder this SKILL.md is in. Scripts live in `SKILL_DIR/scripts/`,
style recipes in `SKILL_DIR/styles/`, and the editor's rulebook in `SKILL_DIR/references/editing-craft.md`.

## What she might say (and where to go)

| She says | Do |
|---|---|
| "/instagram-edits" (first time ever) | Section 1 (setup), then 2, then ask which video |
| "list the tools you have in Edits" | Section 2: count them and describe the groups in plain English |
| "grab my newest video from Downloads and get it ready for Edits" | Section 3 |
| "edit this" / "edit this in the Show it style" / "/instagram-edits" | Sections 4-7 |
| "now do it in the Clean style" | Rebuild from the SAME take in a NEW Edits project (keep the first one) |
| "analyse my editing style frame by frame and save it as a new look" (+ reel links) | `references/make-your-own-look.md` |
| "write my caption" | Section 9 |
| "export it" | Section 10 |
| "publish this to Instagram, TikTok and YouTube with Blotato" | Section 11 |
| "update my profile" / "change my colours" | Edit `SKILL_DIR/profile.md` with her |

## 0. Hard rules (never break these)

- **Never post, share, trial-post, schedule or delete** anything without her clear yes for that exact reel. That
  includes Blotato posts and deleting Edits projects.
- **Files must be inside `~/Movies`** (Edits is sandboxed and can't open Downloads or Desktop). Takes go in
  `~/Movies/Edits-inbox/`, everything else (screenshots, cards, B-roll, fonts) in `~/Movies/Edits-assets/<reel>/`.
  Edits needs **full paths** (`/Users/<name>/Movies/...`), never `~`. Get the real path once with `echo $HOME`.
- **iPhone takes are HDR.** Convert to SDR first (section 3) and set every project to SDR.
- **Real things only.** Real screens (hers, or official product images from the maker's own website), real logos,
  numbers she actually says, her own words. Never invent proof, results, quotes or numbers, and never mock up a
  screen. Blur other people's names and faces unless they agreed. No AI-generated people.
- **Comment-keyword CTAs only if `profile.md` lists that keyword as live.** Never invent a keyword funnel.
- **Styles are "inspired by" a creator's editing techniques only.** Never their footage, logos, music or catchphrases.
- **The Edits access token stays private** (section 2).
- **Ask before installing or downloading anything** (ffmpeg, the Python toolbox, the free fonts). One line on what
  and why.
- Edits updates about weekly and Meta can switch the automation server off. If a tool errors, say so plainly;
  don't guess or work around it by clicking the Edits window.

## 1. First run: set up her profile (once, then reuse)

If `SKILL_DIR/profile.md` doesn't exist, copy `profile.example.md` to `profile.md` and fill it in WITH her. Ask in
one friendly message (she can answer in any order, "skip" is fine):
1. Her brand accent colour (a hex code, or "the pink in my logo" plus a screenshot; you can sample it).
2. Her Instagram handle.
3. Two or three past captions she's happy with, pasted exactly (this is how you learn her caption voice).
4. Any comment-keyword funnels she already has live (e.g. "comment GUIDE and I'll DM you"), or none.
5. Whether she likes her talking sped up a little (many creators use 1.1-1.3x).

Save her answers in `profile.md` (it's hers: never uploaded, and skill updates don't overwrite it). Read it at the
start of every session and never ask these again unless she wants to change them.

**One-time toolbox (ask first):** `bash SKILL_DIR/scripts/setup_python.sh` (a private Python folder with Pillow,
which draws the cards and word stacks) and `bash SKILL_DIR/scripts/get_fonts.sh` (the free fonts the styles use,
saved in `~/Movies/Edits-assets/fonts/`). Then `importAccountFont` the fonts Edits needs by name (the ones with a name in `references/fonts.md`; the
PNG-only fonts don't need importing).

## 2. Is Edits connected?

1. Edits for Mac installed (Apple silicon M1 or newer, macOS 15.1+), signed in with Instagram.
   Download: https://edits.instagram.com/desktop . Windows and Intel Macs can't run it yet.
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
  I only get the full editing tools when a project is open."
- **About 270 tools:** connected. If she asked "list the tools", describe the groups in plain English (cutting,
  captions, text, overlays, colour, sound, music, checking frames, export) with a count, not a raw list.

Before editing, read `references/edits-tool-notes.md` (every tool quirk we know about).

## 3. "Grab my newest video from Downloads and get it ready for Edits"

1. Run `bash SKILL_DIR/scripts/grab_newest_video.sh`. It finds the newest .mov/.mp4/.m4v in `~/Downloads`, COPIES it
   (never moves) to `~/Movies/Edits-inbox/`, checks the colour mode and converts HDR to SDR. The last line it prints
   is the file to edit.
2. Exit code 2 means ffmpeg is missing. Ask: "I need a free tool called ffmpeg to check your video's colour mode.
   Want me to install it with Homebrew?" If yes: `brew install ffmpeg` (if Homebrew itself is missing, explain and
   ask again before installing it from https://brew.sh). Then run the script again.
3. Tell her in one or two lines: which file (name + time it was saved), where it is now, and whether it was HDR and
   got switched to SDR ("the bright colour mode iPhones film in; left on, you can look washed out on Instagram").
4. Recommended: `bash SKILL_DIR/scripts/level_voice.sh <file>` evens out her voice to Instagram loudness; import the
   `-levelled.mp4` it makes. B-roll clips: copy them into `~/Movies/Edits-assets/<reel>/` and run
   `scripts/hdr_to_sdr.sh` on any iPhone clip.

## 4. Pick the style (from the footage)

Read `references/editing-craft.md` now; it's the order every edit follows. Then match the style to what she filmed:

| Style | Inspired by | Needs | Recipe |
|---|---|---|---|
| **Clean** | Alex Hormozi's classic captions | any talking-head take | `styles/clean.md` |
| **Show it** | Mariah Brunner | a take where she NAMES things (tools, steps, "5 things...") | `styles/show-it.md` |
| **B-roll story** | Nana Del Rey | her voice + 3-6 camera-roll clips of her doing things | `styles/broll-story.md` |
| **Minimal** | calm luxury | a calm take (story, reflection, premium offer) | `styles/minimal.md` |

She can pick by name ("the Mariah one", "the B-roll one" count). If she doesn't pick, choose from the footage and
say why in one line. If she picks one her footage can't carry, say so kindly and suggest the fit, or tell her what
to film or send ("Send me 3-5 clips of you working and I'll do the B-roll one"). Her own saved looks
(`SKILL_DIR/my-looks/`) count too. Show her the demos if she wants to see them first:
https://claude.ai/artifact/N46Gep95Kujh6TWQyV2y2r

## 5. Build it (in Edits, with Edits' own tools)

1. **New project:** `saveProject` the open one first, then `newProject` (if it errors, check `title` + `clips`:
   the new project often opened anyway) -> `setTitle` ("<topic> - <style>") -> `setProjectDynamicRange` sdr ->
   `setCanvas` 9:16 at 30 fps -> `addMedia` the take (full path).
2. **Rough cut in Edits** (editing-craft section 1): `transcribeClip` -> `jobStatus` -> plan the cuts from the word
   times -> `splitAt` -> `selectById` the dead pieces -> `delete`. Speed from `profile.md`.
3. **Follow the style recipe** step by step: captions, graphics, B-roll, sound, grade. Its numbers are tested.
4. **Graphics Edits can't draw** (cards with a screenshot inside, word stacks with a soft shadow, tight-spaced giant
   words) are made as see-through PNGs by `scripts/show_it_cards.py` and `scripts/word_stacks.py` and placed in
   Edits with `addOverlay`. Run them with `~/.instagram-edits/venv/bin/python`. Everything else is Edits' own tools.
5. **Screens to show** (Show it): Claude finds them; she doesn't need a library. Her screenshots first, otherwise
   `scripts/grab_page_images.py` on the maker's own product page, then look and crop to the app window.

The first edit takes about 10 minutes and she can watch the timeline fill up. Say that up front. `saveProject`
after each big step.

## 6. Check your own work (on the export)

Export (section 10) to `~/Movies/Edits-assets/<reel>/check.mp4`, run `bash SKILL_DIR/scripts/contact_sheet.sh
<file>`, look at the sheet next to the creator's real reel, and go through the checklist at the end of
`references/editing-craft.md`. Fix, re-export, check again. Only then tell her it's ready. Claude can't hear: ask
her to listen to the music level and the sounds.

## 7. Hand-over

"It's in Edits as <project>. Have a play, move anything you don't love, then say 'write my caption' when you're
happy." Keep it short. Write anything that worked into "My Edits picks" in `profile.md`, and anything that broke
into "Notes from my sessions".

## 8. Where things come from

1. **Edits' own library** for sound effects, royalty-free music, caption styles, filters.
2. **Her own files** for B-roll, screenshots, proof and brand art.
3. **Official product images** from the maker's own website (Show it), cropped to the app.
4. Optional: the free editing pack (Google Drive): https://drive.google.com/drive/folders/1Mxuof-MXE-pr_HyP0bnLVWafaYi32cgG .
   Ask where she saved it and copy what you use into `~/Movies/Edits-assets/<reel>/` first.

## 9. "Write my caption"

1. Read `profile.md`: her past captions (voice, length, line breaks, emojis, hashtags), words she'd never use, and
   her live comment keywords. Read what she says in the reel (the captions in Edits).
2. Write ONE caption in her voice:
   - **Line 1 is the hook**: the reason to stop scrolling, in her words. Not a repeat of the on-screen hook.
   - A few short lines that add something the reel doesn't say. Match the length of her past captions.
   - **CTA:** a live comment keyword that fits this reel, or else "Save this for later" or a question.
   - Hashtags and emojis only if her past captions use them, in the same amount.
   - No AI tells: no "dive in", "game-changing", "unlock", "in today's fast-paced world", "Whether you're X, Y or Z",
     "It's important to note", "Furthermore/Moreover", three-word rhythm lists, or em-dash chains.
   - Never invent results, numbers or claims she didn't make.
3. Copy it: `printf '%s' "<caption>" | pbcopy` (a quoted heredoc if it has quotes), and save it to
   `~/Movies/Edits-assets/<reel>/caption.txt`.
4. Show it in full and say: "Copied. Paste it in when you hit Share." Offer one alternative hook line.

## 10. Export (for the check, or when she asks for a file)

`setExportSettings` with `resolutionType` HD, `aspectRatio` nineBySixteen, `quality` high, frameRate 30,
dynamicRange sdr (all of them, or it silently fails), then `export` to a full path in `~/Movies`. Wait until the
file stops growing, then check it exists and its length matches.

## 11. Posting: two routes, both need her yes

**Route A: Share from Edits (trial reels).** You can't press Share (there's no share tool). Tell her:
"Hit Share in Edits, paste your caption, switch on Trial reel if you want it shown to non-followers first, and post."

**Route B: Export, then Blotato** (Instagram, TikTok and YouTube at once):
1. Export (section 10). 2. Check Blotato is connected (tools named like `blotato_list_accounts`).
3. `blotato_list_accounts`, show her which accounts you'd post to.
4. Show the exact plan: file, caption, accounts, now or a time, plus a YouTube title (under 100 characters).
   **Wait for her yes.**
5. `blotato_create_presigned_upload_url`, PUT the file, then `blotato_create_post` per platform. Report each status.

## Notes for Claude
- Don't hard-code her username in paths; use `$HOME`.
- Short messages, plain words, one question at a time.
- When Edits behaves differently from `references/edits-tool-notes.md`, trust what you see, tell her, and write it
  into "Notes from my sessions" in `profile.md`.
