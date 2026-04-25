# Hades Gate

Status: Initialized

Objective: Materialize the Void (Intent) into Reality (Code).

Strategy:
- The Brain: You provide the "Seed" (the task).
- The Kitchen: Gemini proposes three ways to solve it based on your code history.
- The Muscle: Claude Code executes the chosen path.
- The Pulse: We use a "Safe Browser" (Firefox/Playwright) to see results in real-time, feeding that "feeling" back into the next loop.

Terminal alias:
```
hades() {
    case "$1" in
        genesis)
            # Usage: hades genesis "My new idea"
            echo -e "\n## Seed $(date +%Y-%m-%d_%H:%M)\n$2\n---" >> .hades/styx.md
            echo "📜 Seed carved into the Styx."
            ;;
        ignite)
            # Usage: hades ignite
            echo "🔥 Igniting the Spark..."
            # Adjust 'gemini' to your specific CLI command if different
            gemini --system "$(cat .hades/manifesto.md)" \
            "Read .hades/styx.md and .hades/papyrus.md. Analyze the project. Write 3 Prions to .hades/prions.md."
            echo "🦠 Prions have materialized in .hades/prions.md"
            ;;
        *)
            echo "Usage: hades [genesis 'text' | ignite]"
            ;;
    esac
}
```
