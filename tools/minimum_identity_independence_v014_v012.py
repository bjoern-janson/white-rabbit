from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from dataclasses import dataclass

from tools.minimum_identity_independence_v014_v011 import (
    ArchitectureDelta,
    Case,
    ConformanceError,
    Cost,
    Frozen,
    HEX64,
    Life,
    ORACLE_BLOB,
    ORACLE_VERSION,
    PRIMARY_FIELDS,
    Prepared,
    SCHEMAS,
    SCHEMA_SHA,
    Store,
    TERMINALS,
    aggregate,
    dominates,
    git_blob_sha1,
    load_oracle,
    pareto,
    parse,
    prepare,
    resolve_case,
    schema_sha,
    score,
    serialize,
    shared_sha,
    validate,
    verify_schemas,
)

EVENT_SHA256 = "SHA256_OPERATION"
EVENT_EXTRACT = "EXTRACT_OPERATION"
EVENT_COMPARE = "IDENTITY_COMPARE_OPERATION"
EVENTS = {EVENT_SHA256, EVENT_EXTRACT, EVENT_COMPARE}

_CHILD_PRELUDE = r'''import hashlib,json,sys

def emit(event):
    print(event,file=sys.stderr,flush=True)
    return None

def compare(left,right):
    emit("IDENTITY_COMPARE_OPERATION")
    return left==right

def extract(text):
    emit("EXTRACT_OPERATION")
    return text.encode()

def digest(data):
    emit("SHA256_OPERATION")
    return hashlib.sha256(data).hexdigest()

data=sys.stdin.buffer.read()
if data.startswith(b"\xef\xbb\xbf") or data.endswith(b"\n"):
    raise SystemExit(81)
view=json.loads(data.decode(),object_pairs_hook=dict)
if list(view)!=EXPECTED_KEYS:
    raise SystemExit(82)
if json.dumps(view,separators=(",",":"),ensure_ascii=False).encode()!=data:
    raise SystemExit(83)
'''

_CHILD_BODY = {
    "chi_0": r'''value=view["convenience_identity_match"]
terminal="IDENTITY_PASS" if value is True else "IDENTITY_MISMATCH" if value is False else "IDENTITY_UNRESOLVED"
''',
    "chi_1": r'''terminal="IDENTITY_MISMATCH" if not compare(view["frozen_sha256"],view["materialized_sha256"]) else "IDENTITY_UNRESOLVED"
''',
    "chi_2": r'''if not compare(view["frozen_sha256"],view["materialized_sha256"]):
    terminal="IDENTITY_MISMATCH"
else:
    terminal="IDENTITY_PASS" if compare(view["materialized_sha256"],view["custody_reported_executed_sha256"]) else "IDENTITY_MISMATCH"
''',
    "chi_3": r'''if not compare(view["frozen_sha256"],view["materialized_sha256"]):
    terminal="IDENTITY_MISMATCH"
else:
    executed_hash=digest(extract(view["executed_raw_bytes_utf8"]))
    terminal="IDENTITY_PASS" if compare(view["materialized_sha256"],executed_hash) else "IDENTITY_MISMATCH"
''',
}

_CHILD_EPILOGUE = r'''sys.stdout.write(json.dumps({"terminal":terminal},separators=(",",":")))
sys.stdout.flush()
'''


def architecture_source(chi: str) -> str:
    if chi not in SCHEMAS:
        raise ConformanceError("unknown architecture")
    keys = [field[0] for field in SCHEMAS[chi]["fields_in_order"]]
    return (
        "EXPECTED_KEYS="
        + repr(keys)
        + "\n"
        + _CHILD_PRELUDE
        + _CHILD_BODY[chi]
        + _CHILD_EPILOGUE
    )


def _minimal_child_env() -> dict[str, str]:
    # No PYTHONPATH/PWD/user variables are inherited. Windows runtime roots are
    # permitted because they contain no case/oracle state.
    env: dict[str, str] = {}
    for key in ("SYSTEMROOT", "WINDIR"):
        value = os.environ.get(key)
        if value:
            env[key] = value
    return env


@dataclass(frozen=True)
class ArchitectureResult:
    terminal: str
    output_bytes: bytes
    event_bytes: bytes


def _invoke_architecture(chi: str, view_bytes: bytes) -> ArchitectureResult:
    # Harness validates the exact bytes; the child receives those exact bytes on
    # stdin. No case label, oracle field, ordinal, meter, or ledger is in argv/env.
    parse(chi, view_bytes)
    source = architecture_source(chi)
    with tempfile.TemporaryDirectory(prefix="mii-arch-") as td:
        try:
            completed = subprocess.run(
                [sys.executable, "-I", "-c", source],
                input=view_bytes,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=td,
                env=_minimal_child_env(),
                timeout=5,
                check=False,
            )
        except (OSError, subprocess.SubprocessError) as exc:
            raise ConformanceError("architecture process failure") from exc

    if completed.returncode != 0:
        raise ConformanceError(
            f"architecture process nonzero exit {completed.returncode}: {completed.stderr!r}"
        )

    # Copy/freeze terminal bytes before instrumentation events are interpreted.
    output_bytes = bytes(completed.stdout)
    event_bytes = bytes(completed.stderr)
    try:
        output = json.loads(output_bytes.decode(), object_pairs_hook=dict)
    except Exception as exc:
        raise ConformanceError("invalid architecture output") from exc
    if list(output) != ["terminal"] or output.get("terminal") not in TERMINALS:
        raise ConformanceError("invalid architecture terminal")
    if json.dumps(output, separators=(",", ":")).encode() != output_bytes:
        raise ConformanceError("noncanonical architecture output")
    return ArchitectureResult(output["terminal"], output_bytes, event_bytes)


def chi_0(view_bytes: bytes) -> str:
    return _invoke_architecture("chi_0", view_bytes).terminal


def chi_1(view_bytes: bytes) -> str:
    return _invoke_architecture("chi_1", view_bytes).terminal


def chi_2(view_bytes: bytes) -> str:
    return _invoke_architecture("chi_2", view_bytes).terminal


def chi_3(view_bytes: bytes) -> str:
    return _invoke_architecture("chi_3", view_bytes).terminal


_ARCHITECTURES = {"chi_0", "chi_1", "chi_2", "chi_3"}


def evaluate(chi: str, view_bytes: bytes) -> ArchitectureResult:
    if chi not in _ARCHITECTURES:
        raise ConformanceError("unknown architecture")
    return _invoke_architecture(chi, view_bytes)


def _decode_events(event_bytes: bytes) -> ArchitectureDelta:
    if not event_bytes:
        rows: list[str] = []
    else:
        if not event_bytes.endswith(b"\n"):
            raise ConformanceError("unterminated instrumentation event")
        try:
            rows = event_bytes.decode("ascii").splitlines()
        except UnicodeDecodeError as exc:
            raise ConformanceError("non-ascii instrumentation event") from exc
    if any(row not in EVENTS for row in rows):
        raise ConformanceError("unknown instrumentation event")
    return ArchitectureDelta(
        sha256_ops=sum(row == EVENT_SHA256 for row in rows),
        extract_ops=sum(row == EVENT_EXTRACT for row in rows),
        identity_compare_ops=sum(row == EVENT_COMPARE for row in rows),
    )


def run(chi: str, prepared: Prepared) -> Frozen:
    prepared.life.through(Life.ORDER[2])
    result = evaluate(chi, prepared.view_bytes)
    frozen = Frozen(result.terminal, result.output_bytes, shared_sha(result.output_bytes))
    prepared.life.mark(Life.ORDER[3])
    # One-way event stream is interpreted and merged only after output freeze/T3.
    prepared.cost.merge_architecture_delta(_decode_events(result.event_bytes))
    return frozen
