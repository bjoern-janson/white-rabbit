# Minimum Identity Independence Implementation v0.1.3

Version: `MINIMUM_IDENTITY_INDEPENDENCE_IMPLEMENTATION_V0.1.3`

Status: `IMPLEMENTED / CAPABILITY_DENIAL_FIXTURES_PASS / IMPLEMENTATION_REVIEW_REQUIRED / NOT_EXECUTED / NON_AUTHORIZING`

This artifact records the minimal runtime-capability successor after `MINIMUM_IDENTITY_INDEPENDENCE_IMPLEMENTATION_V0.1.2` failed hostile implementation review because `python -I` did not make filesystem/network/process capabilities unavailable.

It does not authorize the constituted 36 architecture-case evaluations.

## Authority

```text
constitution
assays/MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0_1_4.md
blob: f6d7817153176383b24c283ccc1e421b298fff1a

constitution hostile review
assays/MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0_1_4_REVIEW.md
blob: 08436c34754503313219b11fac7dcd5d199634b3

historical implementation blocker
assays/MINIMUM_IDENTITY_INDEPENDENCE_IMPLEMENTATION_V0_1_2_REVIEW.md
blob: 731ce97ff0ecb5ee5836b1b709bdfe345a206293

successor implementation
tools/minimum_identity_independence_v014_v013.py
commit introducing file: 8dddf5cc56a63305d72a81eb1c62e57f074df2c5
blob: 11957b8b90c68cd45c40a9a2e2161a40d06cb91f

capability-denial fixtures
tests/test_minimum_identity_independence_v014_v013.py
commit introducing file: 31c64fd58b1a4d6fe8da7cb594bd3d6b3139ccf1
blob: e8ea93a37b3443577dda11d754837ff9c31da042
```

The committed implementation and fixture blob identities equal the exact locally executed bytes.

## Sole intended repair

No constitution, oracle, view schema, architecture logic, scoring rule, cost contract, or result rule is changed.

The sole repair is the `T2 -> T3` architecture runtime capability boundary.

The successor requires Linux x86_64 and fails closed if the required sandbox primitive is unavailable.

Each architecture evaluation is launched through:

```text
unshare
  --user --map-root-user
  --net
  --pid --fork
```

followed by a fresh base Python interpreter in isolated/no-site mode.

Before the child reads `V_i`, a trusted bootstrap:

1. installs `PR_SET_NO_NEW_PRIVS`;
2. installs a seccomp BPF deny filter;
3. disables subsequent Python imports;
4. clears `sys.modules` discovery state;
5. emits `SANDBOX_READY`;
6. only then reads the exact serialized `V_i` bytes from stdin.

The parent does not send `V_i` before `SANDBOX_READY`.

## Architecture-visible channels after readiness

After the sandbox readiness barrier, the intended architecture-visible channels are:

```text
stdin  = exact V_i bytes only
stdout = terminal result only
stderr = write-only fixed operation-event stream only
```

The child receives:

```text
env = {}
close_fds = true
fresh temporary cwd
fresh PID namespace
fresh network namespace
```

No cost ledger, meter, semantic case ID, oracle verdict, case partition, prior-run state, or parent environment is supplied.

## Capability denial

The seccomp filter denies the syscall families used for:

```text
filesystem open/path inspection
network sockets/connect/peer IPC
fork/clone/exec
process inspection / ptrace / process_vm
mount/setns/unshare/chroot
SysV/POSIX-like IPC creation surfaces
io_uring setup
pidfd access
selected clock/process-metadata surfaces
```

The implementation is deliberately fail-closed outside the frozen Linux x86_64 runtime target.

## Conformance fixtures executed

Only synthetic implementation-conformance fixtures were executed.

```text
capability-denial fixtures: 11
local result: PASS
constituted assay architecture-case evaluations: 0
scientific/model observations: 0
```

The exact committed fixture suite verifies:

```text
sandbox runtime available
forbidden sentinel-file read denied
network socket creation denied
socketpair / peer IPC denied
fork denied
parent-process query denied
arbitrary import denied
parent environment not inherited
normal chi_3 evaluation still works
same exact V_i under different hidden parent state -> identical architecture result/event trace
changed forbidden sentinel contents remain unreadable
```

The local runtime used for the fixture pass was Linux x86_64 with user/network/PID namespaces available.

These are engineering conformance observations only. They are not assay observations.

## One-way instrumentation retained

The v0.1.2 one-way instrumentation repair remains in force:

```text
architecture operation
  -> fixed event token on stderr
  -> parent capture
  -> output frozen at T3
  -> event decode / cost merge after T3
```

No meter or counter object exists inside the production architecture logic.

## Execution firewall

```text
constituted assay architecture-case evaluations executed: 0
scientific/model observations: 0
Gate 7 observations created: 0
```

Next permitted action:

```text
HOSTILE IMPLEMENTATION-CONFORMANCE REVIEW FROM GATE 1
```

Execution remains unauthorized.
