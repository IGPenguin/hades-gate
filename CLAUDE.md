# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

**Hades Gate** is a meta-framework — not a project itself, but a structured loop for turning ideas into code across any project. It separates the **Architect** role (Gemini analyzes and proposes) from the **Builder** role (Claude implements). This repo contains only the framework tooling; actual projects symlink to `.hades/` via the Ghostwire protocol.

## Commands

All interaction happens via the `hades` CLI (aliased to `hades.py`).

```bash
hades link                # Setup the Ghostwire symlink in the active project
hades status              # Check the pulse (drift detection, seed count)
hades survey              # Cultivate the Arche — scan the active project
hades seed "Intent"       # Plant a seed into .hades/styx.md
hades summon "query"      # Pull tasks from the project backlog
hades ignite              # Strike the flint — auto-surveys if drift detected
```

## Architecture

### The `.hades/` Folder

| File | Role | Git-tracked? |
|------|------|-------------|
| `manifesto.md` | Global coding standards for the Architect | Yes |
| `papyrus.md` | The 6-path proposal template | Yes |
| `styx.md` | Active seeds (raw intent) | **No** |
| `arche.md` | Project DNA (Survey output) | **No** |
| `prions.md` | 6-path proposals (Ignition output) | **No** |
| `erebus.env` | API keys (`GEMINI_API_KEY`) | **No** |

### The Ghostwire Protocol

Projects use `hades link` to automatically symlink their `.hades/` directory to this repo's source. This ensures shared rules but project-specific state.

### `hades.py` Logic

- **Smart Survey:** Uses `git diff --stat` to detect "Drift". If the project state has changed significantly since the last survey, `hades ignite` will prompt for a re-survey.
- **Argparse CLI:** Standardized command structure with built-in help.
- **JS Parsing:** Extracts skeletons (signatures) to keep context token-efficient.

### The Proposal Format (Papyrus)

Every `ignite` run produces exactly 6 paths in `prions.md`:
- **Option A — The Fast Path:** minimal friction, immediate result
- **Option B — The Interconnecting Path:** leveraging existing opportunities
- **Option C — The Dream Path:** high quality, polished, clean architecture
- **Option D — The Inspired Path:** common or proven existing solution
- **Option E — The Experimental Path:** outside-the-box or novel approach
- **Option F — The Frankenstein Path:** flashy results with a pragmatic interior

The Evaluation Matrix at the bottom recommends which to crystallize.

## Workflow

1. `cd` into the active project (the one with the `.hades` symlink)
2. `hades survey` — update the Arche with current code state
3. `hades seed "What you want to achieve"` — log intent to Styx
4. `hades summon "query"` — pull from project backlog
5. `hades ignite` — Gemini generates 6 proposals into `prions.md`
6. Review `prions.md`, pick a path, tell Claude in your **active session** to implement it
   - Claude reads `CLAUDE.md` (project rules) + `.hades/prions.md` (the chosen proposal)
   - No separate `execute` step — implementation happens in the ongoing conversation

## Adding a New Project

1. Symlink `.hades` as above
2. Add to the project's `CLAUDE.md`:
   ```markdown
   ## Hades Gate Integration
   - Before starting any task, check `.hades/prions.md` for the latest proposals.
   ```
3. Run `hades survey` from the project root to populate `arche.md`
