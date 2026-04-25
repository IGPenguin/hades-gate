import os
import re
import time
import glob
import sys
import subprocess
import threading

# --- PATH CONFIGURATION ---
HADES_PATH = os.path.expanduser("~/Repositories/hades-gate/.hades")
MANIFESTO = os.path.join(HADES_PATH, "manifesto.md")
PAPYRUS = os.path.join(HADES_PATH, "papyrus.md")
STYX = os.path.join(HADES_PATH, "styx.md")
PRIONS = os.path.join(HADES_PATH, "prions.md")
ARCHE = os.path.join(HADES_PATH, "arche.md")
STYX_ARCHIVE = os.path.join(HADES_PATH, "styx_archive.md")

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

def parse_js_skeleton(filepath):
    """Parses a JS file and extracts only function signatures and classes."""
    skeleton = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if re.match(r'^(async\s+)?function\s+\w+', line):
                    skeleton.append("  " + line.split('{')[0].strip() + " { ... }")
                elif line.startswith("class "):
                    skeleton.append("  " + line.split('{')[0].strip() + " { ... }")
                elif re.match(r'^(const|let|var)\s+\w+\s*=\s*(\(.*?\)\s*=>|function|new\s+)', line):
                    clean_line = line.split('{')[0].rstrip('=> ').strip()
                    if "=>" not in clean_line and "function" not in clean_line:
                        clean_line += " =>"
                    skeleton.append("  " + clean_line + " { ... }")
    except Exception as e:
        skeleton.append(f"  // Error reading file: {e}")
    return skeleton

def cultivate_arche():
    """Extracts the project DNA and writes a clean, token-efficient arche.md."""
    print("🌱 Cultivating the Semantic Arche...")
    
    PROJECT_ROOT = os.getcwd() 
    
    with open(ARCHE, "w", encoding="utf-8") as arche:
        arche.write(f"# THE ARCHE: PROJECT DNA\nInscribed: {time.ctime()}\n\n")

        # 1. Core Identity (The FULL CLAUDE.md)
        claude_path = os.path.join(PROJECT_ROOT, "CLAUDE.md")
        if os.path.exists(claude_path):
            arche.write("## Project Identity & Rules\n")
            with open(claude_path, "r", encoding="utf-8") as f:
                arche.write(f.read().strip() + "\n\n")

        # 2. The Labyrinth (Strictly filtered directory map)
        arche.write("## The Labyrinth\n```text\n")
        # Aggressive blacklist for build artifacts and caches
        ignore_dirs = {
            '.git', 'node_modules', '_site', 'assets', '.hades', 
            'fonts', '.jekyll-cache', '_jekyll-cache', '.sass-cache', 'cleanup'
        }
        
        for root, dirs, files in os.walk(PROJECT_ROOT):
            dirs[:] = [d for d in dirs if d not in ignore_dirs]
            level = root.replace(PROJECT_ROOT, '').count(os.sep)
            indent = ' ' * 4 * (level)
            folder_name = os.path.basename(root)
            if folder_name and folder_name != os.path.basename(PROJECT_ROOT): 
                arche.write(f"{indent}{folder_name}/\n")
            sub_indent = ' ' * 4 * (level + 1)
            for f in files:
                if not f.startswith('.') and not f.endswith(('png', 'jpg', 'svg', 'eot', 'ttf', 'woff', 'woff2')):
                    arche.write(f"{sub_indent}{f}\n")
        arche.write("```\n\n")

        # 3. The API Surface (Parsed JS Skeletons)
        js_dir = os.path.join(PROJECT_ROOT, "js")
        if os.path.exists(js_dir):
            arche.write("## Core API Surface\n")
            arche.write("*(Abstracted function signatures and classes)*\n\n")
            for f_path in glob.glob(f"{js_dir}/*.js"):
                filename = os.path.basename(f_path)
                skeleton = parse_js_skeleton(f_path)
                if skeleton:
                    arche.write(f"### {filename}\n```javascript\n")
                    arche.write("\n".join(skeleton))
                    arche.write("\n```\n\n")

    print(f"✨ Arche inscribed at {ARCHE}")

def check_ghostwire():
    """Warn if the cwd has no .hades symlink pointing to hades-gate."""
    local_hades = os.path.join(os.getcwd(), ".hades")
    if os.path.islink(local_hades):
        target = os.path.realpath(local_hades)
        if target != os.path.realpath(HADES_PATH):
            print(f"⚠️  Warning: .hades symlink points to {target}, not {HADES_PATH}")
    elif os.path.isdir(local_hades):
        print("⚠️  Warning: .hades is a plain directory, not a Ghostwire symlink.")
    # No .hades at all means we're running from hades-gate itself — fine.

def archive_styx(styx_content):
    """Append consumed seeds to styx_archive.md and clear styx.md."""
    with open(STYX_ARCHIVE, 'a', encoding='utf-8') as f:
        f.write(f"\n\n## === Ignited {time.strftime('%Y-%m-%d %H:%M')} ===\n")
        f.write(styx_content.strip())
    open(STYX, 'w').close()
    print("📦 Seeds archived. Styx cleared for the next ritual.")

def ignite():
    check_ghostwire()
    for file_path in [MANIFESTO, PAPYRUS, STYX]:
        if not os.path.exists(file_path):
            print(f"❌ Error: {file_path} not found.")
            return

    with open(MANIFESTO, 'r') as f: manifesto = f.read()
    with open(PAPYRUS, 'r') as f: papyrus = f.read()
    with open(STYX, 'r') as f: styx = f.read()

    if not styx.strip():
        print("⚠️  Styx is empty — carve a seed first with: hades genesis 'your intent'")
        return

    arche_context = ""
    if os.path.exists(ARCHE):
        age_hours = (time.time() - os.path.getmtime(ARCHE)) / 3600
        if age_hours > 24:
            print(f"⚠️  Arche is {int(age_hours / 24)}d old — consider running 'hades seed' first.")
        with open(ARCHE, 'r') as f:
            arche_context = f"\n--- THE ARCHE (PROJECT DNA) ---\n{f.read()}\n"
    else:
        print("⚠️  No Arche found — Gemini will have no project context. Run 'hades seed' first.")

    combined_prompt = f"""
{manifesto}
{arche_context}

--- STRUCTURE TO FOLLOW ---
{papyrus}

--- CURRENT SEEDS FROM THE STYX ---
{styx}

INSTRUCTION:
Using the Arche as your ground truth and the Styx as your objective, generate 3 Prions.
Output ONLY the markdown content for prions.md.
Do NOT include citation markers (e.g. [cite: X], [cite_start]) anywhere in your output.
"""

    t = threading.Thread(target=spinner)
    t.start()

    try:
        result = subprocess.run(
            ["gemini", "-p", combined_prompt],
            capture_output=True,
            text=True
        )
    finally:
        t.do_run = False
        t.join()

    if result.returncode == 0:
        output = result.stdout.strip()
        # Strip Gemini citation artifacts
        output = re.sub(r'\[cite_start\]', '', output)
        output = re.sub(r'\s*\[cite:\s*[\d,\s]+\]', '', output)
        with open(PRIONS, 'w') as f:
            f.write(output)
        
        print("\n" + "="*40)
        print("🧬 THE PRIONS HAVE MATERIALIZED")
        print("="*40)
        print(output)
        print("="*40)
        print(f"\n✨ Proposals saved to {PRIONS}")
        archive_styx(styx)
    else:
        print(f"\n❌ Ignition failed: {result.stderr}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "seed":
        cultivate_arche()
    else:
        ignite()