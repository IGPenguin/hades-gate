# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

**Hades Gate** is a meta-framework for turning ideas into code. It provides the **Architect** role: analyzing intent, understanding project context, and proposing six distinct implementation paths (The Hexalogy) plus a synthesis.

The primary delivery mechanism is a **Claude Code skill** (`/hades`). The legacy path uses a Python CLI + Gemini API - documented in `GEMINI.md`.

## Repo Structure

| Path | Purpose |
|------|---------|
| `claude-skill/skills/hades/SKILL.md` | The `/hades` skill definition |
| `install-skill.sh` | One-command installer for the skill |
| `.hades/papyrus.md` | Proposal template (source of truth for the repo) |
| `.hades/manifesto.md` | Coding philosophy (source of truth for the repo) |
| `hades.py` | Legacy Gemini CLI catalyst |

## History Logging

After each `/hades` run, the skill automatically saves a session record to `.hades/YYYY-MM-DD-HHMM-slug.md` in the current working directory, where `slug` is a 3-word-max summary of the intent. The file captures the user's inputs (intent, scope, constraints) and the full Hexalogy output.

The skill also ensures `.hades/` is added to `.gitignore` on first use - history files are local and should never be committed.

## The Skill

The `/hades` skill is installed to `~/.claude/plugins/cache/local/hades/1.0.0/` and reads its user-tweakable config from:
- `~/.claude/hades/papyrus.md` - proposal output structure
- `~/.claude/hades/manifesto.md` - quality standards

When modifying the skill, update `claude-skill/skills/hades/SKILL.md` in this repo. Commit and push, then re-run `install-skill.sh` to pick up changes (the installer pulls from GitHub).

## The Proposal Format (Papyrus)

Every ignition produces 6 core paths (The Hexalogy) plus one synthesis:
- **Option A - The Spark:** minimal friction, immediate result
- **Option B - The Weave:** leveraging existing infrastructure
- **Option C - The Apex:** high quality, clean architecture
- **Option D - The Echo:** proven standard patterns
- **Option E - The Rift:** experimental, outside-the-box
- **Option F - The Chimera:** flashy results, pragmatic interior
- **The Synthesis:** curated convergence of the strongest elements

The Oracle section at the end recommends which path to crystallize and why.
