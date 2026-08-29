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
base_rule_mem = MANIFEST["base_source_rule_memory"]
compiled_mem = MANIFEST["compiled_group_memory"]
mem_budget = MANIFEST["memory_budget"]
prod_budget = MANIFEST["productive_budget"]
lambdas = MANIFEST["lambda_values"]
corr_budget = MANIFEST["correction_budget"]
base_rules = [g % 2 for g in range(N)]

def compile_group(rule):
    return [(i % 2) ^ rule for i in range(L)]

s0 = {"rules": {f"G{g}": base_rules[g] for g in range(N)}, "compiled": {}}

def mem(st, regime, lam=None):
    total = 0
    for g in range(N):
        k = f"G{g}"
        hr, hc = k in st["rules"], k in st["compiled"]
        if hc:
            total += compiled_mem
            if hr:
                assert regime == "C"
                total += lam
        elif hr:
            total += base_rule_mem
        else:
            raise AssertionError
    return total

def qcost(st, g):
    return 1 if f"G{g}" in st["compiled"] else 3

def V(st):
    avg = sum(weights[g] * qcost(st, g) for g in range(N)) / sum(weights)
    return math.floor(prod_budget / avg)

def accumulate_P():
    st = json.loads(json.dumps(s0))
    for g in range(N):
        k = f"G{g}"
        if mem(st, "P") - base_rule_mem + compiled_mem <= mem_budget:
            rule = st["rules"].pop(k)
            st["compiled"][k] = compile_group(rule)
    return st

def accumulate_C(lam):
    st = json.loads(json.dumps(s0))
    for g in range(N):
        k = f"G{g}"
        if mem(st, "C", lam) - base_rule_mem + compiled_mem + lam <= mem_budget:
            st["compiled"][k] = compile_group(st["rules"][k])
    return st

states = {"P": accumulate_P()}
for lam in lambdas:
    states[f"C_lambda_{lam}"] = accumulate_C(lam)

truths = {}
for gstar in range(N):
    rules = base_rules[:]
    rules[gstar] ^= 1
    truths[gstar] = {
        "n_groups": N,
        "leaves_per_group": L,
        "rules": rules,
        "surprise_group": gstar,
        "operation": "flip_rule",
    }

def predict(st, g, i):
    k = f"G{g}"
    if k in st["compiled"]:
        return st["compiled"][k][i]
    return (i % 2) ^ st["rules"][k]

def nerr(st, gstar):
    rules = truths[gstar]["rules"]
    return sum(
        predict(st, g, i) != ((i % 2) ^ rules[g])
        for g in range(N) for i in range(L)
    )

def acts(st, gstar):
    k = f"G{gstar}"
    target = truths[gstar]["rules"][gstar]
    out = []
    if k in st["rules"]:
        out += [("SET_RULE", gstar, target), ("COMPILE_GROUP", gstar)]
    if k in st["compiled"]:
        for i in range(L):
            out.append(("PATCH_LEAF", gstar, i, (i % 2) ^ target))
    return out

def apply(st, action):
    ns = json.loads(json.dumps(st))
    kind, g = action[0], action[1]
    k = f"G{g}"
    if kind == "SET_RULE":
        if k not in ns["rules"]:
            return None
        ns["rules"][k] = action[2]
    elif kind == "COMPILE_GROUP":
        if k not in ns["rules"]:
            return None
        ns["compiled"][k] = compile_group(ns["rules"][k])
    elif kind == "PATCH_LEAF":
        if k not in ns["compiled"]:
            return None
        ns["compiled"][k][action[2]] = action[3]
    return ns

def key(st):
    return json.dumps(st, sort_keys=True, separators=(",", ":"))

def bfs(start, gstar):
    q = deque([(start, [])])
    seen = {key(start)}
    explored = 0
    while q:
        st, path = q.popleft()
        explored += 1
        if nerr(st, gstar) == 0:
            return st, path, explored
        if len(path) >= corr_budget:
            continue
        for a in acts(st, gstar):
            ns = apply(st, a)
            if ns is None:
                continue
            k = key(ns)
            if k not in seen:
                seen.add(k)
                q.append((ns, path + [a]))
    return None, None, explored

items = []
raw = []
for state_name, st in states.items():
    regime = "P" if state_name == "P" else "C"
    lam = None if regime == "P" else int(state_name.rsplit("_", 1)[1])
    for gstar in range(N):
        ep, path, explored = bfs(st, gstar)
        eid = f"{state_name}__G{gstar}"
        items.append({"id": eid, "state": ep, "truth": truths[gstar]})
        raw.append({
            "id": eid, "state": state_name, "lambda": lam,
            "V_present": V(st), "memory_used": mem(st, regime, lam),
            "surprise": f"G{gstar}", "path": path,
            "Cstar_candidate": len(path) if path is not None else None,
            "states_explored": explored,
        })

batch_path = ROOT / "REPRODUCTION_VALIDATION_INPUT.json"
batch_path.write_text(json.dumps({"items": items}, sort_keys=True) + "\n", encoding="utf-8")
cp = subprocess.run(
    [sys.executable, str(ROOT / "validate_batch.py"), str(batch_path)],
    capture_output=True, text=True, timeout=20
)
validation = json.loads(cp.stdout)
vmap = {x["id"]: x for x in validation["results"]}

rows = []
for r in raw:
    vr = vmap[r["id"]]
    rows.append({**r, "Cstar": r["Cstar_candidate"] if vr["pass"] else None, "validation": vr})

summary = []
for state_name, st in states.items():
    rr = [r for r in rows if r["state"] == state_name]
    costs = [r["Cstar"] for r in rr]
    regime = "P" if state_name == "P" else "C"
    lam = None if regime == "P" else int(state_name.rsplit("_", 1)[1])
    summary.append({
        "state": state_name,
        "lambda": lam,
        "V_present": V(st),
        "memory_used": mem(st, regime, lam),
        "n_compiled": len(st["compiled"]),
        "mean_Cstar": sum(costs) / N,
        "max_Cstar": max(costs),
        "min_Cstar": min(costs),
        "n_surprises_Cstar_gt_1": sum(c > 1 for c in costs),
        "all_validated": all(r["validation"]["pass"] for r in rr),
    })

out = {
    "contract_sha256": MANIFEST["contract_sha256"],
    "summary": summary,
    "n_evaluations": len(rows),
    "all_validations_pass": all(r["validation"]["pass"] for r in rows),
}
(ROOT / "REPRODUCTION.json").write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(out, indent=2, sort_keys=True))
