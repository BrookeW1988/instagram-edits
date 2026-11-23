#!/bin/bash
# level_voice.sh: even out your voice and set it to Instagram loudness (about -14 LUFS) BEFORE editing.
#
# WHY: phone takes usually come in quiet (around -22 LUFS) and uneven. Edits' own "normalize" is plain
# volume gain: in testing it pushed the peaks into clipping (crackly audio) and, in "add" mode, dropped a
# new clip on the timeline. Levelling the file first with ffmpeg avoids both. The video is copied untouched.
#
# The chain, in plain English: cut rumble below 70 Hz -> gentle compression so loud and soft words sit closer
# -> loudness to -14 LUFS with peaks kept under -2 dB -> a safety limiter.
#
# USAGE:  bash level_voice.sh <video in ~/Movies/Edits-inbox>
# Writes <name>-levelled.mp4 next to it and prints that path on the last line.

set -euo pipefail

src="${1:-}"
[ -f "$src" ] || { echo "usage: level_voice.sh <video>" >&2; exit 1; }
command -v ffmpeg >/dev/null 2>&1 || { echo "ffmpeg is not installed: brew install ffmpeg" >&2; exit 2; }

out="${src%.*}-levelled.mp4"
ffmpeg -hide_banner -loglevel error -y -i "$src" \
  -af "highpass=f=70,acompressor=threshold=-26dB:ratio=3:attack=8:release=120:makeup=4dB,loudnorm=I=-14:TP=-2:LRA=7,alimiter=limit=0.84:level=disabled" \
  -c:v copy -c:a aac -b:a 256k -ar 48000 -movflags +faststart "$out"

echo "$out"
