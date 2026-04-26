#!/bin/bash

# Hades Gate Installation Script
echo "🏛️  Welcome to the Hades Gate Setup"

GATE_HOME=$(pwd)
HADES_DIR="$GATE_HOME/.hades"
EREBUS_ENV="$HADES_DIR/erebus.env"

# 1. Dependency Checks
echo "🔍 Checking dependencies..."
if ! command -v python3 &> /dev/null; then
    echo "❌ python3 is not installed. Please install it first."
    exit 1
fi

if ! command -v gemini &> /dev/null; then
    echo "⚠️  Gemini CLI not found on PATH. Ensure it's installed for 'ignite' to work."
fi

# 2. Setup erebus.env
if [ ! -f "$EREBUS_ENV" ]; then
    echo "🔑 API Key Setup"
    echo "To use 'ignite', you need a Gemini API Key from https://aistudio.google.com/app/apikey"
    read -p "Enter your GEMINI_API_KEY (leave empty to skip): " api_key
    if [ ! -z "$api_key" ]; then
        echo "export GEMINI_API_KEY=\"$api_key\"" > "$EREBUS_ENV"
        chmod 600 "$EREBUS_ENV"
        echo "✅ API Key saved to .hades/erebus.env"
    else
        echo "⏭️  Skipping API Key setup. You can add it later to .hades/erebus.env"
        touch "$EREBUS_ENV"
    fi
else
    echo "✅ .hades/erebus.env already exists."
fi

# 3. Setup Shell Integration
echo ""
echo "🐚 Shell Integration"
echo "Add the following function to your ~/.zshrc (includes 'hades execute' → Claude bridge):"
echo ""
echo "hades() {"
echo "    local GATE_BIN=\"$GATE_HOME/hades\""
echo "    if [[ \"\$1\" == \"execute\" ]]; then"
echo "        if [ -z \"\$2\" ]; then"
echo "            echo \"❌ Please specify Path A, B, or C.\""
echo "        else"
echo "            echo \"🛠️ Summoning Claude to implement Path \$2...\""
echo "            claude \"Analyze .hades/prions.md and implement the full logic for Option \$2. Follow all rules in .hades/manifesto.md.\""
echo "        fi"
echo "    else"
echo "        \"\$GATE_BIN\" \"\$@\""
echo "    fi"
echo "}"
echo ""
echo "  (Or use a plain alias if you don't need 'execute': alias hades='$GATE_HOME/hades')"

# 4. Finalize
echo -e "\n✨ Hades Gate setup complete."
echo "Usage:"
echo "  hades survey            # Cultivate the Arche"
echo "  hades seed \"intent\"     # Carve a seed"
echo "  hades ignite            # Strike the flint"
