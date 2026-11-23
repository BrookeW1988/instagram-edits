#!/bin/bash
# hdr_to_sdr.sh: make iPhone HDR footage look the way it did on your phone.
#
# WHY: iPhones film in HDR (Dolby Vision / HLG) by default. Instagram, Edits' default SDR export and most
# editing tools expect normal SDR (Rec.709). Left in HDR, you can come out grey, flat and washed out once
# it's posted. Just relabelling the file, or a quick ffmpeg colour convert, is NOT enough.
#
# HOW: Apple's own converter (`avconvert`, built into macOS) does a proper HDR -> SDR tone map, the same
# engine Photos uses when it shares a video. ffprobe (part of ffmpeg) is only used to check the colour mode.
#
# USAGE:  hdr_to_sdr.sh <video> [<video> ...] [-o <output folder>]
#   - SDR files (webcam, screen recordings, HDR-off iPhone) are left alone; their path is printed as-is.
#   - HDR files become <name>-sdr.mov (full resolution, ~source quality) next to the original,
#     or in the -o folder. The original is never changed.
#   - The LAST line printed for each file is the path to edit from.
#   - Already converted? It reuses the existing -sdr.mov instead of redoing it.

set -euo pipefail

if ! command -v ffprobe >/dev/null 2>&1; then
  echo "ERROR: ffprobe not found. It comes with ffmpeg: brew install ffmpeg" >&2
  exit 2
fi
if ! command -v avconvert >/dev/null 2>&1; then
  echo "ERROR: avconvert not found. It's built into macOS; this script only works on a Mac." >&2
  exit 2
fi

outdir=""
files=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    -o) outdir="$2"; shift 2 ;;
    *)  files+=("$1"); shift ;;
  esac
done
[[ ${#files[@]} -eq 0 ]] && { echo "usage: hdr_to_sdr.sh <video> [...] [-o outdir]" >&2; exit 1; }

transfer_of() {
  ffprobe -v error -select_streams v:0 -show_entries stream=color_transfer \
    -of default=nw=1:nk=1 "$1" 2>/dev/null | head -1
}

for src in "${files[@]}"; do
  [[ -f "$src" ]] || { echo "ERROR: not found: $src" >&2; exit 1; }
  trc="$(transfer_of "$src")"

  # arib-std-b67 = HLG (the iPhone default), smpte2084 = PQ / HDR10 (some cameras and Android phones)
  if [[ "$trc" != "arib-std-b67" && "$trc" != "smpte2084" ]]; then
    echo "SDR already (${trc:-unknown}): no conversion needed: $src"
    echo "$src"
    continue
  fi

  dir="${outdir:-$(dirname "$src")}"
  mkdir -p "$dir"
  base="$(basename "${src%.*}")"
  out="$dir/${base}-sdr.mov"

  if [[ -f "$out" && "$out" -nt "$src" && "$(transfer_of "$out")" == "bt709" ]]; then
    echo "HDR ($trc): reusing existing SDR copy: $out"
    echo "$out"
    continue
  fi

  echo "HDR ($trc): converting with Apple avconvert (a minute or two for a short reel): $src"
  # PresetHighestQuality keeps full resolution and the phone's real frame timings.
  # avconvert prints "completed with error:0." on SUCCESS, so only show its output on failure.
  if ! log="$(avconvert --source "$src" --output "$out" --preset PresetHighestQuality --replace 2>&1)"; then
    echo "ERROR: avconvert failed on $src:" >&2; echo "$log" >&2; exit 1
  fi

  # Check the result really is SDR: never hand back a file that will still look washed out.
  got="$(transfer_of "$out")"
  if [[ "$got" != "bt709" ]]; then
    echo "ERROR: conversion output is '$got', not bt709: $out" >&2
    exit 1
  fi
  echo "$out"
done
