import json, sys
from pathlib import Path
state = json.loads(Path(sys.argv[1]).read_text())
truth = json.loads(Path(sys.argv[2]).read_text())
errors = []
for g in range(truth["n_groups"]):
    key = f"G{g}"
    for i in range(truth["leaves_per_group"]):
        if key in state["compiled"]:
            got = state["compiled"][key][i]
        elif key in state["rules"]:
            got = (i % 2) ^ state["rules"][key]
        else:
            got = None
        want = (i % 2) ^ truth["rules"][g]
        if got != want:
            errors.append([g, i, got, want])
print(json.dumps({"pass": not errors, "n_errors": len(errors), "errors": errors}, sort_keys=True))
raise SystemExit(0 if not errors else 1)
