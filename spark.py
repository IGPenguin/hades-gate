import os
import subprocess

# --- PATH CONFIGURATION ---
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

    # The Combined Prompt Ritual
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
    
    # Execute the Gemini CLI
    result = subprocess.run(
        ["gemini", "-p", combined_prompt],
        capture_output=True,
        text=True
    )

    # All this logic must live INSIDE the ignite() function
    if result.returncode == 0:
        output = result.stdout.strip()
        with open(PRIONS, 'w') as f:
            f.write(output)
        
        # --- ECHO TO TERMINAL ---
        print("\n" + "="*40)
        print("🧬 THE PRIONS HAVE MATERIALIZED")
        print("="*40)
        print(output)
        print("="*40)
        print(f"\n✨ Proposals saved to {PRIONS}")
    else:
        print(f"❌ Ignition failed: {result.stderr}")

if __name__ == "__main__":
    ignite()