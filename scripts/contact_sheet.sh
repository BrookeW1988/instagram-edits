#!/bin/bash
# contact_sheet.sh: one image of the whole reel (a frame every N seconds), for the final check.
#
# WHY: Claude can't watch a video, but it can look at a grid of frames. Checking the EXPORT (not the editor preview)
# catches what Edits really rendered: captions, sizes, anything clipped at the edges, empty stretches.
# Put it side by side with frames of the reel she's copying and compare.
#
#   bash contact_sheet.sh <video> [output.jpg]   -> 40 frames spread evenly across the WHOLE reel
set -euo pipefail
in="$1"; out="${2:-${in%.*}-sheet.jpg}"
command -v ffmpeg >/dev/null || { echo "ffmpeg is missing (see section 3 of SKILL.md)" >&2; exit 2; }
# one frame every (length / 40) seconds, so a 15 s reel and a 90 s reel both fill the 10 x 4 grid
len=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$in")
step=$(python3 -c "print(max(0.2, $len / 40))")
ffmpeg -loglevel error -y -i "$in" -vf "fps=1/$step,scale=200:-1,tile=10x4" -frames:v 1 "$out"
echo "$out"
