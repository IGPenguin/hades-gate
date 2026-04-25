<p align="center">
  <img src="assets/header.svg" width="100%" alt="Hades Gate Header">
</p>

## 🔥 Materialize your ideas into reality

**Hades Gate** is a **High-Velocity Vibe-Coding** interface that analyzes your idea within your project context and proposes three distinct implementation paths:<br>
- **Option A:** The Fast Path (Minimum Viable Result)
- **Option B:** The Dream Path (High Quality/Polished)
- **Option C:** The Experimental Path (Outside the Box)

The **Architect** (Gemini) analyzes your project, the **Builder** (Claude) executes the chosen plan in an active session — where full context already lives.

| Command | Action |
| :--- | :--- |
| `hades survey` | Scans your project (including `TODOs.md`) and writes the DNA map to `arche.md`. |
| `hades seed "idea"` | Plants your idea into `styx.md`. |
| `hades summon "query"` | Searches your `TODOs.md` for a task and "summons" it as a seed in `styx.md`. |
| `hades ignite` | Sends `arche.md` (context) + `styx.md` (seed) to Gemini. Proposals land in `prions.md`. |
|**Claude session:** *"implement option B"*|Claude reads `prions.md` with full context and executes the plan.|
|**(or) Terminal:** `hades execute B`|Bridges the selected `prions.md` plan execution to a clean Claude CLI session directly.|

### 🔱 Project pillars
*   **Zero Pollution:** By using Ghostwire Protocol, your main repository remains "Pure", the transient proposals stay in the `hades-gate` directory, never polluting your project's git history.
*   **Peripheral Vision:** By reading your versioned `TODOs.md`, the AI plans Path B (The Dream Path) with awareness of your future goals, ensuring immediate fixes don't block long-term vision.
*   **Context Isolation:** The AI sees an optimized "Snapshot" of your project, preventing it from getting lost in the noise of your entire `.git` history or binary assets.
*   **The Global Brain:** Improvements to your `manifesto.md` (coding standards) or `papyrus.md` (proposal structure) in the `hades-gate` repo immediately benefit all linked projects.

### 🔗 Project linking

**Ghostwire Protocol** (a symlink) bridges the **Hades Gate** framework to your project, this keeps the "Brain" and "Rules" centralized while the local project "State" is ignored by git.

```text
       [ HADES GATE ] (The Source)
      ~/Repositories/hades-gate/
      ├── .hades/
      │   ├── manifesto.md (Central Rules)
      │   └── papyrus.md   (Proposal Template)
      └── hades.py         (The Catalyst)
             │
             │      [ GHOSTWIRE ]
             └──── (Symlink link) ────┐
                                      ▼
                           [ YOUR PROJECT ] (The Target)
                           ~/Repositories/your-project/
                           ├── .hades/ <─── (Shared State)
                           ├── TODOs.md    (Versioned Roadmap)
                           └── src/        (Your Codebase)
```

### 🧬 Important files
*   **The Backlog (`TODOs.md`):** Your versioned, human-curated roadmap. Lives in your project root.
*   **The Styx (`styx.md`):** The "Active Ritual" — transient seeds currently being processed.
*   **The Arche (`arche.md`):** Project DNA (CLAUDE.md + File Tree + Backlog + API Surface). Built by `hades survey`.
*   **The Prions (`prions.md`):** Gemini's output — three infectious paths ready to mutate your codebase.
*   **The Spark (`hades.py`):** The catalyst logic that bridges the gate and manages the ritual.

---

## ⚙️ Setup & Installation

<details>
<summary><b>Click to expand the installation steps...</b></summary>

### 1. Clone & Install
```bash
git clone https://github.com/your-repo/hades-gate.git ~/Repositories/hades-gate
cd ~/Repositories/hades-gate
./install.sh
```
Follow the prompts to set up your `GEMINI_API_KEY`.

### 2. Shell Function
Add the following function to your `~/.zshrc` or `~/.bashrc`. It wraps the `hades` script and adds the optional `execute` command:
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

### 3. The Ghostwire (Symlink)
Link your project into the Gate so it shares the `.hades/` state:
```bash
cd ~/Repositories/your-project
ln -s ~/Repositories/hades-gate/.hades .hades
```
</details>
