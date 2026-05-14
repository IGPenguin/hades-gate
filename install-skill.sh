#!/bin/bash
# Installs the Hades Gate /hades skill into Claude Code.

set -e

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
HADES_CONFIG="$HOME/.claude/hades"

echo "🔥 Installing Hades Gate..."

# 1. Register the GitHub repo as a marketplace (idempotent)
if claude plugins marketplace list 2>/dev/null | grep -q "hades-gate"; then
    claude plugins marketplace update hades-gate 2>/dev/null || true
else
    claude plugins marketplace add IGPenguin/hades-gate --scope user
fi

# 2. Install (or update) the hades plugin
if claude plugins list 2>/dev/null | grep -q "hades@hades-gate"; then
    claude plugins update hades@hades-gate 2>/dev/null || true
else
    claude plugins install hades@hades-gate --scope user
fi

# 3. Copy user-editable config files
mkdir -p "$HADES_CONFIG"
cp "$REPO_DIR/.hades/papyrus.md" "$HADES_CONFIG/papyrus.md"
cp "$REPO_DIR/.hades/manifesto.md" "$HADES_CONFIG/manifesto.md"

echo "✨ Done. Restart Claude Code, then type /hades in any project."
