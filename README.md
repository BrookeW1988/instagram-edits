# Instagram Edits skill: Claude edits your reels inside Edits for Mac

A skill for **Claude Code** or **Codex** that edits your talking-head reels inside Instagram's free **Edits** app on
your Mac. You film, Claude does the edit in a real Edits project (cuts your pauses, adds captions, a text hook,
picture cards, GIFs, sound effects and zooms), writes your caption in your voice, and you press Share.

It uses the automation switch that's built into Edits for Mac, so Claude works right inside the app and you can
still change anything it's done.

Built by [Brooke Wright](https://wrightmode.com) for her community, then shared as the *system*: the looks, the
build steps, the rules and the scripts. Your colours, fonts and caption voice are yours: the skill asks for them the
first time and saves them on your Mac.

---

## What you need

- A Mac with an **M1 chip or newer**, on **macOS 15.1 or later**. (Edits for desktop isn't on Windows or Intel Macs
  yet. On Windows? Grab the free editing pack below and use Edits on your phone.)
- **Edits for Mac**, from https://edits.instagram.com/desktop , logged in with your Instagram account.
- **Claude Code** or **Codex**.
- **ffmpeg** (free). Claude checks for it and offers to install it with Homebrew; it always asks first.

That's it for the normal (quick) edits. The premium versions of the looks also need Node.js 22+ and HyperFrames;
Claude offers to set those up only if you ask for premium.

---

## Install (the easy way)

1. In Edits, start a project and leave it open. **Always have a project open in Edits before you start a chat
   with Claude.** On the Edits home screen Claude only gets a handful of tools; with a project open it gets the full
   editing suite.
2. In Edits, go to **Settings > Automation**, switch on **Enable Automation Server**, and hit **Copy** next to
   Claude Code (or Codex). That line has a private key in it: paste it into the **Terminal** app and press Enter,
   and don't share it or show it on a screen recording. (If you ever do, hit **Regenerate access token**.)
3. Start a new chat in Claude Code or Codex (in your usual Claude HQ folder) and ask it to **list the tools it has
   in Edits, in plain English**. That's how you know it's working.
4. Paste this repo's link into the chat and say:

   > install this skill for me

5. Start a new chat, then type `/instagram-edits`. The first time, it asks for your brand colours, fonts,
   Instagram handle and two or three past captions, and saves them.

### For Claude or Codex doing the install

Install ONE copy and link it, so Claude Code and Codex share the same profile:

```bash
# 1. Download the skill (git comes with macOS's developer tools; if git isn't there, macOS offers to install it,
#    or download https://github.com/BrookeW1988/instagram-edits-skill/archive/refs/heads/main.zip and unzip it
#    to the same place, renaming the folder to instagram-edits)
mkdir -p ~/.agents/skills
git clone https://github.com/BrookeW1988/instagram-edits-skill ~/.agents/skills/instagram-edits

# 2. Make it visible to Claude Code too (a link, not a second copy)
mkdir -p ~/.claude/skills
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

`cd ~/.agents/skills/instagram-edits && git pull`. Your `profile.md` and your own looks in `my-looks/` are never
touched by updates.

---

## What to say

| Say this | What happens |
|---|---|
| **grab my newest video from Downloads and get it ready for Edits** | Finds the newest video in Downloads (AirDrop puts phone videos there), copies it into `Movies/Edits-inbox` (Edits can only open videos from your Movies folder), and switches it out of iPhone HDR so you don't look washed out on Instagram |
| **/instagram-edits** | Starts an edit: pick a look and a format |
| **edit this in the Full look** | Builds the edit in your open Edits project in that look |
| **now do it in the pop-up proof look** | Rebuilds the same video in a new Edits project, in a different look |
| **analyse my editing style frame by frame and save it as a new look** (+ links to 3 of your reels) | Measures your reels and saves your style as a look you can reuse |
| **write my caption** | Writes your Instagram caption in your voice and copies it, ready to paste |
| **export it** | Saves the finished reel to your Mac |
| **publish this to Instagram, TikTok and YouTube with Blotato** | Posts your exported reel with Blotato, after you say yes to the exact post |

**Claude never posts for you.** In Edits you press **Share**, paste your caption, and switch on **Trial reel** if you
want it shown to people who don't follow you first. Or you hit **Export** and ask Claude to publish with Blotato;
it shows you exactly what it will post and waits for your yes.

---

## The looks and formats

See them all (with a demo reel each) in the **Reel Look Library**: https://claude.ai/artifact/N46Gep95Kujh6TWQyV2y2r

- **Looks** (how it looks): Just you · Full · Hormozi classic · Hormozi 2026 · Codie Sanchez · Diary of a CEO ·
  Nana Del Rey · Mariah Brunner · Nick Saraev · Iman Gadzhi · Calm luxury
- **Formats** (how it's structured): Pop-up proof · Text over B-roll · Serialised episode · Before-and-after ·
  POV skit · Green-screen proof · Timestamp vlog · Yes... but

Looks named after creators are **inspired by their editing techniques** (sizes, pacing, caption style), measured from
their public reels. They never use the creators' footage, logos, music or catchphrases. Pop-up proof uses **your**
proof: Claude asks for your own screenshots.

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
library-map.md              Edits sound effects and caption styles that worked in testing
styles/                     quick recipes: each look or format built with Edits' own tools
templates/                  premium templates (HyperFrames): one folder per look/format, SPEC.md has every number
  _shared/                  helpers several templates use
references/
  edits-tool-notes.md       every Edits tool quirk found so far
  premium-build.md          how the premium route works
  make-your-own-look.md     how "save my style as a new look" works
scripts/
  grab_newest_video.sh      newest video in Downloads -> Movies/Edits-inbox, HDR -> SDR
  hdr_to_sdr.sh             iPhone HDR -> SDR with Apple's own converter (built into macOS)
  level_voice.sh            evens out your voice to Instagram loudness (-14 LUFS) before editing
  make_text_card.py         draws boxed text hooks and number cards as see-through PNGs
  setup_python.sh           sets up the small Python toolbox (Pillow; premium adds mlx-whisper)
  get_fonts.sh              downloads the free fonts a template needs
  prep_overlay.sh           gets a premium overlay ready to render
my-looks/                   looks you create from your own reels (yours, never overwritten)
```

Things that land on your Mac: your videos in `~/Movies/Edits-inbox/`, cards and overlays in `~/Movies/Edits-assets/`,
premium builds in `~/Movies/Edits-builds/`, and the Python toolbox in `~/.instagram-edits/`. Delete any of them any time.

---

## Good to know

- **Only a few tools?** Edits was on its home screen. Open a project, then start a new chat.
- **The first edit takes about five minutes** while Claude finds its way around Edits. It gets quicker.
- **Music:** add songs from Edits' library yourself in the Edits window, and share or export from the window. Songs
  from the library go silent when Claude exports.
- Edits updates about weekly, so its tools can change. If something stops working, tell Claude; it notes what changed.

## Licence

The code and instructions are MIT licensed (see `LICENSE`). No fonts, sounds, GIFs or videos are included. The fonts the
templates download are free Google Fonts under the SIL Open Font Licence; SF Pro is Apple's font and is only ever copied
from your own Mac for your own builds. See `FONTS.md`.
