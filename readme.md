<p align="center">
  <img src="assets/header.svg" width="100%" alt="Hades Gate Header">
</p>

## 🧠 Materialize your ideas into reality

Hades Gate smoothens out the "human to vibe-coding" interface by analyzing your idea proposals vs your projects and proposing three distinct implementation paths.<br>
- **Option A:** The Fast Path (Minimum Viable Result)
- **Option B:** The Dream Path (High Quality/Polished)
- **Option C:** The Experimental Path (Outside the Box)

The **Architect** (Gemini) analyzes your project, the **Builder** (Claude) executes the choosen plan in an active session — where full context already lives.

---

### ⚙️ Setup & Installation

#### 1. Clone & Install
```bash
git clone https://github.com/your-repo/hades-gate.git ~/Repositories/hades-gate
cd ~/Repositories/hades-gate
./install.sh
```
Follow the prompts to set up your `GEMINI_API_KEY`.

#### 2. Shell Function
Add the following function to your `~/.zshrc` or `~/.bashrc`. It wraps the `hades` script and adds the optional `execute` command, which bridges directly to Claude CLI:
```zsh
hades() {
    local GATE_BIN="$HOME/Repositories/hades-gate/hades"

    if [[ "$1" == "execute" ]]; then
        if [ -z "$2" ]; then
            echo "❌ Please specify Path A, B, or C."
        else
            echo "🛠️ Summoning Claude to implement Path $2..."
            claude "Analyze .hades/prions.md and implement the full logic for Option $2. Follow all rules in .hades/manifesto.md."
        fi
    else
        "$GATE_BIN" "$@"
    fi
}
```

> A plain `alias` works if you don't need `execute`. The function is preferred.

#### 3. The Ghostwire (Symlink)
Link your project into the Gate so it shares the `.hades/` state:
```bash
cd ~/Repositories/your-project
ln -s ~/Repositories/hades-gate/.hades .hades
```

---

### 🕹️ Usage

| Command | Action |
| :--- | :--- |
| `hades seed` | Scans your project and writes the DNA map to `arche.md`. |
| `hades genesis "your idea"` | Appends your idea to `styx.md`. |
| `hades ignite` | Sends Arche + Seeds to Gemini. Three proposals land in `prions.md`. |
|**Claude session:** *"implement option B"*|Claude reads `prions.md` with full context and executes the plan.|
|**(or) Terminal:** `hades execute B`|Bridges the selected `prions.md` plan execution to a clean Claude CLI session directly.|

---

### 🛡️ Safety & Privacy
* **Ghostwire Protocol:** `.hades/` is symlinked — your seeds, API key, and generated files stay in `hades-gate`, never committed to your project.
* **Git Integrity:** `styx.md`, `arche.md`, `prions.md`, and `erebus.env` are all gitignored.

---

### 🏛️ Architecture

* **The Styx (`styx.md`):** Where you carve seeds — raw intent, tasks, objectives.
* **The Arche (`arche.md`):** Project DNA snapshot (CLAUDE.md + file tree + API surface). Built by `hades seed`.
* **The Spark (`spark.py`):** Sends Arche + Seeds to Gemini. Three proposals materialize.
* **The Prions (`prions.md`):** Gemini's output — three infectious paths ready to mutate your codebase.
