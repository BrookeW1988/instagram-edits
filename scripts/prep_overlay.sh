#!/bin/bash
# prep_overlay.sh: make sure a template's overlay folder is a complete HyperFrames project before rendering it.
#
# WHY: each template's build.py writes the overlay page (the graphics on a see-through background that goes
# into Edits). Some templates only write the page itself, and HyperFrames refuses to render a folder that
# doesn't also have hyperframes.json, package.json, meta.json and the shared assets. This fills in ONLY the
# missing pieces, so it never overwrites anything a template made.
#
# USAGE:  bash prep_overlay.sh <build-folder> <overlay-folder-name>
#   e.g.  bash prep_overlay.sh ~/Movies/Edits-builds/2026-11-23-nick-saraev-pricing overlay
# Skip it when the template renders a single file (iman-gadzhi uses `render -c overlays.html`).

set -euo pipefail

build="${1:-}"
name="${2:-}"
if [ -z "$build" ] || [ -z "$name" ]; then
  echo "usage: prep_overlay.sh <build-folder> <overlay-folder-name>" >&2
  exit 1
fi

ov="$build/$name"
if [ ! -f "$ov/index.html" ]; then
  echo "ERROR: $ov/index.html not found. Run the template's build.py with its overlay option first." >&2
  exit 1
fi

# Copy the build's own settings when they exist (same HyperFrames version as the template).
for f in hyperframes.json package.json; do
  if [ ! -f "$ov/$f" ] && [ -f "$build/$f" ]; then
    cp "$build/$f" "$ov/$f"
    echo "added $f"
  fi
done

if [ ! -f "$ov/meta.json" ]; then
  printf '{\n  "id": "%s-overlay",\n  "name": "%s-overlay"\n}\n' "$name" "$name" > "$ov/meta.json"
  echo "added meta.json"
fi

# The overlay page points at assets/... so it shares the build's assets folder through a link.
if [ ! -e "$ov/assets" ] && [ -d "$build/assets" ]; then
  ln -s ../assets "$ov/assets"
  echo "linked assets"
fi

echo "Overlay project ready: $ov"
