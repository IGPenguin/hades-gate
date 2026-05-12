#!/bin/bash
# Installs the Hades Gate /hades skill into Claude Code.

set -e

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
PLUGIN_CACHE="$HOME/.claude/plugins/cache/local/hades/1.0.0"
HADES_CONFIG="$HOME/.claude/hades"
PLUGINS_JSON="$HOME/.claude/plugins/installed_plugins.json"

echo "🔥 Installing Hades Gate skill..."

mkdir -p "$PLUGIN_CACHE/skills/hades"
mkdir -p "$PLUGIN_CACHE/.claude-plugin"
mkdir -p "$HADES_CONFIG"

cp "$REPO_DIR/claude-skill/skills/hades/SKILL.md" "$PLUGIN_CACHE/skills/hades/SKILL.md"

cat > "$PLUGIN_CACHE/.claude-plugin/plugin.json" << 'PLUGINJSON'
{
  "name": "hades",
  "description": "Hades Gate — generates six orthogonal implementation paths (The Hexalogy) plus a synthesis for any idea or task",
  "author": {
    "name": "Adam Svoboda",
    "email": "eidamsvoboda@gmail.com"
  }
}
PLUGINJSON
cp "$REPO_DIR/.hades/papyrus.md" "$HADES_CONFIG/papyrus.md"
cp "$REPO_DIR/.hades/manifesto.md" "$HADES_CONFIG/manifesto.md"

SETTINGS_JSON="$HOME/.claude/settings.json"

python3 - "$PLUGIN_CACHE" "$PLUGINS_JSON" "$SETTINGS_JSON" << 'EOF'
import json, os, sys
from datetime import datetime, timezone

install_path = sys.argv[1]
plugins_json = sys.argv[2]
settings_json = sys.argv[3]

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

with open(settings_json) as f:
    settings = json.load(f)

settings.setdefault('enabledPlugins', {})['hades@local'] = True

with open(settings_json, 'w') as f:
    json.dump(settings, f, indent=2)
EOF

echo "✨ Done. Restart Claude Code, then type /hades in any project."
