from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
import tarfile
from pathlib import Path


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def iter_raw_files(obs: Path):
    """Yield only raw run-custody files in a deterministic order.

    Derived results, prior archives, checksums, and other top-level analyzer
    outputs are intentionally excluded by construction.
    """
    run_dirs = sorted(
        p for p in obs.iterdir()
        if p.is_dir() and p.name.startswith("run-") and p.name[4:].isdigit()
    )
    for run_dir in run_dirs:
        for path in sorted(p for p in run_dir.rglob("*") if p.is_file()):
            yield path


def build_raw_custody_archive(obs: Path, output: Path) -> str:
    """Create deterministic gzip/tar custody from raw run directories only."""
    obs = obs.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)

    with output.open("wb") as raw_out:
        with gzip.GzipFile(fileobj=raw_out, mode="wb", filename="", mtime=0) as gz:
            with tarfile.open(fileobj=gz, mode="w", format=tarfile.PAX_FORMAT) as tar:
                for path in iter_raw_files(obs):
                    rel = path.relative_to(obs).as_posix()
                    data = path.read_bytes()
                    info = tarfile.TarInfo(name=f"{obs.name}/{rel}")
                    info.size = len(data)
                    info.mtime = 0
                    info.uid = 0
                    info.gid = 0
                    info.uname = ""
                    info.gname = ""
                    info.mode = 0o644
                    tar.addfile(info, io.BytesIO(data))

    return sha256_file(output)


def list_archive_members(archive: Path) -> list[str]:
    with tarfile.open(archive, "r:gz") as tar:
        return tar.getnames()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Deterministic raw-custody builder for historical G7 robustness observations."
    )
    parser.add_argument(
        "--obs",
        type=Path,
        default=Path(__file__).resolve().parents[1]
        / "observations"
        / "G7-neutral-control-robustness-v0.1.1",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output archive. Defaults to <obs>/raw-custody-v012.tar.gz.",
    )
    args = parser.parse_args()
    output = args.output or (args.obs / "raw-custody-v012.tar.gz")
    digest = build_raw_custody_archive(args.obs, output)
    result = {
        "status": "DETERMINISTIC_RAW_CUSTODY_BUILDER_ONLY",
        "scientific_authority_restored": False,
        "input_scope": "run-* directories only",
        "archive": str(output),
        "sha256": digest,
        "members": len(list_archive_members(output)),
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
