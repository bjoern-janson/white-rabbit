import json, sys
from pathlib import Path

batch = json.loads(Path(sys.argv[1]).read_text())
out = []
for item in batch["items"]:
    state = item["state"]
    truth = item["truth"]
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
    out.append({"id": item["id"], "pass": not errors, "n_errors": len(errors), "errors": errors})
print(json.dumps({"results": out}, sort_keys=True))
raise SystemExit(0 if all(x["pass"] for x in out) else 1)
