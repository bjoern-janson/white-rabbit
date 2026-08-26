from __future__ import annotations

import json
import select
import subprocess
import tempfile
from pathlib import Path
from typing import BinaryIO

from tools.minimum_identity_independence_v014_v019 import *  # re-export frozen parent surfaces
import tools.minimum_identity_independence_v014_v019 as _persist

# Gate-5-only successor. Constitution, oracle, schemas, architecture authority,
# runtime sandbox, lifecycle meanings, SHA/extract/compare/capture/persistence
# semantics, scoring, cost dimensions, missingness rules, and Pareto rules remain
# unchanged. The sole repair is exact-view dispatch-byte accounting.

# Latest reviewed child-operation implementation and lifecycle sandbox lineage.
_complete = _persist._capture._sha._complete
_ops = _complete._ops
_life = _ops._life


class Cost(_persist.Cost):
    """Successor ledger whose view-byte authority exists only at dispatch."""

    def mark_view(self, data: bytes) -> None:
        """Historical prepare-time completion path is forbidden in this successor."""
        raise ConformanceError(
            "C_view_bytes authority belongs only to actual exact-view dispatch"
        )

    def _view_pending(self) -> None:
        self.C_view_bytes = None
        self.complete["C_view_bytes"] = False

    def _view_known_partial(self, total: int) -> None:
        if total < 0:
            raise ConformanceError("negative view transfer count")
        self.C_view_bytes = total
        self.complete["C_view_bytes"] = False

    def _view_unknown(self) -> None:
        self.C_view_bytes = None
        self.complete["C_view_bytes"] = False

    def _view_complete_after_t2(self, total: int, life: Life) -> None:
        # Enforce the causal authority direction mechanically:
        # complete C_view_bytes => T2 already exists.
        life.through(Life.ORDER[2])
        self.C_view_bytes = total
        self.complete["C_view_bytes"] = True


def prepare(chi: str, case: Case, root: Path) -> Prepared:
    """Construct and freeze exact V_i while leaving view-byte cost pending."""
    verify_schemas()
    life = Life()
    life.mark(Life.ORDER[0])
    handle = __import__("secrets").token_hex(32)
    if not HEX64.fullmatch(handle):
        raise ConformanceError("handle")

    life.mark(Life.ORDER[1])
    cost = Cost()
    cost._view_pending()

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

    # No prepare-time C_view_bytes value or completion authority is granted.
    # The common attestation hash remains shared scaffolding, as constituted.
    attestation = {
        "case_handle": handle,
        "schema_id": schema_id,
        "schema_sha256": SCHEMA_SHA[chi],
        "dispatched_view_sha256": shared_sha(data),
        "schema_validation": "PASS",
    }

    # Preserve reviewed fail-closed total operation semantics.
    _persist._capture._sha._complete._set_operation_measurement_complete(cost, False)
    return Prepared(data, attestation, cost, life)


def _write_exact_view_account_and_mark_t2(
    stream: BinaryIO,
    view_bytes: bytes,
    cost: Cost,
    life: Life,
) -> None:
    """Transfer exact V_i, account only known transferred bytes, then earn T2."""
    life.through(Life.ORDER[1])
    if not view_bytes:
        raise ConformanceError("empty view dispatch")

    cost._view_pending()
    total = 0
    payload = memoryview(view_bytes)

    try:
        while total < len(payload):
            written = stream.write(payload[total:])
            if (
                not isinstance(written, int)
                or isinstance(written, bool)
                or written < 0
                or written > len(payload) - total
            ):
                # The transfer measurement itself is unusable; do not invent a
                # byte count for the current write attempt.
                cost._view_unknown()
                raise ConformanceError("invalid view dispatch write count")
            if written == 0:
                # Zero is a known result. Preserve any previously transferred
                # prefix, but do not promote it to an exact-view dispatch.
                cost._view_known_partial(total)
                raise ConformanceError("view dispatch incomplete")

            total += written
            cost._view_known_partial(total)

        # Production stdin is opened unbuffered below, so successful returned
        # write counts are the authoritative transfer counts. Flush/close must
        # still succeed before full exact dispatch earns T2.
        stream.flush()
        stream.close()
    except ConformanceError:
        raise
    except (BrokenPipeError, OSError, ValueError) as exc:
        # The current failed operation has no authoritative returned transfer
        # count. Do not invent a full count or zero.
        cost._view_unknown()
        raise ConformanceError("view dispatch failed with unknown byte count") from exc

    if total != len(view_bytes):
        cost._view_known_partial(total)
        raise ConformanceError("view dispatch byte-count mismatch")

    # Lifecycle authority is earned at the exact same causal boundary as the
    # completed view transfer. Completion is granted only after T2 exists.
    life.mark(Life.ORDER[2])
    cost._view_complete_after_t2(total, life)


def _spawn(
    source: str,
    input_bytes: bytes,
    cost: Cost | None = None,
    life: Life | None = None,
) -> tuple[bytes, bytes]:
    """Retain the reviewed sandbox; bind production view accounting to stdin."""
    with tempfile.TemporaryDirectory(prefix="mii-sandbox-") as td:
        proc = subprocess.Popen(
            _life._base._launcher() + [source],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=td,
            env={},
            close_fds=True,
            # Make returned stdin.write counts the transfer primitive rather
            # than merely buffered bytes prepared in the parent process.
            bufsize=0,
        )
        try:
            ready, _, _ = select.select([proc.stderr], [], [], 5)
            if not ready:
                proc.kill()
                proc.wait(timeout=2)
                raise ConformanceError("sandbox readiness timeout")
            line = proc.stderr.readline()
            if line != _life._base.SANDBOX_READY:
                out, err = proc.communicate(timeout=2)
                raise ConformanceError(
                    f"sandbox failed before readiness: {line!r} {out!r} {err!r}"
                )

            if life is None:
                # Probe/conformance path only; no assay lifecycle or primary
                # C_view authority is created here.
                out, err = proc.communicate(input=input_bytes, timeout=5)
            else:
                if cost is None:
                    raise ConformanceError("production dispatch cost ledger missing")
                if proc.stdin is None:
                    raise ConformanceError("sandbox stdin unavailable")
                stdin = proc.stdin
                _write_exact_view_account_and_mark_t2(
                    stdin, input_bytes, cost, life
                )
                proc.stdin = None
                out, err = proc.communicate(timeout=5)
        except subprocess.TimeoutExpired as exc:
            proc.kill()
            proc.wait(timeout=2)
            if cost is not None and life is not None and Life.ORDER[2] not in life.events:
                cost.complete["C_view_bytes"] = False
            raise ConformanceError("sandbox execution timeout") from exc

    if proc.returncode != 0:
        raise ConformanceError(f"sandbox child nonzero exit {proc.returncode}: {err!r}")
    return bytes(out), bytes(err)


def _invoke_architecture_with_life(
    chi: str,
    view_bytes: bytes,
    cost: Cost,
    life: Life,
) -> ArchitectureResult:
    parse(chi, view_bytes)
    output_bytes, event_bytes = _spawn(
        _ops.architecture_source(chi),
        view_bytes,
        cost=cost,
        life=life,
    )
    return _ops._parse_architecture_result(output_bytes, event_bytes)


def run(chi: str, prepared: Prepared) -> Frozen:
    """Production path with authoritative exact-view dispatch accounting."""
    prepared.life.through(Life.ORDER[1])
    result = _invoke_architecture_with_life(
        chi,
        prepared.view_bytes,
        prepared.cost,
        prepared.life,
    )
    prepared.life.through(Life.ORDER[2])

    output_bytes = bytes(result.output_bytes)
    frozen = Frozen(
        result.terminal,
        output_bytes,
        shared_sha(output_bytes),
    )
    prepared.life.mark(Life.ORDER[3])

    _complete._merge_operation_events_fail_closed(
        prepared.cost, result.event_bytes
    )
    return frozen


def evaluate(chi: str, view_bytes: bytes):
    """Engineering-only evaluation; does not create primary view-cost authority."""
    return _persist.evaluate(chi, view_bytes)


def capability_probe(action: str, payload: dict[str, str]) -> str:
    """Retain the reviewed capability-probe path without primary cost authority."""
    return _persist.capability_probe(action, payload)
