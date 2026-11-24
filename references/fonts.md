# Fonts: which file, where from, and what Edits calls it

Every style uses free Google Fonts (SIL Open Font Licence). Nothing is bundled in this repo:
`scripts/get_fonts.sh` downloads them (ask her first, one line on what and why).

## The three rules
1. **The files must be inside `~/Movies`.** Edits is sandboxed and can't open a font anywhere else. They live in
   `~/Movies/Edits-assets/fonts/`. The PNG scripts read them from there too.
2. **Import once, then use the name Edits reports.** `importAccountFont` with the FULL path
   (`/Users/<name>/Movies/Edits-assets/fonts/<file>`), then `listAccountFonts` to confirm. `setTextFont` wants the
   name in the third column, NOT the file name. Some are odd (Montserrat Black comes in as `MontserratThin-Black`):
   that's what's written inside the file. Use it exactly.
3. **Fonts only used in the PNGs don't need importing.** Pillow reads the file directly.

## The files and the pairings
| File | Fontsource family / weight | Name in Edits (`setTextFont`) | Style: used for |
|---|---|---|---|
| `Montserrat-Black.ttf` | `montserrat` / 900 | `MontserratThin-Black` | Clean: captions, hook, hero word |
| `Inter-Black.ttf` | `inter` / 900 | PNG only | Show it: hook + keyword stacks |
| `Inter-ExtraBold.ttf` | `inter` / 800 | `Inter-ExtraBold` | Show it: captions, card labels |
| `Inter-Bold.ttf` | `inter` / 700 | PNG only | Show it: card sub-labels |
| `InterTight-ExtraBold.ttf` | `inter-tight` / 800 | PNG only | B-roll story: giant words |
| `InterTight-Regular.ttf` | `inter-tight` / 400 | `InterTight-Regular` | B-roll story: subtitles |
| `Newsreader-Regular.ttf` | `newsreader` / 400 | `Newsreader16pt16pt-Regular` | Minimal: captions |

Names confirmed by Edits in testing (24/11/2026). If Edits ever reports a different name, use what Edits says and
update this table. Source pattern: `https://cdn.jsdelivr.net/fontsource/fonts/<family>@latest/latin-<weight>-normal.ttf`

**Why these pairings:** one heavy face for the words that land, one plain face for reading. Show it = Inter Black +
Inter ExtraBold (same family, so it never clashes). B-roll story = Inter Tight ExtraBold + Inter Tight Regular (one
family, two extreme weights, which is what makes the giant words feel designed). Clean and Minimal use one font each.

## Her own brand font
Ask for the file (she must own a licence that allows video use), copy it to `~/Movies/Edits-assets/fonts/`,
`importAccountFont`, read the name back with `listAccountFonts`, and save that name in `profile.md`. It can replace
the caption font in any style; keep the style's display font for stacks and giant words unless she asks.
