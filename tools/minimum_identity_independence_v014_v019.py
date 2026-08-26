from __future__ import annotations

import secrets
from pathlib import Path

from tools.minimum_identity_independence_v014_v018 import *  # re-export frozen parent surfaces
import tools.minimum_identity_independence_v014_v018 as _capture

# Gate-5-only successor. Constitution, oracle, schemas, architecture authority,
# runtime sandbox, lifecycle, SHA/extract/compare/capture completed-work
# semantics, scoring, cost dimensions, missingness rules, and Pareto rules
# remain unchanged. The sole repair is cumulative persistence write accounting.


def _persistence_write_once(path: Path, data: bytes, mode: str) -> int:
    """Perform one architecture-evidence byte write and return its known count.

    If the underlying operation raises before returning a byte count, the
    transferred amount is treated as unknown by the instrumented caller.
    """
    with path.open(mode) as stream:
        return stream.write(data)


class Store(_capture.Store):
    """Successor custody store with cumulative, fail-closed write accounting."""

    def __init__(self, root: Path, cost: Cost):
        super().__init__(root, cost)
        # Once any architecture-attributable persistence write becomes partial
        # or unknowable, later successful writes may not restore completeness.
        self._persistence_measurement_valid = True

    def _write_mode(self, name: str, data: bytes, mode: str) -> None:
        path = self.p(name)
        path.parent.mkdir(parents=True, exist_ok=True)

        # A required persistence operation is pending until its authoritative
        # returned write count is known. Unknown transfer amount must fail closed.
        self.cost.complete["C_persist_bytes"] = False
        try:
            written = _persistence_write_once(path, data, mode)
        except Exception:
            self._persistence_measurement_valid = False
            self.cost.complete["C_persist_bytes"] = False
            raise

        if (
            not isinstance(written, int)
            or isinstance(written, bool)
            or written < 0
            or written > len(data)
        ):
            self._persistence_measurement_valid = False
            self.cost.complete["C_persist_bytes"] = False
            raise ConformanceError("invalid persistence write count")

        # Preserve every positively known byte that actually completed writing,
        # even when the intended write was short and the dimension is incomplete.
        self.cost.C_persist_bytes += written

        if written != len(data):
            self._persistence_measurement_valid = False
            self.cost.complete["C_persist_bytes"] = False
            raise ConformanceError("partial write")

        if self._persistence_measurement_valid:
            self.cost.complete["C_persist_bytes"] = True

    def write(self, name: str, data: bytes) -> None:
        """Create/overwrite evidence; every actual returned byte counts."""
        self._write_mode(name, data, "wb")

    def append(self, name: str, data: bytes) -> None:
        """Append evidence through the same authoritative cumulative primitive."""
        self._write_mode(name, data, "ab")


def prepare(chi: str, case: Case, root: Path) -> Prepared:
    """Construct exact V_i using the repaired cumulative persistence store only."""
    verify_schemas()
    life = Life()
    life.mark(Life.ORDER[0])
    handle = secrets.token_hex(32)
    if not HEX64.fullmatch(handle):
        raise ConformanceError("handle")

    life.mark(Life.ORDER[1])
    cost = Cost()

    # Capture and persistence are constituted complete-zero for chi_0/chi_1,
    # which require neither executed-byte custody capture nor persistence.
    # For chi_2/chi_3 both measurements are pending until the required work
    # completes through their authoritative primitives.
    if chi in {"chi_2", "chi_3"}:
        cost.complete["C_capture_bytes"] = False
        cost.complete["C_persist_bytes"] = False
    else:
        cost.complete["C_capture_bytes"] = True
        cost.complete["C_persist_bytes"] = True

    store = Store(root, cost)
    schema_id = SCHEMAS[chi]["schema_id"]
    view: dict[str, object] = {
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
        captured = cost.capture(case.executed_bytes)
        store.write("executed.raw", captured)
        raw = store.read("executed.raw")
        view["executed_raw_bytes_utf8"] = raw.decode()
        view["custody_reported_executed_sha256"] = (
            case.custody_override or cost.projection_sha(raw)
        )

    names = [field[0] for field in SCHEMAS[chi]["fields_in_order"]]
    ordered = {name: view[name] for name in names}
    data = serialize(chi, ordered)
    cost.mark_view(data)
    attestation = {
        "case_handle": handle,
        "schema_id": schema_id,
        "schema_sha256": SCHEMA_SHA[chi],
        "dispatched_view_sha256": shared_sha(data),
        "schema_validation": "PASS",
    }

    # Preserve the reviewed fail-closed total operation semantics.
    _capture._sha._complete._set_operation_measurement_complete(cost, False)
    return Prepared(data, attestation, cost, life)


def run(chi: str, prepared: Prepared) -> Frozen:
    return _capture.run(chi, prepared)


def evaluate(chi: str, view_bytes: bytes):
    return _capture.evaluate(chi, view_bytes)


def capability_probe(action: str, payload: dict[str, str]) -> str:
    return _capture.capability_probe(action, payload)
