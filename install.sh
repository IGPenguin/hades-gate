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
echo "🐚 Shell Integration"
echo "To use 'hades' from anywhere, you can:"
echo "A) Add this directory to your PATH"
echo "B) Create an alias in your .zshrc or .bashrc"

echo -e "\nRecommended alias (copy and paste into your .zshrc):"
echo "alias hades='$GATE_HOME/hades'"

# 4. Finalize
echo -e "\n✨ Hades Gate setup complete."
echo "Usage:"
echo "  hades seed              # Cultivate the Arche"
echo "  hades genesis \"intent\"  # Carve a seed"
echo "  hades ignite            # Strike the flint"
