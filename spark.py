import os
import subprocess

# --- UPDATE THIS LINE TO YOUR ACTUAL PATH ---
# We use os.path.expanduser to handle the '~' correctly
HADES_PATH = os.path.expanduser("~/Repositories/hades-gate/.hades")

MANIFESTO = os.path.join(HADES_PATH, "manifesto.md")
PAPYRUS = os.path.join(HADES_PATH, "papyrus.md")
STYX = os.path.join(HADES_PATH, "styx.md")
PRIONS = os.path.join(HADES_PATH, "prions.md")

def ignite():
    # Safety check: Do the files actually exist?
    for file_path in [MANIFESTO, PAPYRUS, STYX]:
        if not os.path.exists(file_path):
            print(f"❌ Error: {file_path} not found.")
            return

    with open(MANIFESTO, 'r') as f: manifesto = f.read()
    with open(PAPYRUS, 'r') as f: papyrus = f.read()
    with open(STYX, 'r') as f: styx = f.read()

    # Construct the prompt
    full_prompt = f"Using this structure: {papyrus}\n\nAnalyze these seeds: {styx}"

    print("⚡ Sending seeds to the void...")
    
    # This calls your local gemini CLI
    # Adjust the command name if your gemini CLI uses a different trigger
    result = subprocess.run(
        ["gemini", "--system", manifesto, full_prompt],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        with open(PRIONS, 'w') as f:
            f.write(result.stdout)
        print(f"🦠 Prions materialized in {PRIONS}")
    else:
        print(f"❌ Ignition failed: {result.stderr}")

if __name__ == "__main__":
    ignite()