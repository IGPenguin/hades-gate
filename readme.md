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
    # 1. Define the Master Path to your framework
    local GATE_HOME="/Users/username/.../hades-gate"

    case "$1" in
        genesis)
            # This now always hits the same styx.md regardless of where you are
            echo -e "\n## Seed $(date +%Y-%m-%d_%H:%M)\n$2\n---" >> "$GATE_HOME/.hades/styx.md"
            echo "📜 Seed carved into the Styx."
            ;;
        ignite)
            echo "🔥 Striking the flint..."
            # Now we actually call spark.py and let IT handle the Gemini CLI call
            python3 "$GATE_HOME/spark.py"
            ;;
        *)
            echo "Usage: hades [genesis 'text' | ignite]"
            ;;
    esac
}

```
