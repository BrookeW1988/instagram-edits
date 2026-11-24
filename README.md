# Instagram Edits skill: Claude edits your reels inside Edits for Mac

A skill for **Claude Code** or **Codex** that edits your talking-head reels inside Instagram's free **Edits** app on
your Mac. You film, Claude does the edit in a real Edits project in one of 4 styles (cuts your pauses, adds captions,
real screenshots it finds for you, word stacks, your B-roll, music and sound), checks the result, writes your caption
in your voice, and you press Share.

It uses the automation switch that's built into Edits for Mac, so Claude works right inside the app and you can
still change anything it's done.

Built by [Brooke Wright](https://wrightmode.com) for her community, then shared as the *system*: the 4 styles, the
editing rules, the build steps and the scripts. Your brand colour and caption voice are yours: the skill asks for them the first
time and saves them on your Mac.

---

## What you need

- A Mac with an **M1 chip or newer**, on **macOS 15.1 or later**. (Edits for desktop isn't on Windows or Intel Macs
  yet. On Windows? Grab the free editing pack below and use Edits on your phone.)
- **Edits for Mac**, from https://edits.instagram.com/desktop , logged in with your Instagram account.
- **Claude Code** or **Codex**.
- **ffmpeg** (free). Claude checks for it and offers to install it with Homebrew; it always asks first.
- Optional: **Blotato**, only if you want Claude to post to Instagram, TikTok and YouTube at once (it's a separate
  account you connect to Claude first).

That's it. Claude builds every style with Edits' own tools. The first time, it offers to set up a small Python
toolbox (for drawing the cards and word stacks) and download a few free fonts. It always asks first.

---

## Install (the easy way)

1. **Open a project in Edits and leave it open.** Always have a project open in Edits before you start a chat
   with Claude: on the Edits home screen Claude only gets a handful of tools; with a project open it gets them all.
2. **Connect Claude to Edits.** Open Claude Code or Codex in your usual folder (your Claude HQ) and start a chat.
   In Edits, go to **Settings > Automation**, switch on **Enable Automation Server**, hit **Copy** next to
   Claude Code (or Codex), paste that line into the chat and say:

   > connect this for me

   The line has a private key in it, but it only unlocks Edits on this Mac. Don't post it or show it on a screen
   recording; if it ever was, hit **Regenerate access token** in Edits and connect again.
3. **Install the skill.** In the same chat, paste this link (https://github.com/BrookeW1988/instagram-edits) and say:

   > install this skill for me
4. **Start a new chat** (so Claude picks up Edits and the skill), then type `/instagram-edits`. It checks it can
   see Edits, then asks for your brand colour, Instagram handle and two or three past captions, and saves them.

**Words you'll hear:** *B-roll* = short clips of you doing things, cut over your voice. *Captions* = the words on
screen as you talk. *Punch-in* = a quick zoom in on your face. *Word stack* = a few big words stacked on screen.
*HDR / SDR* = iPhone's bright colour mode / normal colour (Claude switches it so you don't look washed out).
*Rough cut* = cutting out the pauses and false starts.

### For Claude or Codex doing the install

Install ONE copy and link it, so Claude Code and Codex share the same profile:

```bash
# 1. Download the skill (git comes with macOS's developer tools; if git isn't there, macOS offers to install it,
#    or download https://github.com/BrookeW1988/instagram-edits/archive/refs/heads/main.zip and unzip it
#    to the same place, renaming the folder to instagram-edits)
mkdir -p ~/.agents/skills ~/.claude/skills
git clone https://github.com/BrookeW1988/instagram-edits ~/.agents/skills/instagram-edits

# 2. Make it visible to Claude Code too (a link, not a second copy)
[ -e ~/.claude/skills/instagram-edits ] || ln -s ~/.agents/skills/instagram-edits ~/.claude/skills/instagram-edits

# 3. Make the scripts runnable
chmod +x ~/.agents/skills/instagram-edits/scripts/*.sh
```

If `~/.claude/skills/instagram-edits` or `~/.agents/skills/instagram-edits` already exists, stop and ask before
replacing it (it may hold the person's `profile.md`). Then tell them to start a new chat and type `/instagram-edits`.

### Manual install

Copy this whole folder (named `instagram-edits`) to `~/.claude/skills/instagram-edits/` for Claude Code, or
`~/.agents/skills/instagram-edits/` for Codex.

### Updating

`cd ~/.agents/skills/instagram-edits && git pull`. Your `profile.md` and your own looks in `my-looks/` are never touched by updates.

---

## What to say

| Say this | What happens |
|---|---|
| **grab my newest video from Downloads and get it ready for Edits** | Finds the newest video in Downloads (AirDrop puts phone videos there), copies it into `Movies/Edits-inbox` (Edits can only open videos from your Movies folder), and switches it out of iPhone HDR so you don't look washed out on Instagram |
| **/instagram-edits** | Starts an edit: Claude reads your video, shows you an edit plan with timings, rough-cuts it in Edits and builds it in the style that fits |
| **just edit it** | A proper editor pass with no style: rough cut, captions, punch-ins and pacing |
| **just do the rough cut** | Cuts your pauses and false starts in Edits, then hands it back |
| **edit this in the Show it style** | Builds the edit in your open Edits project in that style |
| **now do it in the Clean style** | Rebuilds the same video in a new Edits project, in a different style |
| **analyse my editing style frame by frame and save it as a new look** (+ links to 3 of your reels) | Measures your reels and saves your style as a look you can reuse |
| **write my caption** | Writes your Instagram caption in your voice and copies it, ready to paste |
| **export it** | Saves the finished reel to your Mac |
| **publish this to Instagram, TikTok and YouTube with Blotato** | Posts your exported reel with Blotato, after you say yes to the exact post |

**Claude never posts for you.** In Edits you press **Share**, paste your caption, and switch on **Trial reel** if you
want it shown to people who don't follow you first. Or ask Claude to publish with Blotato: it exports the reel,
shows you exactly what it will post and waits for your yes.

---

## The 4 styles

See them (with a demo reel each) in the **Reel Look Library**: https://claude.ai/artifact/N46Gep95Kujh6TWQyV2y2r

| Style | Inspired by | You need | What Claude does |
|---|---|---|---|
| **Clean** | Alex Hormozi's classic captions | any talking-head video | tight cuts, punch-ins, big bold captions with the spoken word in yellow |
| **Show it** | Mariah Brunner | a video where you NAME things (tools, steps, "5 things...") | finds the real screen of each thing you name and pops it up on a numbered card, plus keyword stacks |
| **B-roll story** | Nana Del Rey | your voice + 3-6 clips from your camera roll | cuts your B-roll over your voice, small subtitles, two or three giant word moments, soft music |
| **Minimal** | calm luxury | a calm, considered video | one small serif caption line and a warm grade, nothing else |

Not sure? Just say "edit this" and Claude picks the style that fits what you filmed. Styles named after creators are
**inspired by their editing techniques** only (sizes, pacing, caption style). They never use the creators'
footage, logos, music or catchphrases.

---

## Free editing pack (optional)

Brooke's free pack of reaction GIFs, callouts and sounds lives on Google Drive:
https://drive.google.com/drive/folders/1Mxuof-MXE-pr_HyP0bnLVWafaYi32cgG . Download it if you want more GIFs than
Edits has (Edits has no GIF search for Claude). Tell Claude where you saved it.

---

## What's inside

```
SKILL.md                    the instructions Claude follows
profile.example.md          what your profile looks like (yours is saved as profile.md on first run)
library-map.md              Edits sounds, music and effects that worked in testing
styles/                     the 4 style recipes (clean, show-it, broll-story, minimal)
references/
  editing-craft.md          how a good editor thinks: the edit plan, rough cut, pacing, punch-ins, captions, sound, the final check
  edits-equivalents.md      which Edits tools do each editor move (cut, punch-in, J-cut, cutaway, music...)
  edits-tool-notes.md       every Edits tool quirk found so far
  fonts.md                  which free font each style uses and what Edits calls it
  make-your-own-look.md     how "save my style as a new look" works
scripts/
  grab_newest_video.sh      newest video in Downloads -> Movies/Edits-inbox, HDR -> SDR
  hdr_to_sdr.sh             iPhone HDR -> SDR with Apple's own converter (built into macOS)
  level_voice.sh            evens out your voice to Instagram loudness (-14 LUFS) before editing
  get_fonts.sh              downloads the free fonts the styles use
  setup_python.sh           sets up the small Python toolbox (Pillow)
  grab_page_images.py       downloads the product screenshots from a maker's own page (Show it)
  show_it_cards.py          draws the Show it numbered cards with the real screen inside
  word_stacks.py            draws the word stacks (Show it) and giant words (B-roll story)
  contact_sheet.sh          one image of the whole export, for Claude's final check
my-looks/                   looks you create from your own reels (yours, never overwritten)
```

Things that land on your Mac: your videos in `~/Movies/Edits-inbox/`, screenshots, cards and fonts in `~/Movies/Edits-assets/`,
and the Python toolbox in `~/.instagram-edits/`. Delete any of them any time.

---

## Good to know

- **Only a few tools?** Edits was on its home screen. Open a project, then start a new chat.
- **The first edit takes about ten minutes** while Claude finds its way around Edits. It gets quicker.
- **Music:** Claude can add royalty-free songs from Edits' own library, and they export fine. Want a licensed
  (trending) song? Add it yourself in the Edits window and share from there.
- Edits updates about weekly, so its tools can change. If something stops working, tell Claude; it notes what changed.

## Licence

The code and instructions are MIT licensed (see `LICENSE`). No fonts, sounds, GIFs or videos are included. The fonts the
looks use are free Google Fonts under the SIL Open Font Licence. See `references/fonts.md`.
