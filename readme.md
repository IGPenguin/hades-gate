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

#### 2. Shell Alias
Add the following to your `~/.zshrc` or `~/.bashrc`:
```bash
alias hades='~/Repositories/hades-gate/hades'
```

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
   - **Option A (Live):** In your active Claude session, say *"implement Option B"*.
   - **Option B (CLI):** If you have the optional `execute` alias, run `hades execute B`.

---

### 🛡️ Safety & Privacy
* **Ghostwire Protocol:** `.hades/` is symlinked — your seeds, API key, and generated files stay in `hades-gate`, never committed to your project.
* **Git Integrity:** `styx.md`, `arche.md`, `prions.md`, and `erebus.env` are all gitignored.
