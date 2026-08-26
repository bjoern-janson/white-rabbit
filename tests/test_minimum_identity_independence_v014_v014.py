from __future__ import annotations

import hashlib
import os
import tempfile
import threading
import unittest
from pathlib import Path
from unittest import mock

import tools.minimum_identity_independence_v014_v014 as m

A = b"mii-lifecycle-conformance:v1\ncondition=ALPHA\npayload=A"


def case() -> m.Case:
    return m.Case(
        semantic_case_id="SYNTHETIC_ONLY",
        frozen_bytes=A,
        materialized_bytes=A,
        executed_bytes=A,
        declared_object_id="ALPHA",
        convenience_identity_match=True,
        custody_override=None,
    )


def life_at_t1() -> m.Life:
    life = m.Life()
    life.mark(m.Life.ORDER[0])
    life.mark(m.Life.ORDER[1])
    return life


class DelayedWriter:
    def __init__(self) -> None:
        self.entered = threading.Event()
        self.release = threading.Event()
        self.data = bytearray()
        self.closed = False

    def write(self, payload) -> int:
        self.entered.set()
        if not self.release.wait(timeout=2):
            raise TimeoutError("test release timeout")
        chunk = bytes(payload)
        self.data.extend(chunk)
        return len(chunk)

    def flush(self) -> None:
        return None

    def close(self) -> None:
        self.closed = True


class BrokenWriter:
    def write(self, payload) -> int:
        raise BrokenPipeError("synthetic dispatch failure")

    def flush(self) -> None:
        return None

    def close(self) -> None:
        return None


class LifecycleRealizationConformance(unittest.TestCase):
    def test_01_prepare_stops_at_t1(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_3", case(), Path(td))
        self.assertEqual(tuple(prepared.life.events), m.Life.ORDER[:2])
        self.assertEqual(
            prepared.attestation["dispatched_view_sha256"],
            hashlib.sha256(prepared.view_bytes).hexdigest(),
        )

    def test_02_t2_cannot_precede_delayed_write_completion(self):
        writer = DelayedWriter()
        life = life_at_t1()
        errors = []

        def target():
            try:
                m._write_exact_view_and_mark_t2(writer, b"EXACT-VIEW", life)
            except Exception as exc:  # pragma: no cover - asserted below
                errors.append(exc)

        thread = threading.Thread(target=target)
        thread.start()
        self.assertTrue(writer.entered.wait(timeout=1))
        self.assertEqual(tuple(life.events), m.Life.ORDER[:2])
        self.assertNotIn(m.Life.ORDER[2], life.events)
        writer.release.set()
        thread.join(timeout=2)

        self.assertFalse(thread.is_alive())
        self.assertEqual(errors, [])
        self.assertEqual(bytes(writer.data), b"EXACT-VIEW")
        self.assertTrue(writer.closed)
        self.assertEqual(tuple(life.events), m.Life.ORDER[:3])

    def test_03_failed_view_write_never_emits_t2(self):
        life = life_at_t1()
        with self.assertRaises(m.ConformanceError):
            m._write_exact_view_and_mark_t2(BrokenWriter(), b"EXACT-VIEW", life)
        self.assertEqual(tuple(life.events), m.Life.ORDER[:2])

    def test_04_sandbox_readiness_failure_never_emits_t2(self):
        life = life_at_t1()
        with self.assertRaises(m.ConformanceError):
            m._spawn("raise SystemExit(9)", b"EXACT-VIEW", life=life)
        self.assertEqual(tuple(life.events), m.Life.ORDER[:2])

    def test_05_normal_run_realizes_t2_then_t3_then_t4(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_3", case(), Path(td))
            self.assertEqual(tuple(prepared.life.events), m.Life.ORDER[:2])
            frozen = m.run("chi_3", prepared)
            self.assertEqual(tuple(prepared.life.events), m.Life.ORDER[:4])
            self.assertEqual(frozen.terminal, "IDENTITY_PASS")
            self.assertEqual(
                frozen.output_sha256, hashlib.sha256(frozen.output_bytes).hexdigest()
            )
            self.assertEqual(m.score(prepared, frozen, False), 1)
            self.assertEqual(tuple(prepared.life.events), m.Life.ORDER)

    def test_06_t3_never_appears_if_terminal_freeze_path_fails(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_3", case(), Path(td))

        def fail_after_dispatch(chi, view_bytes, life):
            life.mark(m.Life.ORDER[2])
            raise m.ConformanceError("synthetic terminal failure")

        with mock.patch.object(m, "_invoke_architecture_with_life", fail_after_dispatch):
            with self.assertRaises(m.ConformanceError):
                m.run("chi_3", prepared)
        self.assertEqual(tuple(prepared.life.events), m.Life.ORDER[:3])
        self.assertNotIn(m.Life.ORDER[3], prepared.life.events)

    def test_07_t4_cannot_exist_before_t3(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_0", case(), Path(td))
        fake = m.Frozen(
            "IDENTITY_PASS",
            b'{"terminal":"IDENTITY_PASS"}',
            hashlib.sha256(b'{"terminal":"IDENTITY_PASS"}').hexdigest(),
        )
        with self.assertRaises(m.ConformanceError):
            m.score(prepared, fake, False)
        self.assertEqual(tuple(prepared.life.events), m.Life.ORDER[:2])

    def test_08_successor_spawn_retains_file_denial(self):
        with tempfile.TemporaryDirectory() as td:
            secret = Path(td) / "oracle-secret"
            secret.write_text("FORBIDDEN")
            result = m.capability_probe("file", {"path": str(secret)})
        self.assertTrue(result.startswith("DENIED:PermissionError"), result)

    def test_09_successor_spawn_retains_network_denial(self):
        self.assertEqual(m.capability_probe("socket", {}), "-1")
        self.assertEqual(m.capability_probe("socketpair", {}), "-1")

    def test_10_successor_spawn_retains_environment_denial(self):
        old = os.environ.get("MII_SECRET")
        os.environ["MII_SECRET"] = "HIDDEN-WORLD"
        try:
            self.assertEqual(
                m.capability_probe("env", {"name": "MII_SECRET"}), "NONE"
            )
        finally:
            if old is None:
                os.environ.pop("MII_SECRET", None)
            else:
                os.environ["MII_SECRET"] = old

    def test_11_identical_view_is_still_hidden_world_invariant(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_3", case(), Path(td))
        view = prepared.view_bytes
        old = os.environ.get("MII_SECRET")
        try:
            os.environ["MII_SECRET"] = "WORLD-A"
            life_a = life_at_t1()
            a = m._invoke_architecture_with_life("chi_3", view, life_a)
            os.environ["MII_SECRET"] = "WORLD-B-DIFFERENT"
            life_b = life_at_t1()
            b = m._invoke_architecture_with_life("chi_3", view, life_b)
        finally:
            if old is None:
                os.environ.pop("MII_SECRET", None)
            else:
                os.environ["MII_SECRET"] = old
        self.assertEqual(a, b)
        self.assertEqual(tuple(life_a.events), m.Life.ORDER[:3])
        self.assertEqual(tuple(life_b.events), m.Life.ORDER[:3])

    def test_12_projection_schema_remains_exact(self):
        for chi in ("chi_0", "chi_1", "chi_2", "chi_3"):
            with tempfile.TemporaryDirectory() as td:
                prepared = m.prepare(chi, case(), Path(td))
            parsed = m.parse(chi, prepared.view_bytes)
            expected = [field[0] for field in m.SCHEMAS[chi]["fields_in_order"]]
            self.assertEqual(list(parsed), expected)


if __name__ == "__main__":
    unittest.main()
