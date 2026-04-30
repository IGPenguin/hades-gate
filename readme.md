<p align="center">
  <img src="assets/header.svg" width="100%" alt="Hades Gate Header">
</p>

## 🔥 Materialize your ideas into reality

**Hades Gate** is a **High-Velocity Vibe-Coding** interface. Once initialized, the **Architect** (Gemini) analyzes your idea within your project context and proposes six distinct implementation paths for the **Builder** (Claude) to execute cleanly, in combination or with extra refining:<br>
- **Option A:** The Fast Path (Minimum Viable Result)
- **Option B:** The Interconnecting Path (Existing Opportunities)
- **Option C:** The Dream Path (High Quality/Polished)
- **Option D:** The Inspired Path (Common Solution)
- **Option E:** The Experimental Path (Outside the Box)
- **Option F:** The Frankenstein Path (Flashy Outside/Pragmatic Inside)

### 🔪 Execution
**Claude session:** *`read .hades/prions.md to implement combination of options A and E + feature X from option B`*<br>
- Implement the selected proposal, or a combination of multiple options, or simply cherry-pick features as you like.<br>
- <i>**Pro-tip:** Ask Claude to fill any blind spots it discovers when planning the excution by asking you questions.</i><br>

### 📌 Commands
| Command | Action |
| :--- | :--- |
| `hades status` | Checks the pulse of the Gate (drift detection, seed count). |
| `hades link` | Automatically symlinks your project into the Gate (Ghostwire Protocol). |
| `hades survey` | Scans your project and writes the DNA map to `arche.md`. |
| `hades seed "idea"` | Plants your idea into `styx.md`. |
| `hades summon "query"` | Searches your `TODOs.md` for a task and "summons" it as a seed. |
| `hades ignite` | The ritual: Auto-surveys (if drifted) + generates Prions into `prions.md`. |

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
*   **The Prions (`prions.md`):** Gemini's output — six infectious paths ready to mutate your codebase.
*   **The Spark (`hades.py`):** The catalyst logic that bridges the gate and manages the ritual.

## ⚙️ Setup & Installation

<details>
<summary><b>Click to expand the installation steps...</b></summary>

### 1. Clone & Install
```bash
git clone https://github.com/your-repo/hades-gate.git ~/Repositories/hades-gate
cd ~/Repositories/hades-gate
./install.sh
```

### 2. Global Alias
Add this to your `~/.zshrc` or `~/.bashrc`:
```bash
alias hades='python3 ~/Repositories/hades-gate/hades.py'
```

### 3. The Ghostwire Ritual
Link any project into the Gate to start the cycle:
```bash
cd ~/Repositories/your-project
hades link
hades status
```
</details>
