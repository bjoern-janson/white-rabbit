from __future__ import annotations

import json
import os
import platform
import select
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass

from tools.minimum_identity_independence_v014_v012 import *  # re-export frozen parent surfaces
import tools.minimum_identity_independence_v014_v012 as _base

EVENT_SHA256 = "SHA256_OPERATION"
EVENT_EXTRACT = "EXTRACT_OPERATION"
EVENT_COMPARE = "IDENTITY_COMPARE_OPERATION"
EVENTS = {EVENT_SHA256, EVENT_EXTRACT, EVENT_COMPARE}
SANDBOX_READY = b"SANDBOX_READY\n"

# Linux x86_64 syscalls denied after the trusted bootstrap and before V_i is read.
# This is deliberately fail-closed and architecture execution is unsupported on
# other kernels/architectures in v0.1.3.
_DENY_SYSCALLS = (
    2, 4, 6, 21, 22, 29, 30, 31, 35, 39, 41, 42, 43, 44, 45, 46, 47, 48,
    49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 62, 63, 64, 65, 66, 67,
    68, 69, 70, 71, 78, 79, 80, 81, 89, 96, 100, 101, 110, 155, 161, 165,
    166, 186, 200, 201, 217, 228, 229, 230, 234, 240, 250, 253, 257, 258,
    259, 260, 262, 263, 264, 265, 266, 267, 268, 269, 282, 284, 288, 289,
    290, 293, 294, 298, 299, 300, 303, 304, 307, 310, 311, 319, 321, 322,
    323, 332, 424, 425, 426, 427, 434, 435, 437, 438,
)

_BOOTSTRAP = r'''import builtins,ctypes,errno,hashlib,json,sys
from ctypes import Structure,c_ushort,c_ubyte,c_uint,POINTER
class _F(Structure): _fields_=[("code",c_ushort),("jt",c_ubyte),("jf",c_ubyte),("k",c_uint)]
class _P(Structure): _fields_=[("len",c_ushort),("filter",POINTER(_F))]
_DENY=DENY_LIST
BPF_LD=0x20;BPF_JEQ=0x15;BPF_RET=0x06;ALLOW=0x7fff0000;ERR=0x00050000|errno.EPERM
_ins=[_F(BPF_LD,0,0,0)]
for _n in _DENY:_ins.extend((_F(BPF_JEQ,0,1,_n),_F(BPF_RET,0,0,ERR)))
_ins.append(_F(BPF_RET,0,0,ALLOW));_arr=(_F*len(_ins))(*_ins);_prog=_P(len(_ins),_arr)
_libc=ctypes.CDLL(None,use_errno=True)
if _libc.prctl(38,1,0,0,0)!=0: raise SystemExit(70)
if _libc.prctl(22,2,ctypes.byref(_prog))!=0: raise SystemExit(71)
_stdin=sys.stdin.buffer;_stdout=sys.stdout;_stderr=sys.stderr
_loads=json.loads;_dumps=json.dumps;_sha256=hashlib.sha256

def _deny_import(*a,**k): raise PermissionError("imports denied")
builtins.__import__=_deny_import
sys.modules.clear()
del ctypes,errno,hashlib,json,builtins,_libc,_arr,_prog,_ins,_F,_P

def emit(event,_err=_stderr):
    _err.write(event+"\n");_err.flush();return None

def compare(a,b): emit("IDENTITY_COMPARE_OPERATION");return a==b

def extract(text): emit("EXTRACT_OPERATION");return text.encode()

def digest(data,_h=_sha256): emit("SHA256_OPERATION");return _h(data).hexdigest()

_stderr.write("SANDBOX_READY\n");_stderr.flush()
data=_stdin.read()
view=_loads(data.decode(),object_pairs_hook=dict)
if list(view)!=EXPECTED_KEYS: raise SystemExit(82)
if _dumps(view,separators=(",",":"),ensure_ascii=False).encode()!=data: raise SystemExit(83)
'''

_CHILD_BODY = {
    "chi_0": 'value=view["convenience_identity_match"]\nterminal="IDENTITY_PASS" if value is True else "IDENTITY_MISMATCH" if value is False else "IDENTITY_UNRESOLVED"\n',
    "chi_1": 'terminal="IDENTITY_MISMATCH" if not compare(view["frozen_sha256"],view["materialized_sha256"]) else "IDENTITY_UNRESOLVED"\n',
    "chi_2": 'if not compare(view["frozen_sha256"],view["materialized_sha256"]):\n    terminal="IDENTITY_MISMATCH"\nelse:\n    terminal="IDENTITY_PASS" if compare(view["materialized_sha256"],view["custody_reported_executed_sha256"]) else "IDENTITY_MISMATCH"\n',
    "chi_3": 'if not compare(view["frozen_sha256"],view["materialized_sha256"]):\n    terminal="IDENTITY_MISMATCH"\nelse:\n    executed_hash=digest(extract(view["executed_raw_bytes_utf8"]))\n    terminal="IDENTITY_PASS" if compare(view["materialized_sha256"],executed_hash) else "IDENTITY_MISMATCH"\n',
}
_CHILD_EPILOGUE = '_stdout.write(_dumps({"terminal":terminal},separators=(",",":")));_stdout.flush()\n'


def sandbox_available() -> bool:
    return (
        sys.platform.startswith("linux")
        and platform.machine().lower() in {"x86_64", "amd64"}
        and shutil.which("unshare") is not None
        and os.path.isabs(getattr(sys, "_base_executable", sys.executable))
    )


def _launcher() -> list[str]:
    if not sandbox_available():
        raise ConformanceError("runtime sandbox unavailable; fail closed")
    return [
        shutil.which("unshare"),
        "--user",
        "--map-root-user",
        "--net",
        "--pid",
        "--fork",
        getattr(sys, "_base_executable", sys.executable),
        "-I",
        "-S",
        "-c",
    ]


def architecture_source(chi: str) -> str:
    if chi not in _base.SCHEMAS:
        raise ConformanceError("unknown architecture")
    keys = [field[0] for field in _base.SCHEMAS[chi]["fields_in_order"]]
    return (
        "EXPECTED_KEYS=" + repr(keys) + "\nDENY_LIST=" + repr(list(_DENY_SYSCALLS)) + "\n"
        + _BOOTSTRAP + _CHILD_BODY[chi] + _CHILD_EPILOGUE
    )


@dataclass(frozen=True)
class ArchitectureResult:
    terminal: str
    output_bytes: bytes
    event_bytes: bytes


def _spawn(source: str, input_bytes: bytes) -> tuple[bytes, bytes]:
    with tempfile.TemporaryDirectory(prefix="mii-sandbox-") as td:
        proc = subprocess.Popen(
            _launcher() + [source],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=td,
            env={},
            close_fds=True,
        )
        try:
            ready, _, _ = select.select([proc.stderr], [], [], 5)
            if not ready:
                proc.kill(); proc.wait(timeout=2)
                raise ConformanceError("sandbox readiness timeout")
            line = proc.stderr.readline()
            if line != SANDBOX_READY:
                out, err = proc.communicate(timeout=2)
                raise ConformanceError(f"sandbox failed before readiness: {line!r} {out!r} {err!r}")
            out, err = proc.communicate(input=input_bytes, timeout=5)
        except subprocess.TimeoutExpired as exc:
            proc.kill(); proc.wait(timeout=2)
            raise ConformanceError("sandbox execution timeout") from exc
    if proc.returncode != 0:
        raise ConformanceError(f"sandbox child nonzero exit {proc.returncode}: {err!r}")
    return bytes(out), bytes(err)


def _invoke_architecture(chi: str, view_bytes: bytes) -> ArchitectureResult:
    _base.parse(chi, view_bytes)
    output_bytes, event_bytes = _spawn(architecture_source(chi), view_bytes)
    try:
        output = json.loads(output_bytes.decode(), object_pairs_hook=dict)
    except Exception as exc:
        raise ConformanceError("invalid architecture output") from exc
    if list(output) != ["terminal"] or output.get("terminal") not in _base.TERMINALS:
        raise ConformanceError("invalid architecture terminal")
    if json.dumps(output, separators=(",", ":")).encode() != output_bytes:
        raise ConformanceError("noncanonical architecture output")
    return ArchitectureResult(output["terminal"], output_bytes, event_bytes)


def chi_0(view_bytes: bytes) -> str: return _invoke_architecture("chi_0", view_bytes).terminal
def chi_1(view_bytes: bytes) -> str: return _invoke_architecture("chi_1", view_bytes).terminal
def chi_2(view_bytes: bytes) -> str: return _invoke_architecture("chi_2", view_bytes).terminal
def chi_3(view_bytes: bytes) -> str: return _invoke_architecture("chi_3", view_bytes).terminal

def evaluate(chi: str, view_bytes: bytes) -> ArchitectureResult:
    return _invoke_architecture(chi, view_bytes)


def _decode_events(event_bytes: bytes) -> ArchitectureDelta:
    if event_bytes and not event_bytes.endswith(b"\n"):
        raise ConformanceError("unterminated instrumentation event")
    try:
        rows = event_bytes.decode("ascii").splitlines() if event_bytes else []
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
    prepared.cost.merge_architecture_delta(_decode_events(result.event_bytes))
    return frozen

# Capability-denial probes use the exact same launcher/bootstrap/filter. Probe-only
# code is appended after SANDBOX_READY and is not part of any production chi_i.
def _probe_source(action: str) -> str:
    probe_boot = r'''import builtins,ctypes,errno,json,sys
from ctypes import Structure,c_ushort,c_ubyte,c_uint,POINTER
class _F(Structure): _fields_=[("code",c_ushort),("jt",c_ubyte),("jf",c_ubyte),("k",c_uint)]
class _P(Structure): _fields_=[("len",c_ushort),("filter",POINTER(_F))]
_DENY=DENY_LIST;BPF_LD=0x20;BPF_JEQ=0x15;BPF_RET=0x06;ALLOW=0x7fff0000;ERR=0x00050000|errno.EPERM
_ins=[_F(BPF_LD,0,0,0)]
for _n in _DENY:_ins.extend((_F(BPF_JEQ,0,1,_n),_F(BPF_RET,0,0,ERR)))
_ins.append(_F(BPF_RET,0,0,ALLOW));_arr=(_F*len(_ins))(*_ins);_prog=_P(len(_ins),_arr)
_libc=ctypes.CDLL(None,use_errno=True);_libc.syscall.restype=ctypes.c_long;_libc.getenv.restype=ctypes.c_char_p
if _libc.prctl(38,1,0,0,0)!=0: raise SystemExit(70)
if _libc.prctl(22,2,ctypes.byref(_prog))!=0: raise SystemExit(71)
def _deny_import(*a,**k): raise PermissionError("imports denied")
builtins.__import__=_deny_import
sys.stderr.write("SANDBOX_READY\n");sys.stderr.flush()
p=json.loads(sys.stdin.read());a=ACTION
try:
    if a=="file": open(p["path"],"rb").read();r="AVAILABLE"
    elif a=="socket": r=str(_libc.syscall(41,2,1,0))
    elif a=="socketpair": r=str(_libc.syscall(53,1,1,0,0))
    elif a=="fork": r=str(_libc.syscall(57))
    elif a=="getppid": r=str(_libc.syscall(110))
    elif a=="import": __import__(p["module"]);r="AVAILABLE"
    elif a=="env":
        v=_libc.getenv(p["name"].encode());r="NONE" if not v else v.decode()
    else: r="UNKNOWN"
except Exception as e: r="DENIED:"+type(e).__name__+":"+str(getattr(e,"errno",None))
sys.stdout.write(r);sys.stdout.flush()
'''
    return "DENY_LIST=" + repr(list(_DENY_SYSCALLS)) + "\nACTION=" + repr(action) + "\n" + probe_boot


def capability_probe(action: str, payload: dict[str, str]) -> str:
    out, err = _spawn(_probe_source(action), json.dumps(payload, separators=(",", ":")).encode())
    if err:
        raise ConformanceError(f"unexpected probe event stream: {err!r}")
    return out.decode()
