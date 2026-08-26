from __future__ import annotations

import hashlib
import json
import re
import secrets
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping


class ConformanceError(RuntimeError):
    pass


HEX64 = re.compile(r"^[0-9a-f]{64}$")
TERMINALS = {"IDENTITY_PASS", "IDENTITY_MISMATCH", "IDENTITY_UNRESOLVED"}
ORACLE_VERSION = "MINIMUM_IDENTITY_INDEPENDENCE_ORACLE_V0.1.1"
ORACLE_BLOB = "f2f46f4ad0df0086aaa40c6f2b67755050a66ad6"
PRIMARY_FIELDS = (
    "C_view_bytes",
    "C_capture_bytes",
    "C_persist_bytes",
    "C_sha256_ops",
    "C_extract_ops",
    "C_identity_compare_ops",
)

_SCHEMA_JSON = {
    "chi_0": '{"authority":"self-report/convenience only; no H_f/H_m/H_e bytes or hashes","forbidden":["semantic_case_id","case_partition","oracle_mismatch","oracle_class","global_ordinal","oracle_aliases","previous_state","expected_terminal"],"fields_in_order":[["schema_version","const:MII_VIEW_CHI0_V0.1"],["case_handle","hex64"],["declared_object_id","enum:ALPHA|BETA"],["convenience_identity_match","bool|null"]],"schema_id":"MII_VIEW_CHI0_V0.1"}',
    "chi_1": '{"authority":"independent H_f/H_m only; H_e unavailable; H_m must not substitute for H_e","forbidden":["semantic_case_id","case_partition","oracle_mismatch","oracle_class","global_ordinal","oracle_aliases","previous_state","expected_terminal","executed_raw_bytes_utf8","custody_reported_executed_sha256"],"fields_in_order":[["schema_version","const:MII_VIEW_CHI1_V0.1"],["case_handle","hex64"],["declared_object_id","enum:ALPHA|BETA"],["convenience_identity_match","bool|null"],["frozen_bytes_utf8","string"],["frozen_sha256","hex64"],["materialized_bytes_utf8","string"],["materialized_sha256","hex64"]],"schema_id":"MII_VIEW_CHI1_V0.1"}',
    "chi_2": '{"authority":"custody_reported_executed_sha256 is H_e authority; do not recompute SHA256(executed_raw_bytes_utf8)","forbidden":["semantic_case_id","case_partition","oracle_mismatch","oracle_class","global_ordinal","oracle_aliases","previous_state","expected_terminal"],"fields_in_order":[["schema_version","const:MII_VIEW_CHI2_V0.1"],["case_handle","hex64"],["declared_object_id","enum:ALPHA|BETA"],["convenience_identity_match","bool|null"],["frozen_bytes_utf8","string"],["frozen_sha256","hex64"],["materialized_bytes_utf8","string"],["materialized_sha256","hex64"],["executed_raw_bytes_utf8","string"],["custody_reported_executed_sha256","hex64"]],"schema_id":"MII_VIEW_CHI2_V0.1"}',
    "chi_3": '{"authority":"independently recompute SHA256(executed_raw_bytes_utf8) as H_e authority; custody-reported H_e diagnostic only","forbidden":["semantic_case_id","case_partition","oracle_mismatch","oracle_class","global_ordinal","oracle_aliases","previous_state","expected_terminal"],"fields_in_order":[["schema_version","const:MII_VIEW_CHI3_V0.1"],["case_handle","hex64"],["declared_object_id","enum:ALPHA|BETA"],["convenience_identity_match","bool|null"],["frozen_bytes_utf8","string"],["frozen_sha256","hex64"],["materialized_bytes_utf8","string"],["materialized_sha256","hex64"],["executed_raw_bytes_utf8","string"],["custody_reported_executed_sha256","hex64"]],"schema_id":"MII_VIEW_CHI3_V0.1"}',
}
SCHEMAS = {k: json.loads(v) for k, v in _SCHEMA_JSON.items()}
SCHEMA_SHA = {
    "chi_0": "54214df3b4b02e8304d96a36629ac8ce6c851d61c4e5e58fcade382f28b739d3",
    "chi_1": "b873fad1d01af7c3c57d27d68cbab0df008248780fd397c5c548e2a9477c7056",
    "chi_2": "61e1de0a04040172faa914813b86f8b31f7396f11db176e82e67e145f253c7a8",
    "chi_3": "bf17650e576cbd28f7c2cbb12b039b60a2885794ae812031a929fe77a52c43b1",
}


def shared_sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def schema_sha(chi: str) -> str:
    raw = json.dumps(
        SCHEMAS[chi], sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()
    return shared_sha(raw)


def verify_schemas() -> None:
    for chi, expected in SCHEMA_SHA.items():
        if schema_sha(chi) != expected:
            raise ConformanceError(f"schema hash mismatch {chi}")


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def load_oracle(path: Path) -> dict[str, Any]:
    data = path.read_bytes()
    if git_blob_sha1(data) != ORACLE_BLOB:
        raise ConformanceError("oracle blob mismatch")
    oracle = json.loads(data.decode())
    if oracle.get("version") != ORACLE_VERSION:
        raise ConformanceError("oracle version mismatch")
    return oracle


@dataclass
class Cost:
    C_view_bytes: int | None = None
    C_capture_bytes: int = 0
    C_persist_bytes: int = 0
    C_sha256_ops: int = 0
    C_extract_ops: int = 0
    C_identity_compare_ops: int = 0
    complete: dict[str, bool] = field(
        default_factory=lambda: {
            "C_view_bytes": False,
            "C_capture_bytes": True,
            "C_persist_bytes": True,
            "C_sha256_ops": True,
            "C_extract_ops": True,
            "C_identity_compare_ops": True,
        }
    )

    # T1 -> T2 projection-side instruments only. This object is never passed to chi_i.
    def capture(self, data: bytes) -> bytes:
        self.C_capture_bytes += len(data)
        return bytes(data)

    def projection_sha(self, data: bytes) -> str:
        self.C_sha256_ops += 1
        return hashlib.sha256(data).hexdigest()

    def mark_view(self, data: bytes) -> None:
        self.C_view_bytes = len(data)
        self.complete["C_view_bytes"] = True

    def merge_architecture_delta(self, delta: "ArchitectureDelta") -> None:
        self.C_sha256_ops += delta.sha256_ops
        self.C_extract_ops += delta.extract_ops
        self.C_identity_compare_ops += delta.identity_compare_ops

    def vector(self) -> tuple[int | None, ...]:
        return tuple(getattr(self, k) for k in PRIMARY_FIELDS)

    def is_complete(self) -> bool:
        return self.C_view_bytes is not None and all(self.complete.values())


@dataclass(frozen=True)
class ArchitectureDelta:
    sha256_ops: int = 0
    extract_ops: int = 0
    identity_compare_ops: int = 0


class _ArchitectureMeter:
    """Fresh T2->T3 write-only meter state local to one architecture call.

    It is created inside the architecture function, starts at zero, receives no
    T1->T2 ledger state, and is not passed in from the harness.
    """

    __slots__ = ("_sha256_ops", "_extract_ops", "_identity_compare_ops")

    def __init__(self) -> None:
        self._sha256_ops = 0
        self._extract_ops = 0
        self._identity_compare_ops = 0

    def sha(self, data: bytes) -> str:
        self._sha256_ops += 1
        return hashlib.sha256(data).hexdigest()

    def extract(self, text: str) -> bytes:
        self._extract_ops += 1
        return text.encode()

    def compare(self, left: str, right: str) -> bool:
        self._identity_compare_ops += 1
        return left == right

    def freeze(self) -> ArchitectureDelta:
        return ArchitectureDelta(
            sha256_ops=self._sha256_ops,
            extract_ops=self._extract_ops,
            identity_compare_ops=self._identity_compare_ops,
        )


class Store:
    def __init__(self, root: Path, cost: Cost):
        self.root = root
        self.cost = cost
        root.mkdir(parents=True, exist_ok=True)
        if any(root.iterdir()):
            raise ConformanceError("custody root not empty at T1")

    def p(self, name: str) -> Path:
        path = (self.root / name).resolve()
        root = self.root.resolve()
        if root != path and root not in path.parents:
            raise ConformanceError("custody escape")
        return path

    def write(self, name: str, data: bytes) -> None:
        path = self.p(name)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("wb") as f:
            written = f.write(data)
        if written != len(data):
            self.cost.complete["C_persist_bytes"] = False
            raise ConformanceError("partial write")
        self.cost.C_persist_bytes += written

    def read(self, name: str) -> bytes:
        return self.p(name).read_bytes()

    def truncate(self, name: str, size: int) -> None:
        with self.p(name).open("r+b") as f:
            f.truncate(size)

    def delete(self, name: str) -> None:
        self.p(name).unlink()

    def retained(self) -> int:
        return sum(p.stat().st_size for p in self.root.rglob("*") if p.is_file())


@dataclass(frozen=True)
class Case:
    semantic_case_id: str
    frozen_bytes: bytes
    materialized_bytes: bytes
    executed_bytes: bytes
    declared_object_id: str
    convenience_identity_match: bool | None
    custody_override: str | None = None


def resolve_case(oracle: Mapping[str, Any], case_id: str) -> Case:
    rows = [
        row
        for section in (
            "critical_clean_controls",
            "critical_failures",
            "diagnostic_cases",
        )
        for row in oracle.get(section, [])
        if row.get("id") == case_id
    ]
    if len(rows) != 1:
        raise ConformanceError("case id must resolve once")
    row = rows[0]
    objects = oracle["objects"]

    def obj(alias: str) -> bytes:
        entry = objects[alias]
        data = entry["bytes"].encode()
        if shared_sha(data) != entry["sha256"]:
            raise ConformanceError("object hash mismatch")
        return data

    return Case(
        semantic_case_id=case_id,
        frozen_bytes=obj(row["frozen"]),
        materialized_bytes=obj(row["materialized"]),
        executed_bytes=obj(row["executed"]),
        declared_object_id=row["declared_condition"],
        convenience_identity_match=row.get("convenience_identity_match"),
        custody_override=row.get("recorder_reported_executed_sha256"),
    )


@dataclass
class Life:
    events: list[str] = field(default_factory=list)
    ORDER = (
        "T0_COMMON_ACTUAL_OBJECT_FIXED",
        "T1_ARCHITECTURE_SPECIFIC_EVIDENCE_PATH_OPEN",
        "T2_EXACT_VIEW_DISPATCHED",
        "T3_TERMINAL_ARCHITECTURE_VERDICT_FROZEN",
        "T4_REFEREE_ORACLE_JOIN",
    )

    def mark(self, event: str) -> None:
        expected = self.ORDER[len(self.events)] if len(self.events) < 5 else "NO_FURTHER_EVENT"
        if event != expected:
            raise ConformanceError(f"lifecycle got {event}, expected {expected}")
        self.events.append(event)

    def through(self, event: str) -> None:
        idx = self.ORDER.index(event)
        if tuple(self.events) != self.ORDER[: idx + 1]:
            raise ConformanceError(f"lifecycle not through {event}")


@dataclass(frozen=True)
class Prepared:
    view_bytes: bytes
    attestation: dict[str, str]
    cost: Cost
    life: Life


def _rule(name: str, rule: str, value: Any) -> None:
    if rule.startswith("const:") and value != rule.split(":", 1)[1]:
        raise ConformanceError(name)
    if rule == "hex64" and (not isinstance(value, str) or not HEX64.fullmatch(value)):
        raise ConformanceError(name)
    if rule == "enum:ALPHA|BETA" and value not in {"ALPHA", "BETA"}:
        raise ConformanceError(name)
    if rule == "bool|null" and value is not None and not isinstance(value, bool):
        raise ConformanceError(name)
    if rule == "string" and not isinstance(value, str):
        raise ConformanceError(name)


def validate(chi: str, view: Mapping[str, Any]) -> None:
    fields = SCHEMAS[chi]["fields_in_order"]
    names = [x[0] for x in fields]
    if list(view) != names:
        raise ConformanceError("view fields/order")
    for name, rule in fields:
        _rule(name, rule, view[name])
    raw = json.dumps(view, separators=(",", ":"), ensure_ascii=False).encode()
    for forbidden in (
        b"semantic_case_id",
        b"case_partition",
        b"oracle_mismatch",
        b"oracle_class",
        b"global_ordinal",
        b"expected_terminal",
        b"previous_state",
        b"ALPHA_MUT",
    ):
        if forbidden in raw:
            raise ConformanceError(f"forbidden leak {forbidden!r}")


def serialize(chi: str, view: Mapping[str, Any]) -> bytes:
    validate(chi, view)
    data = json.dumps(view, separators=(",", ":"), ensure_ascii=False).encode()
    if data.startswith(b"\xef\xbb\xbf") or data.endswith(b"\n"):
        raise ConformanceError("serialization")
    return data


def parse(chi: str, data: bytes) -> dict[str, Any]:
    if data.startswith(b"\xef\xbb\xbf") or data.endswith(b"\n"):
        raise ConformanceError("serialization")
    view = json.loads(data.decode(), object_pairs_hook=dict)
    validate(chi, view)
    if json.dumps(view, separators=(",", ":"), ensure_ascii=False).encode() != data:
        raise ConformanceError("noncanonical view")
    return view


def prepare(chi: str, case: Case, root: Path) -> Prepared:
    verify_schemas()
    life = Life()
    life.mark(Life.ORDER[0])
    handle = secrets.token_hex(32)
    if not HEX64.fullmatch(handle):
        raise ConformanceError("handle")

    life.mark(Life.ORDER[1])
    cost = Cost()
    store = Store(root, cost)
    schema_id = SCHEMAS[chi]["schema_id"]
    view: dict[str, Any] = {
        "schema_version": schema_id,
        "case_handle": handle,
        "declared_object_id": case.declared_object_id,
        "convenience_identity_match": case.convenience_identity_match,
    }
    if chi != "chi_0":
        view |= {
            "frozen_bytes_utf8": case.frozen_bytes.decode(),
            "frozen_sha256": cost.projection_sha(case.frozen_bytes),
            "materialized_bytes_utf8": case.materialized_bytes.decode(),
            "materialized_sha256": cost.projection_sha(case.materialized_bytes),
        }
    if chi in {"chi_2", "chi_3"}:
        store.write("executed.raw", cost.capture(case.executed_bytes))
        raw = store.read("executed.raw")
        view["executed_raw_bytes_utf8"] = raw.decode()
        view["custody_reported_executed_sha256"] = (
            case.custody_override or cost.projection_sha(raw)
        )

    names = [x[0] for x in SCHEMAS[chi]["fields_in_order"]]
    view = {name: view[name] for name in names}
    data = serialize(chi, view)
    cost.mark_view(data)
    attestation = {
        "case_handle": handle,
        "schema_id": schema_id,
        "schema_sha256": SCHEMA_SHA[chi],
        "dispatched_view_sha256": shared_sha(data),
        "schema_validation": "PASS",
    }
    life.mark(Life.ORDER[2])
    return Prepared(data, attestation, cost, life)


@dataclass(frozen=True)
class ArchitectureResult:
    terminal: str
    delta: ArchitectureDelta


def chi_0(view_bytes: bytes) -> ArchitectureResult:
    """Architecture boundary: exact V_0 bytes are the only case-bearing input."""
    view = parse("chi_0", view_bytes)
    meter = _ArchitectureMeter()
    value = view["convenience_identity_match"]
    terminal = (
        "IDENTITY_PASS"
        if value is True
        else "IDENTITY_MISMATCH"
        if value is False
        else "IDENTITY_UNRESOLVED"
    )
    return ArchitectureResult(terminal, meter.freeze())


def chi_1(view_bytes: bytes) -> ArchitectureResult:
    """Architecture boundary: exact V_1 bytes are the only case-bearing input."""
    view = parse("chi_1", view_bytes)
    meter = _ArchitectureMeter()
    if not meter.compare(view["frozen_sha256"], view["materialized_sha256"]):
        return ArchitectureResult("IDENTITY_MISMATCH", meter.freeze())
    return ArchitectureResult("IDENTITY_UNRESOLVED", meter.freeze())


def chi_2(view_bytes: bytes) -> ArchitectureResult:
    """Architecture boundary: exact V_2 bytes are the only case-bearing input."""
    view = parse("chi_2", view_bytes)
    meter = _ArchitectureMeter()
    if not meter.compare(view["frozen_sha256"], view["materialized_sha256"]):
        return ArchitectureResult("IDENTITY_MISMATCH", meter.freeze())
    terminal = (
        "IDENTITY_PASS"
        if meter.compare(
            view["materialized_sha256"], view["custody_reported_executed_sha256"]
        )
        else "IDENTITY_MISMATCH"
    )
    return ArchitectureResult(terminal, meter.freeze())


def chi_3(view_bytes: bytes) -> ArchitectureResult:
    """Architecture boundary: exact V_3 bytes are the only case-bearing input."""
    view = parse("chi_3", view_bytes)
    meter = _ArchitectureMeter()
    if not meter.compare(view["frozen_sha256"], view["materialized_sha256"]):
        return ArchitectureResult("IDENTITY_MISMATCH", meter.freeze())
    executed_hash = meter.sha(meter.extract(view["executed_raw_bytes_utf8"]))
    terminal = (
        "IDENTITY_PASS"
        if meter.compare(view["materialized_sha256"], executed_hash)
        else "IDENTITY_MISMATCH"
    )
    return ArchitectureResult(terminal, meter.freeze())


_ARCHITECTURES = {"chi_0": chi_0, "chi_1": chi_1, "chi_2": chi_2, "chi_3": chi_3}


def evaluate(chi: str, view_bytes: bytes) -> ArchitectureResult:
    """Dispatches to a one-argument architecture function; no ledger is passed in."""
    try:
        fn = _ARCHITECTURES[chi]
    except KeyError as exc:
        raise ConformanceError("unknown architecture") from exc
    return fn(view_bytes)


@dataclass(frozen=True)
class Frozen:
    terminal: str
    output_bytes: bytes
    output_sha256: str


def run(chi: str, prepared: Prepared) -> Frozen:
    prepared.life.through(Life.ORDER[2])
    result = evaluate(chi, prepared.view_bytes)
    output = json.dumps({"terminal": result.terminal}, separators=(",", ":")).encode()
    frozen = Frozen(result.terminal, output, shared_sha(output))
    prepared.life.mark(Life.ORDER[3])
    # Snapshot/merge architecture-local T2->T3 operation deltas only after output freeze.
    prepared.cost.merge_architecture_delta(result.delta)
    return frozen


def score(prepared: Prepared, frozen: Frozen, oracle_mismatch: bool) -> int:
    prepared.life.through(Life.ORDER[3])
    prepared.life.mark(Life.ORDER[4])
    expected = "IDENTITY_MISMATCH" if oracle_mismatch else "IDENTITY_PASS"
    return int(frozen.terminal == expected)


def aggregate(costs: list[Cost]) -> tuple[int, ...]:
    if len(costs) != 6 or not all(cost.is_complete() for cost in costs):
        raise ConformanceError("COST_COMPARISON_INCOMPLETE")
    return tuple(sum(int(cost.vector()[i]) for cost in costs) for i in range(6))


def dominates(a: tuple[int, ...], b: tuple[int, ...]) -> bool:
    if len(a) != 6 or len(b) != 6:
        raise ConformanceError("dimension")
    return all(x <= y for x, y in zip(a, b)) and any(x < y for x, y in zip(a, b))


def pareto(vectors: Mapping[str, tuple[int, ...]]) -> set[str]:
    return {
        name
        for name, vector in vectors.items()
        if not any(
            other != name and dominates(other_vector, vector)
            for other, other_vector in vectors.items()
        )
    }
