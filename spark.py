import os
import re
import time
import glob
import sys
import subprocess
import threading

# --- PATH CONFIGURATION ---
HADES_HOME = os.path.dirname(os.path.abspath(__file__))
HADES_PATH = os.path.join(HADES_HOME, ".hades")
MANIFESTO = os.path.join(HADES_PATH, "manifesto.md")
PAPYRUS = os.path.join(HADES_PATH, "papyrus.md")
STYX = os.path.join(HADES_PATH, "styx.md")
PRIONS = os.path.join(HADES_PATH, "prions.md")
ARCHE = os.path.join(HADES_PATH, "arche.md")
STYX_ARCHIVE = os.path.join(HADES_PATH, "styx_archive.md")
EREBUS_ENV = os.path.join(HADES_PATH, "erebus.env")

def load_erebus():
    """Load GEMINI_API_KEY from erebus.env if it exists."""
    if os.path.exists(EREBUS_ENV):
        with open(EREBUS_ENV, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if line.startswith("export "):
                    line = line.replace("export ", "")
                if "=" in line:
                    key, value = line.split("=", 1)
                    os.environ[key] = value.strip("'\"")

def carve_seed(intent):
    """Appends the user's intent to styx.md."""
    timestamp = time.strftime("%Y-%m-%d %H:%M")
    with open(STYX, "a", encoding="utf-8") as f:
        f.write(f"\n## Seed {timestamp}\n{intent}\n---\n")
    print(f"📜 Seed carved into the Styx at {STYX}")

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

        # 1. Core Identity (The FULL CLAUDE.md and TODOs.md)
        claude_path = os.path.join(PROJECT_ROOT, "CLAUDE.md")
        todo_paths = [os.path.join(PROJECT_ROOT, "TODOs.md"), os.path.join(PROJECT_ROOT, "TODO.md")]
        
        if os.path.exists(claude_path):
            arche.write("## Project Identity & Rules\n")
            with open(claude_path, "r", encoding="utf-8") as f:
                arche.write(f.read().strip() + "\n\n")
        
        for tp in todo_paths:
            if os.path.exists(tp):
                filename = os.path.basename(tp)
                arche.write(f"## Project Backlog ({filename})\n")
                with open(tp, "r", encoding="utf-8") as f:
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
        # If we are in the hades-gate repo itself, this is expected
        if os.path.realpath(local_hades) == os.path.realpath(HADES_PATH):
            return
        print("⚠️  Warning: .hades is a plain directory, not a Ghostwire symlink.")

def archive_styx(styx_content):
    """Append consumed seeds to styx_archive.md and clear styx.md."""
    with open(STYX_ARCHIVE, 'a', encoding='utf-8') as f:
        f.write(f"\n\n## === Ignited {time.strftime('%Y-%m-%d %H:%M')} ===\n")
        f.write(styx_content.strip())
    open(STYX, 'w').close()
    print("📦 Seeds archived. Styx cleared for the next ritual.")

def ignite():
    load_erebus()
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
        # Only join if t was actually started and is still running
        if t.is_alive():
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

def summon_task(query):
    """Searches for a task in TODOs.md and carves it as a seed."""
    PROJECT_ROOT = os.getcwd()
    todo_paths = [os.path.join(PROJECT_ROOT, "TODOs.md"), os.path.join(PROJECT_ROOT, "TODO.md")]
    found_lines = []
    
    for tp in todo_paths:
        if os.path.exists(tp):
            with open(tp, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for i, line in enumerate(lines):
                    if query.lower() in line.lower():
                        # Try to capture context (like sub-bullets if it's a list)
                        task_block = line.strip()
                        # Simple logic: grab next lines if they are indented
                        for j in range(i + 1, min(i + 5, len(lines))):
                            if lines[j].startswith("  ") or lines[j].startswith("\t"):
                                task_block += "\n" + lines[j].strip()
                            else:
                                break
                        found_lines.append(task_block)
    
    if not found_lines:
        print(f"❌ No tasks matching '{query}' found in TODOs.md")
        return

    combined_seeds = "\n\n".join(found_lines)
    carve_seed(f"Summoned from Backlog:\n{combined_seeds}")
    print(f"🪄 {len(found_lines)} task(s) summoned to the Styx.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "survey":
            cultivate_arche()
        elif cmd == "seed":
            if len(sys.argv) > 2:
                carve_seed(sys.argv[2])
            else:
                print("❌ Error: 'seed' requires an intent message.")
                print("Usage: hades seed 'Your intent here'")
        elif cmd == "summon":
            if len(sys.argv) > 2:
                summon_task(sys.argv[2])
            else:
                print("❌ Error: 'summon' requires a search query.")
                print("Usage: hades summon 'query'")
        elif cmd == "ignite":
            ignite()
        else:
            print(f"Unknown command: {cmd}")
            print("Usage: hades [survey | seed 'intent' | summon 'query' | ignite]")
    else:
        ignite()
