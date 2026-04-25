<p align="center">
  <img src="assets/header.svg" width="100%" alt="Hades Gate Header">
</p>

## Hades Gate: The Primordial AI Forge

**Objective:** Materialize ideas into reality (Code) through a structured, multi-model feedback loop.

Hades Gate separates the **Architect** (Gemini) from the **Builder** (Claude). Gemini analyzes your project and proposes three implementation paths. You pick one, then tell Claude to execute it in your active session — where full context already lives.

---

### 🏛️ The Architecture of the Underworld

* **The Styx (`styx.md`):** Where you carve seeds — raw intent, tasks, objectives.
* **The Arche (`arche.md`):** Project DNA snapshot (CLAUDE.md + file tree + API surface). Built by `hades seed`.
* **The Spark (`spark.py`):** Sends Arche + Seeds to Gemini. Three proposals materialize.
* **The Prions (`prions.md`):** Gemini's output — three infectious paths ready to mutate your codebase.

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

### 🕹️ Commands

| Command | Action |
| :--- | :--- |
| `hades seed` | **Cultivate the Arche.** Scans your project and writes the DNA map to `arche.md`. |
| `hades genesis "Intent"` | **Carve a Seed.** Appends your intent to `styx.md`. |
| `hades ignite` | **Strike the Flint.** Sends Arche + Seeds to Gemini. Three proposals land in `prions.md`. |

---

### 🔄 The Workflow Loop

1. **Map the Universe:** `hades seed` — update the Arche after any structural changes.
2. **Speak Intent:** `hades genesis "what you want"` — log the objective.
3. **Consult the Fates:** `hades ignite` — Gemini returns three paths in `prions.md`.
4. **Materialize:**
   - **In your active Claude session:** say *"implement Option B"* — Claude reads `prions.md` with full context.
   - **From the terminal:** `hades execute B` — bridges to Claude CLI directly.

---

### 🛡️ Safety & Privacy
* **Ghostwire Protocol:** `.hades/` is symlinked — your seeds, API key, and generated files stay in `hades-gate`, never committed to your project.
* **Git Integrity:** `styx.md`, `arche.md`, `prions.md`, and `erebus.env` are all gitignored.
