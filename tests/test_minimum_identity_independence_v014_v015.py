from __future__ import annotations

import hashlib
import io
import json
import tempfile
import unittest
from pathlib import Path

import tools.minimum_identity_independence_v014_v015 as m

A = b"mii-completed-op-conformance:v1\ncondition=ALPHA\npayload=A"


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


def primitive_namespace():
    stderr = io.StringIO()
    ns = {
        "_stderr": stderr,
        "_sha256": hashlib.sha256,
    }
    exec(m._COMPLETED_PRIMITIVE_BLOCK, ns)
    return ns, stderr


class BadEq:
    def __eq__(self, other):
        raise RuntimeError("forced compare failure")


class BadEncode:
    def encode(self):
        raise RuntimeError("forced extract failure")


class CompletedOperationEventConformance(unittest.TestCase):
    def test_01_production_source_contains_post_completion_compare_event(self):
        source = m.architecture_source("chi_3")
        self.assertIn(
            'result=a==b\n    emit("IDENTITY_COMPARE_OPERATION")\n    return result',
            source,
        )
        self.assertNotIn(
            'emit("IDENTITY_COMPARE_OPERATION");return a==b',
            source,
        )

    def test_02_production_source_contains_post_completion_extract_event(self):
        source = m.architecture_source("chi_3")
        self.assertIn(
            'result=text.encode()\n    emit("EXTRACT_OPERATION")\n    return result',
            source,
        )
        self.assertNotIn(
            'emit("EXTRACT_OPERATION");return text.encode()',
            source,
        )

    def test_03_production_source_contains_post_completion_sha_event(self):
        source = m.architecture_source("chi_3")
        self.assertIn(
            'result=_h(data).hexdigest()\n    emit("SHA256_OPERATION")\n    return result',
            source,
        )
        self.assertNotIn(
            'emit("SHA256_OPERATION");return _h(data).hexdigest()',
            source,
        )

    def test_04_failed_compare_emits_no_completed_event(self):
        ns, stderr = primitive_namespace()
        with self.assertRaises(RuntimeError):
            ns["compare"](BadEq(), object())
        self.assertEqual(stderr.getvalue(), "")

    def test_05_failed_extract_emits_no_completed_event(self):
        ns, stderr = primitive_namespace()
        with self.assertRaises(RuntimeError):
            ns["extract"](BadEncode())
        self.assertEqual(stderr.getvalue(), "")

    def test_06_failed_sha_emits_no_completed_event(self):
        ns, stderr = primitive_namespace()
        with self.assertRaises(TypeError):
            ns["digest"](object())
        self.assertEqual(stderr.getvalue(), "")

    def test_07_successful_compare_emits_exactly_one_event(self):
        ns, stderr = primitive_namespace()
        self.assertTrue(ns["compare"]("a", "a"))
        self.assertEqual(stderr.getvalue(), "IDENTITY_COMPARE_OPERATION\n")

    def test_08_successful_extract_emits_exactly_one_event(self):
        ns, stderr = primitive_namespace()
        self.assertEqual(ns["extract"]("abc"), b"abc")
        self.assertEqual(stderr.getvalue(), "EXTRACT_OPERATION\n")

    def test_09_successful_sha_emits_exactly_one_event(self):
        ns, stderr = primitive_namespace()
        self.assertEqual(ns["digest"](b"abc"), hashlib.sha256(b"abc").hexdigest())
        self.assertEqual(stderr.getvalue(), "SHA256_OPERATION\n")

    def test_10_event_sink_still_returns_none(self):
        ns, stderr = primitive_namespace()
        self.assertIsNone(ns["emit"]("IDENTITY_COMPARE_OPERATION"))
        self.assertEqual(stderr.getvalue(), "IDENTITY_COMPARE_OPERATION\n")

    def test_11_normal_chi3_event_vector_unchanged(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_3", case(), Path(td))
            result = m.evaluate("chi_3", prepared.view_bytes)
        self.assertEqual(result.terminal, "IDENTITY_PASS")
        self.assertEqual(
            m._decode_events(result.event_bytes),
            m.ArchitectureDelta(1, 1, 2),
        )

    def test_12_lifecycle_realization_remains_t1_prepare_t2_dispatch_t3_freeze(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_3", case(), Path(td))
            self.assertEqual(tuple(prepared.life.events), m.Life.ORDER[:2])
            frozen = m.run("chi_3", prepared)
        self.assertEqual(frozen.terminal, "IDENTITY_PASS")
        self.assertEqual(tuple(prepared.life.events), m.Life.ORDER[:4])

    def test_13_runtime_capability_denial_is_retained(self):
        with tempfile.TemporaryDirectory() as td:
            secret = Path(td) / "oracle-secret"
            secret.write_text("FORBIDDEN")
            file_result = m.capability_probe("file", {"path": str(secret)})
        self.assertTrue(file_result.startswith("DENIED:PermissionError"), file_result)
        self.assertEqual(m.capability_probe("socket", {}), "-1")

    def test_14_primary_operation_counts_merge_after_t3(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_3", case(), Path(td))
            pre = prepared.cost.vector()
            m.run("chi_3", prepared)
            post = prepared.cost.vector()
        self.assertGreater(post[3], pre[3])
        self.assertGreater(post[4], pre[4])
        self.assertGreater(post[5], pre[5])
        self.assertEqual(prepared.life.events[-1], m.Life.ORDER[3])


if __name__ == "__main__":
    unittest.main()
