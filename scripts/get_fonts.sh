#!/bin/bash
# get_fonts.sh: download the free fonts the 4 styles use into ~/Movies/Edits-assets/fonts.
#
# WHY ~/Movies: Edits is sandboxed and can only open files inside your Movies folder, so importAccountFont
# can't see a font anywhere else. WHY Fontsource: it serves the Google Fonts files as plain single-weight .ttf
# files (one file per weight), which is what Edits and the PNG scripts need. All of them are free under the
# SIL Open Font Licence. See references/fonts.md for which style uses which file.
#
#   bash get_fonts.sh                       -> gets every font (about 1 MB in total), skips ones already there
#   bash get_fonts.sh Inter-Black.ttf ...   -> gets only the files you name
#
# Claude asks before running this. Nothing is uploaded and no keys are needed.

set -euo pipefail

dest="$HOME/Movies/Edits-assets/fonts"
mkdir -p "$dest"

# file name | Fontsource family | weight | style
fonts='Montserrat-Black.ttf montserrat 900 normal
Inter-Bold.ttf inter 700 normal
Inter-ExtraBold.ttf inter 800 normal
Inter-Black.ttf inter 900 normal
InterTight-Regular.ttf inter-tight 400 normal
InterTight-ExtraBold.ttf inter-tight 800 normal
Newsreader-Regular.ttf newsreader 400 normal'

failed=0
while read -r file family weight style; do
  # Only the named files, if any were named
  if [ "$#" -gt 0 ]; then
    case " $* " in *" $file "*) ;; *) continue ;; esac
  fi
  if [ -s "$dest/$file" ]; then
    echo "have  $file"
    continue
  fi
  url="https://cdn.jsdelivr.net/fontsource/fonts/${family}@latest/latin-${weight}-${style}.ttf"
  # Download to a temp name first, so a failed download never leaves a broken font behind
  if curl -fsSL "$url" -o "$dest/$file.part"; then
    mv "$dest/$file.part" "$dest/$file"
    echo "got   $file"
  else
    rm -f "$dest/$file.part"
    echo "FAILED $file ($url)" >&2
    failed=$((failed + 1))
  fi
done <<< "$fonts"
# a here-string (not a pipe) keeps the loop in this shell, so the failure count survives
if [ "$failed" -gt 0 ]; then echo "$failed font(s) failed to download" >&2; exit 1; fi

echo "$dest"
