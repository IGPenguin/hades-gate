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
    for file_path in [MANIFESTO, PAPYRUS, STYX]:
        if not os.path.exists(file_path):
            print(f"❌ Error: {file_path} not found.")
            return

    with open(MANIFESTO, 'r') as f: manifesto = f.read()
    with open(PAPYRUS, 'r') as f: papyrus = f.read()
    with open(STYX, 'r') as f: styx = f.read()

    combined_prompt = f"{manifesto}\n\nSTRUCTURE:\n{papyrus}\n\nSEEDS:\n{styx}\n\nOutput ONLY prions.md markdown."

    # Start the spinner in a separate thread
    t = threading.Thread(target=spinner)
    t.start()

    try:
        result = subprocess.run(
            ["gemini", "-p", combined_prompt],
            capture_output=True,
            text=True
        )
    finally:
        # Stop the spinner
        t.do_run = False
        t.join()

    if result.returncode == 0:
        output = result.stdout.strip()
        with open(PRIONS, 'w') as f:
            f.write(output)
        
        print("\n" + "="*40)
        print("🧬 THE PRIONS HAVE MATERIALIZED")
        print("="*40)
        print(output)
        print("="*40)
    else:
        print(f"\n❌ Ignition failed: {result.stderr}")

if __name__ == "__main__":
    ignite()