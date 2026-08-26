import hashlib
import json
import os
import tempfile
import unittest
from pathlib import Path

import tools.minimum_identity_independence_v014_v013 as m


def chi3_view(payload: str = "abc") -> bytes:
    digest = hashlib.sha256(payload.encode()).hexdigest()
    view = {
        "schema_version": m.SCHEMAS["chi_3"]["schema_id"],
        "case_handle": "0" * 64,
        "declared_object_id": "ALPHA",
        "convenience_identity_match": True,
        "frozen_bytes_utf8": payload,
        "frozen_sha256": digest,
        "materialized_bytes_utf8": payload,
        "materialized_sha256": digest,
        "executed_raw_bytes_utf8": payload,
        "custody_reported_executed_sha256": digest,
    }
    return json.dumps(view, separators=(",", ":"), ensure_ascii=False).encode()


class RuntimeCapabilityIsolation(unittest.TestCase):
    def test_01_sandbox_runtime_is_available(self):
        self.assertTrue(m.sandbox_available())

    def test_02_forbidden_file_read_is_denied(self):
        with tempfile.TemporaryDirectory() as td:
            secret = Path(td) / "oracle-secret"
            secret.write_text("SECRET-A")
            result = m.capability_probe("file", {"path": str(secret)})
            self.assertTrue(result.startswith("DENIED:PermissionError"), result)

    def test_03_network_socket_creation_is_denied(self):
        self.assertEqual(m.capability_probe("socket", {}), "-1")

    def test_04_peer_ipc_socketpair_is_denied(self):
        self.assertEqual(m.capability_probe("socketpair", {}), "-1")

    def test_05_process_creation_is_denied(self):
        self.assertEqual(m.capability_probe("fork", {}), "-1")

    def test_06_parent_process_query_is_denied(self):
        self.assertEqual(m.capability_probe("getppid", {}), "-1")

    def test_07_arbitrary_import_is_denied(self):
        result = m.capability_probe("import", {"module": "socket"})
        self.assertTrue(result.startswith("DENIED:PermissionError"), result)

    def test_08_parent_environment_is_not_inherited(self):
        old = os.environ.get("MII_SECRET")
        os.environ["MII_SECRET"] = "HIDDEN-ORACLE-WORLD"
        try:
            self.assertEqual(m.capability_probe("env", {"name": "MII_SECRET"}), "NONE")
        finally:
            if old is None:
                os.environ.pop("MII_SECRET", None)
            else:
                os.environ["MII_SECRET"] = old

    def test_09_normal_chi3_survives_hard_sandbox(self):
        result = m.evaluate("chi_3", chi3_view())
        self.assertEqual(result.terminal, "IDENTITY_PASS")
        self.assertEqual(m._decode_events(result.event_bytes), m.ArchitectureDelta(1, 1, 2))

    def test_10_identical_view_is_invariant_to_hidden_parent_world(self):
        view = chi3_view()
        old = os.environ.get("MII_SECRET")
        with tempfile.TemporaryDirectory() as td:
            sentinel = Path(td) / "forbidden-parent-state"
            try:
                sentinel.write_text("WORLD-A")
                os.environ["MII_SECRET"] = "WORLD-A"
                result_a = m.evaluate("chi_3", view)

                sentinel.write_text("WORLD-B-DIFFERENT")
                os.environ["MII_SECRET"] = "WORLD-B-DIFFERENT"
                result_b = m.evaluate("chi_3", view)
            finally:
                if old is None:
                    os.environ.pop("MII_SECRET", None)
                else:
                    os.environ["MII_SECRET"] = old
        self.assertEqual(result_a, result_b)

    def test_11_hidden_file_changes_remain_unreadable(self):
        with tempfile.TemporaryDirectory() as td:
            secret = Path(td) / "oracle-secret"
            secret.write_text("WORLD-A")
            a = m.capability_probe("file", {"path": str(secret)})
            secret.write_text("WORLD-B")
            b = m.capability_probe("file", {"path": str(secret)})
        self.assertTrue(a.startswith("DENIED:PermissionError"), a)
        self.assertTrue(b.startswith("DENIED:PermissionError"), b)


if __name__ == "__main__":
    unittest.main()
