#!/bin/bash
# Installs the Hades Gate /hades skill into Claude Code.

set -e

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
PLUGIN_CACHE="$HOME/.claude/plugins/cache/local/hades/1.0.0"
HADES_CONFIG="$HOME/.claude/hades"
PLUGINS_JSON="$HOME/.claude/plugins/installed_plugins.json"

echo "🔥 Installing Hades Gate skill..."

mkdir -p "$PLUGIN_CACHE/skills/hades"
mkdir -p "$HADES_CONFIG"

cp "$REPO_DIR/claude-skill/skills/hades/SKILL.md" "$PLUGIN_CACHE/skills/hades/SKILL.md"
cp "$REPO_DIR/.hades/papyrus.md" "$HADES_CONFIG/papyrus.md"
cp "$REPO_DIR/.hades/manifesto.md" "$HADES_CONFIG/manifesto.md"

python3 - "$PLUGIN_CACHE" "$PLUGINS_JSON" << 'EOF'
import json, os, sys
from datetime import datetime, timezone

install_path = sys.argv[1]
plugins_json = sys.argv[2]

with open(plugins_json) as f:
    data = json.load(f)

now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.000Z')
data['plugins']['hades@local'] = [{
    'scope': 'user',
    'installPath': install_path,
    'version': '1.0.0',
    'installedAt': now,
    'lastUpdated': now
}]

with open(plugins_json, 'w') as f:
    json.dump(data, f, indent=2)
EOF

echo "✨ Done. Restart Claude Code, then type /hades in any project."
