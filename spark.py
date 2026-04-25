import os
import subprocess
import threading
import time
import sys
import glob

# --- PATH CONFIGURATION ---
PROJECT_ROOT = os.getcwd()  # Assumes you run from the project folder
HADES_PATH = os.path.join(PROJECT_ROOT, ".hades")
MANIFESTO = os.path.join(HADES_PATH, "manifesto.md")
PAPYRUS = os.path.join(HADES_PATH, "papyrus.md")
STYX = os.path.join(HADES_PATH, "styx.md")
PRIONS = os.path.join(HADES_PATH, "prions.md")
ARCHE = os.path.join(HADES_PATH, "arche.md")  # The project blueprint

def spinner():
    """A simple terminal spinner to show life in the void."""
    chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    i = 0
    while getattr(threading.current_thread(), "do_run", True):
        sys.stdout.write(f"\r{chars[i % len(chars)]} Sending seeds to the void...")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write("\r✨ The void has answered.      \n")

def cultivate_arche():
    """Extracts the project DNA and writes it to arche.md."""
    print("🌱 Cultivating the Arche (Python Edition)...")
    
    with open(ARCHE, "w") as arche:
        arche.write(f"# THE ARCHE: PROJECT DNA\nInscribed: {time.ctime()}\n\n")

        # 1. Identity (CLAUDE.md)
        claude_path = os.path.join(PROJECT_ROOT, "CLAUDE.md")
        if os.path.exists(claude_path):
            with open(claude_path, "r") as f:
                arche.write(f"## Project Identity (CLAUDE.md)\n{f.read()}\n\n")

        # 2. The Labyrinth (Directory Structure)
        arche.write("## The Labyrinth\n```text\n")
        for root, dirs, files in os.walk(PROJECT_ROOT):
            # Exclude noise
            dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '_site', 'assets', '.hades']]
            level = root.replace(PROJECT_ROOT, '').count(os.sep)
            indent = ' ' * 4 * (level)
            arche.write(f"{indent}{os.path.basename(root)}/\n")
            sub_indent = ' ' * 4 * (level + 1)
            for f in files:
                if not f.startswith('.'):
                    arche.write(f"{sub_indent}{f}\n")
        arche.write("```\n\n")

        # 3. Logic Headers (Scanning JS directory)
        js_dir = os.path.join(PROJECT_ROOT, "js")
        if os.path.exists(js_dir):
            arche.write("## Core Logic Headers\n")
            for f_path in glob.glob(f"{js_dir}/*.js"):
                filename = os.path.basename(f_path)
                with open(f_path, "r") as f:
                    # Grab first 100 lines
                    content = "".join([next(f, "") for _ in range(100)])
                    arche.write(f"### {filename}\n```javascript\n{content}\n```\n\n")

    print(f"✨ Arche inscribed at {ARCHE}")

def ignite():
    # Basic existence check for core files
    for file_path in [MANIFESTO, PAPYRUS, STYX]:
        if not os.path.exists(file_path):
            print(f"❌ Error: {file_path} not found.")
            return

    # Read the core framework files
    with open(MANIFESTO, 'r') as f: manifesto = f.read()
    with open(PAPYRUS, 'r') as f: papyrus = f.read()
    with open(STYX, 'r') as f: styx = f.read()

    # Attempt to read the Arche (Project DNA) if it exists
    arche_context = ""
    if os.path.exists(ARCHE):
        with open(ARCHE, 'r') as f:
            arche_context = f"\n--- THE ARCHE (PROJECT DNA) ---\n{f.read()}\n"

    # Construct the Omnipotent Prompt
    combined_prompt = f"""
{manifesto}
{arche_context}

--- STRUCTURE TO FOLLOW ---
{papyrus}

--- CURRENT SEEDS FROM THE STYX ---
{styx}

INSTRUCTION: 
Using the Arche as your ground truth and the Styx as your objective, generate 3 Prions. 
Ensure the proposals account for the non-linear, random-path nature of the project.
Output ONLY the markdown content for prions.md.
"""

    # Start the spinner in a separate thread
    t = threading.Thread(target=spinner)
    t.start()

    try:
        # Strike the flint: Call Gemini CLI
        result = subprocess.run(
            ["gemini", "-p", combined_prompt],
            capture_output=True,
            text=True
        )
    finally:
        # Ensure the spinner stops even on crash
        t.do_run = False
        t.join()

    # Materialize the results
    if result.returncode == 0:
        output = result.stdout.strip()
        with open(PRIONS, 'w') as f:
            f.write(output)
        
        print("\n" + "="*40)
        print("🧬 THE PRIONS HAVE MATERIALIZED")
        print("="*40)
        print(output)
        print("="*40)
        print(f"\n✨ Proposals saved to {PRIONS}")
    else:
        print(f"\n❌ Ignition failed: {result.stderr}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "seed":
        cultivate_arche()
    else:
        ignite()