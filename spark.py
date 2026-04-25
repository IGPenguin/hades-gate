import os
import subprocess
from dotenv import load_dotenv

load_dotenv()

def run_claude_task(proposal_path):
    """Feeds a crystallized proposal to Claude Code CLI"""
    print(f"🚀 Injecting intent into execution engine...")
    # This assumes 'claude' CLI is installed
    subprocess.run(["claude", "work", "--file", proposal_path])

def cook_with_gemini(inbox_path):
    """Uses Gemini to turn raw notes into 3 proposals"""
    # Logic to call Gemini API and output to proposals.md
    print("🍳 Cooking proposals in the kitchen...")
    pass
