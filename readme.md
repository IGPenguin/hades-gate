<p align="center">
  <img src="assets/header.svg" width="100%" alt="Hades Gate Header">
</p>

## 🔥 Materialize your ideas into reality

**Hades Gate** is a **High-Velocity Vibe-Coding** interface. The **Architect** analyzes your idea within your project context and proposes six orthogonal implementation paths, culminating in a final synthesis for the **Builder** to execute:<br>
- **Option A:** The Spark (Fastest path)
- **Option B:** The Weave (Systems integration)
- **Option C:** The Apex (High polish)
- **Option D:** The Echo (Standard patterns)
- **Option E:** The Rift (Experimental)
- **Option F:** The Chimera (Flashy hacks)
- **The Synthesis:** (Refined convergence)

---

## ⚡ Claude Code — Skill

The Architect lives natively inside Claude Code as a `/hades` skill.

No API keys, no Python CLI, no symlinks per project - install once, invoke from any session forever.

### Setup

```bash
git clone https://github.com/your-repo/hades-gate.git
cd hades-gate
./install-skill.sh
```

Restart Claude Code. That's it.

### Usage

Type `/hades` in any [Claude Code](https://claude.com/product/claude-code) session. The Architect will:
1. Read your project's `CLAUDE.md` if present (instant context, no survey needed)
2. Ask three focused questions - intent, scope, constraints
3. Generate the full Hexalogy + Synthesis inline

Pick a path, tell Claude to implement it. No separate execution step.

### Tweaking

The proposal template and thinking rules live in your home directory - changes take effect immediately.

| File | Purpose |
| :--- | :--- |
| `~/.claude/hades/papyrus.md` | Proposal template — rename options, add fields, change structure |
| `~/.claude/hades/manifesto.md` | Coding philosophy — quality standards applied to every proposal |

---

## 🧞‍♂️ Gemini CLI — Legacy

The original implementation. Setup required, but works with a free Gemini account.

**Prerequisites:** Python 3, [Gemini CLI](https://github.com/google-gemini/gemini-cli) installed, a `GEMINI_API_KEY`.

<details>
<summary><b>Setup & Installation</b></summary>

### 1. Clone & alias
```bash
git clone https://github.com/your-repo/hades-gate.git ~/Repositories/hades-gate
```
Add to your `~/.zshrc` or `~/.bashrc`:
```bash
alias hades='python3 ~/Repositories/hades-gate/hades.py'
```

### 2. Add your API key
Create `.hades/erebus.env`:
```bash
GEMINI_API_KEY=your_key_here
```

### 3. Link a project (Ghostwire Protocol)
```bash
cd ~/Repositories/your-project
hades link
hades status
```

The Ghostwire symlink bridges the Gate's shared rules into your project while keeping transient state out of your git history:

```text
       [ HADES GATE ] (The Source)
      ~/Repositories/hades-gate/
      ├── .hades/
      │   ├── manifesto.md (Central Rules)
      │   └── papyrus.md   (Proposal Template)
      └── hades.py         (The Catalyst)
             │
             │      [ GHOSTWIRE ]
             └──── (Symlink) ──────────┐
                                        ▼
                             [ YOUR PROJECT ]
                             ~/Repositories/your-project/
                             ├── .hades/ ←── (Shared State)
                             ├── TODOs.md    (Versioned Roadmap)
                             └── src/
```
</details>

### Commands

| Command | Action |
| :--- | :--- |
| `hades link` | Ghostwire symlink into the active project |
| `hades survey` | Scan project DNA into `arche.md` |
| `hades seed "idea"` | Plant intent into `styx.md` |
| `hades summon "query"` | Pull a task from `TODOs.md` as a seed |
| `hades ignite` | Generate Prions via Gemini into `prions.md` |
| `hades status` | Drift detection + seed count |

### Workflow

1. `cd` into your linked project
2. `hades survey` — capture project DNA
3. `hades seed "what you want to achieve"`
4. `hades ignite` — Gemini generates the Hexalogy into `prions.md`
5. Open a Claude session: *`read .hades/prions.md and implement The Synthesis`*

### Important files

| File | Role |
| :--- | :--- |
| `styx.md` | Active seeds — raw intent being processed |
| `arche.md` | Project DNA (survey output) |
| `prions.md` | Gemini's output — the Hexalogy + Synthesis |
| `erebus.env` | API key storage (never committed) |
