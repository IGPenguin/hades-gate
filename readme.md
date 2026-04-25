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

#### 0. Dependencies
- Claude Code CLI
- Gemini CLI
- `tree` (optional, for inspection)

#### 1. Repository Structure
```text
~/Repositories/
├── hades-gate/          # The Framework
│   ├── .hades/
│   │   ├── manifesto.md # Global coding standards
│   │   ├── papyrus.md   # Proposal structure template
│   │   └── erebus.env   # API Key (git-ignored)
│   ├── spark.py         # The Python catalyst
│   └── CLAUDE.md        # Framework guidance for Claude
└── your-project/        # Your Active Project
    └── .hades -> hades-gate/.hades  # Ghostwire symlink
```

#### 2. The Ghostwire (Symlink)
Link your project into the Gate so it shares the `.hades/` state:
```bash
cd ~/Repositories/your-project
ln -s ~/Repositories/hades-gate/.hades .hades
```

#### 3. Authentication (Erebus)
Create `.hades/erebus.env` inside the `hades-gate` folder. **Do not commit this file.**
```bash
export GEMINI_API_KEY="your_google_ai_studio_key"
```

#### 4. The Terminal Function
Add the `hades()` function to your `~/.zshrc`:

```bash
hades() {
    local GATE_HOME="$HOME/Repositories/hades-gate"
    if [ -f "$GATE_HOME/.hades/erebus.env" ]; then source "$GATE_HOME/.hades/erebus.env"; fi

    case "$1" in
        genesis)
            echo -e "\n## Seed $(date +%Y-%m-%d_%H:%M)\n$2\n---" >> "$GATE_HOME/.hades/styx.md"
            echo "📜 Seed carved into the Styx."
            ;;
        ignite)
            echo "🔥 Striking the flint..."
            python3 "$GATE_HOME/spark.py"
            ;;
        seed)
            python3 "$GATE_HOME/spark.py" seed
            ;;
        *)
            echo "Usage: hades [genesis 'idea' | ignite | seed]"
            ;;
    esac
}
```

---

### 🕹️ Commands

| Command | Action |
| :--- | :--- |
| `hades seed` | **Cultivate the Arche.** Scans your project and writes the DNA map to `arche.md`. Run after structural changes. |
| `hades genesis "Intent"` | **Carve a Seed.** Appends your intent to `styx.md`. |
| `hades ignite` | **Strike the Flint.** Sends Arche + Seeds to Gemini. Three proposals land in `prions.md`. |

---

### 🔄 The Workflow Loop

1. **Map the Universe:** `hades seed` — update the Arche after any structural changes.
2. **Speak Intent:** `hades genesis "what you want"` — log the objective.
3. **Consult the Fates:** `hades ignite` — Gemini returns three paths in `prions.md`.
4. **Materialize:** In your **active Claude session**, say *"implement Option B"* — Claude reads `prions.md` and executes with full project context.
5. **Observe:** Use the Playwright observer (`playtest.sh`) to capture real rendering data. Feed friction back into the Styx.

---

### 🛡️ Safety & Privacy
* **Ghostwire Protocol:** `.hades/` is symlinked — your seeds, API key, and generated files stay in `hades-gate`, never committed to your project.
* **Git Integrity:** `styx.md`, `arche.md`, `prions.md`, and `erebus.env` are all gitignored.
