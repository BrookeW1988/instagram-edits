#!/bin/bash
# setup_python.sh: make the skill's own little Python toolbox, once.
#
# WHY a separate "venv" (a private Python folder): it keeps these extras away from anything else on your Mac,
# so nothing else breaks and it's easy to delete (just remove ~/.instagram-edits).
#
#   bash setup_python.sh   -> installs Pillow, which draws the boxed text hooks and number cards as PNGs
#                             (Edits' tools can't put a background box behind text).
#
# Claude asks before running this. Needs python3 (macOS offers to install it the first time you type python3).

set -euo pipefail

venv="$HOME/.instagram-edits/venv"

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 not found. Type python3 in Terminal once and macOS will offer to install it." >&2
  exit 2
fi

if [ ! -x "$venv/bin/python" ]; then
  mkdir -p "$HOME/.instagram-edits"
  python3 -m venv "$venv"
  echo "made $venv"
fi

"$venv/bin/python" -m pip install --quiet --upgrade pip
"$venv/bin/python" -m pip install --quiet pillow
echo "Pillow ready"

echo "$venv/bin/python"
