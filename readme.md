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
        execute)
            # Usage: hades execute B
            if [ -z "$2" ]; then
                echo "❌ Please specify Path A, B, or C."
            else
                echo "🛠️ Summoning Claude to implement Path $2..."
                # This launches the Claude CLI with the specific instruction
                claude "Analyze .hades/prions.md and implement the full logic for Option $2. Follow all rules in .hades/manifesto.md."
            fi
            ;;
	seed)
            echo "🌱 Cultivating the Arche..."
            local GATE_HOME="$HOME/Repositories/hades-gate"
            {
                echo "# THE ARCHE: PROJECT DNA"
                tree -I 'node_modules|.git|playtests' --dirsfirst
                echo -e "\n## Core Logic Headers"
                for f in index.html main.js logging.js logic.js state.js; do
                    if [ -f "$f" ]; then
                        echo "### $f"
                        echo '```javascript'
                        head -n 80 "$f"
                        echo -e '```\n'
                    fi
                done
            } > "$GATE_HOME/.hades/arche.md"
            echo "✨ Arche inscribed at $GATE_HOME/.hades/arche.md"
            ;;
        *)
            echo "Usage: hades [genesis 'idea' | ignite | execute A/B/C]"
            ;;
    esac
}
```
