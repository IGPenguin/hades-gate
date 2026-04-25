import os
import subprocess
import threading
import time
import sys

# --- PATH CONFIGURATION ---
HADES_PATH = os.path.expanduser("~/Repositories/hades-gate/.hades")
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
    ignite()