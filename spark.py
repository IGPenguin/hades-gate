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
    # Safety check
    for file_path in [MANIFESTO, PAPYRUS, STYX]:
        if not os.path.exists(file_path):
            print(f"❌ Error: {file_path} not found.")
            return

    with open(MANIFESTO, 'r') as f: manifesto = f.read()
    with open(PAPYRUS, 'r') as f: papyrus = f.read()
    with open(STYX, 'r') as f: styx = f.read()

    # We "bake" the manifesto into the prompt since --system failed
    combined_prompt = f"""
{manifesto}

STRUCTURE TO FOLLOW:
{papyrus}

CURRENT SEEDS FROM THE STYX:
{styx}

INSTRUCTION: 
Generate the 3 Prions based on the latest seeds. 
Output ONLY the markdown content for prions.md.
"""

    print("⚡ Sending seeds to the void...")
    
    # Using -p/--prompt as suggested by your CLI error
    result = subprocess.run(
        ["gemini", "-p", combined_prompt],
        capture_output=True,
        text=True
    )

if result.returncode == 0:
        output = result.stdout.strip()
        with open(PRIONS, 'w') as f:
            f.write(output)
        
        # --- NEW: ECHO TO TERMINAL ---
        print("\n" + "="*40)
        print("🧬 THE PRIONS HAVE MATERIALIZED")
        print("="*40)
        # We'll print the output so you can see the options immediately
        print(output)
        print("="*40)
        print(f"\n✨ Proposals saved to {PRIONS}")
    else:
        print(f"❌ Ignition failed: {result.stderr}")

if __name__ == "__main__":
    ignite()