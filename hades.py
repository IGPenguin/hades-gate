import os
import re
import time
import glob
import sys
import subprocess
import threading
import argparse

# --- COLORS ---
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def log(msg, color=Colors.ENDC):
    print(f"{color}{msg}{Colors.ENDC}")

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
    try:
        with open(STYX, "a", encoding="utf-8") as f:
            f.write(f"\n## Seed {timestamp}\n{intent}\n---\n")
        log(f"📜 Seed carved into the Styx at {STYX}", Colors.OKGREEN)
    except Exception as e:
        log(f"❌ Failed to carve seed: {e}", Colors.FAIL)

def spinner():
    """A simple terminal spinner to show life in the void."""
    chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    i = 0
    while getattr(threading.current_thread(), "do_run", True):
        sys.stdout.write(f"\r{Colors.OKCYAN}{chars[i % len(chars)]}{Colors.ENDC} Sending seeds to the void...")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write(f"\r{Colors.OKGREEN}✨ The void has answered.      {Colors.ENDC}\n")

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
    log("🌱 Cultivating the Semantic Arche...", Colors.OKBLUE)
    
    PROJECT_ROOT = os.getcwd() 
    
    try:
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

        log(f"✨ Arche inscribed at {ARCHE}", Colors.OKGREEN)
    except Exception as e:
        log(f"❌ Failed to cultivate Arche: {e}", Colors.FAIL)

def check_drift():
    """Detect significant code changes since last survey using git."""
    if not os.path.exists(ARCHE):
        return True
    
    last_survey_time = os.path.getmtime(ARCHE)
    
    # Check if there are uncommitted changes or recent commits
    try:
        # Get count of changed lines since the last survey time
        # We use git log to see if any commits happened, and git diff for working tree
        diff_cmd = ["git", "diff", "--shortstat"]
        diff_res = subprocess.run(diff_cmd, capture_output=True, text=True)
        
        if diff_res.stdout.strip():
            log(f"⚠️ Project drift detected: {diff_res.stdout.strip()}", Colors.WARNING)
            return True
            
        # Also check if recent commits happened since the file was written
        log_cmd = ["git", "log", "--since", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(last_survey_time)), "--oneline"]
        log_res = subprocess.run(log_cmd, capture_output=True, text=True)
        if log_res.stdout.strip():
            log("⚠️ New commits detected since last survey.", Colors.WARNING)
            return True
            
    except Exception:
        # Fallback to simple time check if not a git repo
        age_hours = (time.time() - last_survey_time) / 3600
        if age_hours > 24:
            return True
            
    return False

def link_project():
    """Creates a Ghostwire symlink in the current directory."""
    target = os.path.join(os.getcwd(), ".hades")
    if os.path.exists(target):
        if os.path.islink(target):
            log(f"🔗 Ghostwire already exists: {os.path.realpath(target)}", Colors.OKBLUE)
        else:
            log("❌ .hades exists but is not a symlink.", Colors.FAIL)
            return
    else:
        try:
            os.symlink(HADES_PATH, target)
            log(f"✨ Ghostwire linked: {target} -> {HADES_PATH}", Colors.OKGREEN)
        except Exception as e:
            log(f"❌ Failed to create symlink: {e}", Colors.FAIL)

def ignite():
    load_erebus()
    
    # Essential framework files
    for file_path in [MANIFESTO, PAPYRUS]:
        if not os.path.exists(file_path):
            log(f"❌ Error: {file_path} not found.", Colors.FAIL)
            return

    with open(MANIFESTO, 'r') as f: manifesto = f.read()
    with open(PAPYRUS, 'r') as f: papyrus = f.read()
    
    styx = ""
    if os.path.exists(STYX):
        with open(STYX, 'r') as f: 
            styx = f.read()

    if not styx.strip():
        log("⚠️  Styx is empty — carve a seed first with: hades seed 'your intent'", Colors.WARNING)
        return

    if check_drift():
        choice = input(f"{Colors.BOLD}👉 Project state has drifted. Update survey (arche.md)? [Y/n]: {Colors.ENDC}").lower()
        if choice != 'n':
            cultivate_arche()

    arche_context = ""
    if os.path.exists(ARCHE):
        with open(ARCHE, 'r') as f:
            arche_context = f"\n--- THE ARCHE (PROJECT DNA) ---\n{f.read()}\n"

    combined_prompt = f"""
{manifesto}
{arche_context}

--- STRUCTURE TO FOLLOW ---
{papyrus}

--- CURRENT SEEDS FROM THE STYX ---
{styx}

INSTRUCTION:
Using the Arche as your ground truth and the Styx as your objective, generate Prions following the structure in Papyrus.
Output ONLY the markdown content for prions.md.
Do NOT include citation markers anywhere in your output.
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
        if t.is_alive():
            t.join()

    if result.returncode == 0:
        output = result.stdout.strip()
        # Clean Gemini artifacts
        output = re.sub(r'\[cite_start\]', '', output)
        output = re.sub(r'\s*\[cite:\s*[\d,\s]+\]', '', output)
        
        with open(PRIONS, 'w') as f:
            f.write(output)
        
        print("\n" + Colors.BOLD + "="*40 + Colors.ENDC)
        log("🧬 THE PRIONS HAVE MATERIALIZED", Colors.HEADER)
        print(Colors.BOLD + "="*40 + Colors.ENDC)
        print(output)
        print(Colors.BOLD + "="*40 + Colors.ENDC)
        log(f"\n✨ Proposals saved to {PRIONS}", Colors.OKGREEN)
        
        # Append to archive and clear styx
        timestamp = time.strftime('%Y-%m-%d %H:%M')
        with open(STYX_ARCHIVE, 'a', encoding='utf-8') as f:
            f.write(f"\n\n# RITUAL ARCHIVE: {timestamp}\n## SEEDS\n{styx.strip()}\n\n## OUTCOMES\n{output.strip()}\n" + "-"*40 + "\n")
        open(STYX, 'w').close()
        log("📦 Ritual archived. Styx cleared.", Colors.OKBLUE)
    else:
        log(f"\n❌ Ignition failed: {result.stderr}", Colors.FAIL)

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
                        task_block = line.strip()
                        for j in range(i + 1, min(i + 5, len(lines))):
                            if lines[j].startswith("  ") or lines[j].startswith("\t"):
                                task_block += "\n" + lines[j].strip()
                            else:
                                break
                        found_lines.append(task_block)
    
    if not found_lines:
        log(f"❌ No tasks matching '{query}' found in TODOs.md", Colors.FAIL)
        return

    combined_seeds = "\n\n".join(found_lines)
    carve_seed(f"Summoned from Backlog:\n{combined_seeds}")
    log(f"🪄 {len(found_lines)} task(s) summoned to the Styx.", Colors.OKGREEN)

def show_status():
    log("--- HADES STATUS ---", Colors.BOLD)
    if os.path.exists(ARCHE):
        age_hours = (time.time() - os.path.getmtime(ARCHE)) / 3600
        drift = "DRIFTED" if check_drift() else "FRESH"
        color = Colors.WARNING if drift == "DRIFTED" else Colors.OKGREEN
        log(f"📊 Arche: {drift} ({int(age_hours)}h old)", color)
    else:
        log("📊 Arche: MISSING (Run 'hades survey')", Colors.FAIL)
    
    if os.path.exists(STYX):
        with open(STYX, 'r') as f:
            content = f.read().strip()
            count = content.count("## Seed")
            color = Colors.OKCYAN if count > 0 else Colors.ENDC
            log(f"🌱 Styx: {count} seeds waiting", color)
    
    if os.path.exists(STYX_ARCHIVE):
        size = os.path.getsize(STYX_ARCHIVE) // 1024
        log(f"📦 Archive: {size} KB", Colors.OKBLUE)

def main():
    parser = argparse.ArgumentParser(
        description=f"{Colors.HEADER}Hades Gate: Meta-framework for idea-to-execution.{Colors.ENDC}",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available rituals")

    # Survey
    subparsers.add_parser("survey", help="Cultivate the Arche (scan project DNA)")
    
    # Seed
    seed_parser = subparsers.add_parser("seed", help="Plant an idea into the Styx")
    seed_parser.add_argument("intent", help="Your implementation goal")
    
    # Summon
    summon_parser = subparsers.add_parser("summon", help="Pull a task from the project backlog")
    summon_parser.add_argument("query", help="Search term for the TODO list")
    
    # Ignite
    subparsers.add_parser("ignite", help="Strike the flint (generate proposals)")
    
    # Status
    subparsers.add_parser("status", help="Check the pulse of the Gate")
    
    # Link
    subparsers.add_parser("link", help="Create a Ghostwire symlink in the current project")

    args = parser.parse_args()

    if args.command == "survey":
        cultivate_arche()
    elif args.command == "seed":
        carve_seed(args.intent)
    elif args.command == "summon":
        summon_task(args.query)
    elif args.command == "ignite" or args.command is None:
        ignite()
    elif args.command == "status":
        show_status()
    elif args.command == "link":
        link_project()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
