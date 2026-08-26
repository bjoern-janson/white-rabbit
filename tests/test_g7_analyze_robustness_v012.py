from __future__ import annotations

import hashlib
import tarfile
import tempfile
import unittest
from pathlib import Path

from tools.g7_analyze_robustness_v012 import (
    build_raw_custody_archive,
    list_archive_members,
)


class RobustnessRawCustodyV012Tests(unittest.TestCase):
    def fixture(self, root: Path) -> Path:
        obs = root / "G7-neutral-control-robustness-v0.1.1"
        (obs / "run-001" / "recorder-runs" / "a").mkdir(parents=True)
        (obs / "run-002").mkdir(parents=True)
        (obs / "run-001" / "slot-state.json").write_text('{"a":1}\n')
        (obs / "run-001" / "recorder-runs" / "a" / "body.raw").write_bytes(b"abc")
        (obs / "run-002" / "slot-state.json").write_text('{"b":2}\n')
        # Derived/stale files must never enter the raw archive.
        (obs / "derived-results.json").write_text('{"stale":true}\n')
        (obs / "raw-custody.sha256").write_text("old\n")
        (obs / "raw-custody.tar.gz").write_bytes(b"old")
        return obs

    def test_archive_is_deterministic_and_excludes_derived_artifacts(self):
        with tempfile.TemporaryDirectory() as td:
            obs = self.fixture(Path(td))
            a = Path(td) / "a.tar.gz"
            b = Path(td) / "b.tar.gz"
            ha = build_raw_custody_archive(obs, a)

            # Mutate top-level derived outputs only; raw custody is unchanged.
            (obs / "derived-results.json").write_text('{"stale":false,"more":1}\n')
            (obs / "new-derived.txt").write_text("ignore me\n")
            hb = build_raw_custody_archive(obs, b)

            self.assertEqual(ha, hb)
            self.assertEqual(a.read_bytes(), b.read_bytes())

            members = list_archive_members(a)
            self.assertEqual(
                members,
                [
                    f"{obs.name}/run-001/recorder-runs/a/body.raw",
                    f"{obs.name}/run-001/slot-state.json",
                    f"{obs.name}/run-002/slot-state.json",
                ],
            )
            self.assertFalse(any("derived-results" in x for x in members))
            self.assertFalse(any("raw-custody" in x for x in members))

    def test_tar_metadata_is_normalized(self):
        with tempfile.TemporaryDirectory() as td:
            obs = self.fixture(Path(td))
            archive = Path(td) / "a.tar.gz"
            build_raw_custody_archive(obs, archive)
            with tarfile.open(archive, "r:gz") as tar:
                for member in tar.getmembers():
                    self.assertEqual(member.mtime, 0)
                    self.assertEqual(member.uid, 0)
                    self.assertEqual(member.gid, 0)
                    self.assertEqual(member.uname, "")
                    self.assertEqual(member.gname, "")
                    self.assertEqual(member.mode, 0o644)

    def test_raw_change_changes_digest(self):
        with tempfile.TemporaryDirectory() as td:
            obs = self.fixture(Path(td))
            a = Path(td) / "a.tar.gz"
            b = Path(td) / "b.tar.gz"
            ha = build_raw_custody_archive(obs, a)
            (obs / "run-002" / "slot-state.json").write_text('{"b":3}\n')
            hb = build_raw_custody_archive(obs, b)
            self.assertNotEqual(ha, hb)


if __name__ == "__main__":
    unittest.main()
