from pathlib import Path
from collections import deque
import json, hashlib, math, subprocess, sys

ROOT = Path(__file__).resolve().parent
CONTRACT = (ROOT / "CONTRACT.txt").read_text(encoding="utf-8")
MANIFEST = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))

assert hashlib.sha256(CONTRACT.encode()).hexdigest() == MANIFEST["contract_sha256"]

N = MANIFEST["n_groups"]
L = MANIFEST["leaves_per_group"]
weights = MANIFEST["workload_weights"]
base_rules = [g % 2 for g in range(N)]

def compile_group(rule):
    return [(i % 2) ^ rule for i in range(L)]

s0 = {"rules": {f"G{g}": base_rules[g] for g in range(N)}, "compiled": {}}

def memory_used(state):
    return 2 * len(state["rules"]) + 8 * len(state["compiled"])

def query_cost(state, g):
    key = f"G{g}"
    if key in state["compiled"]:
        return 1
    if key in state["rules"]:
        return 3
    return math.inf

def productive_value(state):
    avg = sum(weights[g] * query_cost(state, g) for g in range(N)) / sum(weights)
    return math.floor(MANIFEST["productive_budget"] / avg)

def accumulate(preserve):
    st = json.loads(json.dumps(s0))
    for g in sorted(range(N), key=lambda x: (-weights[x], x)):
        key = f"G{g}"
        if preserve:
            if memory_used(st) + 8 <= MANIFEST["memory_budget"]:
                st["compiled"][key] = compile_group(st["rules"][key])
        else:
            if memory_used(st) + 6 <= MANIFEST["memory_budget"]:
                rule = st["rules"].pop(key)
                st["compiled"][key] = compile_group(rule)
    return st

# Accumulation occurs before selected surprise is materialized.
sP = accumulate(False)
sC = accumulate(True)

gstar = int(MANIFEST["contract_sha256"], 16) % N
post_rules = base_rules[:]
post_rules[gstar] ^= 1

def predicts(st, g, i):
    key = f"G{g}"
    if key in st["compiled"]:
        return st["compiled"][key][i]
    if key in st["rules"]:
        return (i % 2) ^ st["rules"][key]
    return None

def validation_errors(st):
    return sum(
        predicts(st, g, i) != ((i % 2) ^ post_rules[g])
        for g in range(N) for i in range(L)
    )

def actions(st):
    key = f"G{gstar}"
    out = []
    if key in st["rules"]:
        out.append(("SET_RULE", gstar, post_rules[gstar]))
        out.append(("COMPILE_GROUP", gstar))
    if key in st["compiled"]:
        for i in range(L):
            out.append(("PATCH_LEAF", gstar, i, (i % 2) ^ post_rules[gstar]))
    return out

def apply(st, action):
    ns = json.loads(json.dumps(st))
    kind, g = action[0], action[1]
    key = f"G{g}"
    if kind == "SET_RULE":
        if key not in ns["rules"]:
            return None
        ns["rules"][key] = action[2]
    elif kind == "COMPILE_GROUP":
        if key not in ns["rules"]:
            return None
        ns["compiled"][key] = compile_group(ns["rules"][key])
    elif kind == "PATCH_LEAF":
        if key not in ns["compiled"]:
            return None
        ns["compiled"][key][action[2]] = action[3]
    return ns

def key(st):
    return json.dumps(st, sort_keys=True, separators=(",", ":"))

def bfs(start):
    q = deque([(start, [])])
    seen = {key(start)}
    explored = 0
    while q:
        st, path = q.popleft()
        explored += 1
        if validation_errors(st) == 0:
            return st, path, explored
        if len(path) >= MANIFEST["correction_budget"]:
            continue
        for action in actions(st):
            ns = apply(st, action)
            if ns is None:
                continue
            k = key(ns)
            if k not in seen:
                seen.add(k)
                q.append((ns, path + [action]))
    return None, None, explored

endP, pathP, exploredP = bfs(sP)
endC, pathC, exploredC = bfs(sC)

def external_validate(st, name):
    p = ROOT / f"reproduction-{name}.json"
    p.write_text(json.dumps(st, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    cp = subprocess.run(
        [sys.executable, str(ROOT / "validate.py"), str(p), str(ROOT / "hidden_truth.json")],
        capture_output=True, text=True, timeout=10
    )
    detail = json.loads(cp.stdout)
    return cp.returncode == 0 and detail["pass"], detail

okP, valP = external_validate(endP, "P")
okC, valC = external_validate(endC, "C")

out = {
    "contract_sha256": MANIFEST["contract_sha256"],
    "surprise_group": f"G{gstar}",
    "V_s0": productive_value(s0),
    "V_sP": productive_value(sP),
    "V_sC": productive_value(sC),
    "Cstar_P": len(pathP) if okP else None,
    "Cstar_C": len(pathC) if okC else None,
    "delta": (len(pathP) - len(pathC)) if okP and okC else None,
    "path_P": pathP,
    "path_C": pathC,
    "explored_P": exploredP,
    "explored_C": exploredC,
    "validation_P": valP,
    "validation_C": valC,
}
(ROOT / "REPRODUCTION.json").write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(out, indent=2, sort_keys=True))
