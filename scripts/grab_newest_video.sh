#!/bin/bash
# grab_newest_video.sh: "grab my newest video from Downloads and get it ready for Edits".
#
# WHY: AirDrop drops phone videos into Downloads, but Edits for Mac can only open files inside your Movies
# folder (it's sandboxed by macOS). So this finds the newest video in Downloads, copies it (never moves it)
# into ~/Movies/Edits-inbox/, then switches it out of iPhone HDR so you don't look washed out on Instagram.
#
# USAGE:  bash grab_newest_video.sh [<folder to look in>]     (default: ~/Downloads)
# The LAST line printed is the full path of the file to import into Edits.
# Exit code 2 = ffmpeg is missing (Claude offers to install it and asks first).

set -euo pipefail

here="$(cd "$(dirname "$0")" && pwd)"
src_dir="${1:-$HOME/Downloads}"
inbox="${EDITS_INBOX:-$HOME/Movies/Edits-inbox}"   # EDITS_INBOX only exists for testing

if ! command -v ffprobe >/dev/null 2>&1; then
  echo "ffmpeg is not installed (needed to check the colour mode). Install with: brew install ffmpeg" >&2
  exit 2
fi

# Newest .mov / .mp4 / .m4v by modified time (upper or lower case), top level of the folder only.
# stat prints "<modified time> <path>" for each video; sort puts the newest first. (-exec ... + runs nothing
# when there are no videos, so an empty Downloads folder can't list the wrong thing.)
newest="$(find "$src_dir" -maxdepth 1 -type f \( -iname '*.mov' -o -iname '*.mp4' -o -iname '*.m4v' \) \
  -exec stat -f '%m %N' {} + 2>/dev/null | sort -rn | head -1 | cut -d' ' -f2- || true)"

if [ -z "$newest" ]; then
  echo "ERROR: no .mov, .mp4 or .m4v videos found in $src_dir" >&2
  exit 1
fi

echo "Newest video: $newest ($(date -r "$newest" '+%d/%m/%Y %H:%M'))"

mkdir -p "$inbox"
dest="$inbox/$(basename "$newest")"
if [ -e "$dest" ] && cmp -s "$newest" "$dest"; then
  echo "Already in Edits-inbox: $dest"
else
  # -n: never overwrite a different file that happens to share the name
  if [ -e "$dest" ]; then
    stem="$(basename "${newest%.*}")"; ext="${newest##*.}"
    dest="$inbox/${stem}-$(date '+%Y%m%d-%H%M%S').$ext"
  fi
  cp -n "$newest" "$dest"
  echo "Copied to: $dest"
fi

# HDR check + convert. The script prints the path to edit from on its last line.
bash "$here/hdr_to_sdr.sh" "$dest" -o "$inbox"
