#!/bin/bash

# --- COLORS ---
HEADER='\033[95m'
OKGREEN='\033[92m'
FAIL='\033[91m'
ENDC='\033[0m'
BOLD='\033[1m'

echo -e "${HEADER}🔱 HADES GATE: Installation Ritual${ENDC}"

# 1. Check Python
if ! command -v python3 &> /dev/null; then
    echo -e "${FAIL}❌ python3 is not installed. Please install it first.${ENDC}"
    exit 1
fi

# 2. Check Gemini CLI
if ! command -v gemini &> /dev/null; then
    echo -e "${FAIL}❌ 'gemini' CLI is not found in PATH.${ENDC}"
    echo "Please ensure the Gemini CLI is installed and accessible."
    exit 1
fi

# 3. Setup Environment
HADES_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
ENV_FILE="$HADES_DIR/.hades/erebus.env"

if [ ! -f "$ENV_FILE" ]; then
    echo "🔑 Setting up your Gemini API Key..."
    read -p "Enter your GEMINI_API_KEY: " API_KEY
    echo "GEMINI_API_KEY=$API_KEY" > "$ENV_FILE"
    chmod 600 "$ENV_FILE"
    echo -e "${OKGREEN}✨ API Key secured in .hades/erebus.env${ENDC}"
else
    echo "✅ .hades/erebus.env already exists."
fi

# 4. Final Instructions
echo -e "\n${BOLD}Setup Complete!${ENDC}"
echo -e "To use the 'hades' command from anywhere, add this to your .zshrc or .bashrc:"
echo -e "${BOLD}alias hades='python3 $HADES_DIR/hades.py'${ENDC}"
echo -e "\n${BOLD}Quick Start:${ENDC}"
echo "1. cd your-project"
echo "2. hades link"
echo "3. hades survey"
echo "4. hades seed 'My idea'"
echo "5. hades ignite"
