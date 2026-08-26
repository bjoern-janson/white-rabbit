from __future__ import annotations

import hashlib
import secrets
from pathlib import Path

from tools.minimum_identity_independence_v014_v016 import *  # re-export frozen parent surfaces
import tools.minimum_identity_independence_v014_v016 as _complete

# Gate-5-only successor. Constitution, oracle, schemas, architecture authority,
# runtime sandbox, lifecycle, child completed-operation events, scoring, cost
# dimensions, missingness rules, and Pareto rules remain unchanged.
# The sole repair is projection-side SHA completion accounting during T1->T2.


def _projection_sha256_digest(data: bytes) -> str:
    """Uninstrumented digest body used only by the instrumented projection wrapper."""
    return hashlib.sha256(data).hexdigest()


class Cost(_complete.Cost):
    """Successor cost ledger with completed-work projection SHA accounting."""

    def projection_sha(self, data: bytes) -> str:
        # The total SHA dimension is not complete until the T2->T3 operation
        # stream has also been acquired/decoded. A projection-side failure must
        # therefore remain incomplete and must never create a false +1.
        self.complete["C_sha256_ops"] = False
        result = _projection_sha256_digest(data)
        self.C_sha256_ops += 1
        return result


def prepare(chi: str, case: Case, root: Path) -> Prepared:
    """Construct the exact frozen V_i using the repaired projection SHA wrapper.

    This is semantically the reviewed v0.1.4/v0.1.6 preparation path, with only
    the Cost implementation changed. Lifecycle authority still ends at T1;
    T2 remains bound to the actual successful sandbox dispatch.
    """
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
        store.write("executed.raw", cost.capture(case.executed_bytes))
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

    # Preserve v0.1.6 fail-closed total-operation semantics: the projection-side
    # counts above are accrued, but the mandatory total operation dimensions
    # remain incomplete until the architecture event stream is validated.
    _complete._set_operation_measurement_complete(cost, False)
    return Prepared(data, attestation, cost, life)


def run(chi: str, prepared: Prepared) -> Frozen:
    """Inherit the reviewed lifecycle and fail-closed operation-stream merge."""
    return _complete.run(chi, prepared)


def evaluate(chi: str, view_bytes: bytes):
    return _complete._ops.evaluate(chi, view_bytes)


def capability_probe(action: str, payload: dict[str, str]) -> str:
    return _complete._ops.capability_probe(action, payload)
