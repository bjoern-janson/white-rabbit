from __future__ import annotations

import hashlib
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import tools.minimum_identity_independence_v014_v017 as m

A = b"mii-projection-sha-conformance:v1\ncondition=ALPHA\npayload=A"


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


class ProjectionShaCompletionConformance(unittest.TestCase):
    def test_01_successful_projection_sha_increments_exactly_once(self):
        cost = m.Cost()
        before = cost.C_sha256_ops
        got = cost.projection_sha(b"abc")
        self.assertEqual(got, hashlib.sha256(b"abc").hexdigest())
        self.assertEqual(cost.C_sha256_ops, before + 1)

    def test_02_failed_projection_sha_does_not_increment(self):
        cost = m.Cost()
        before = cost.C_sha256_ops
        with mock.patch.object(
            m, "_projection_sha256_digest", side_effect=RuntimeError("forced sha failure")
        ):
            with self.assertRaises(RuntimeError):
                cost.projection_sha(b"abc")
        self.assertEqual(cost.C_sha256_ops, before)
        self.assertFalse(cost.complete["C_sha256_ops"])

    def test_03_failed_projection_sha_during_prepare_has_no_false_completed_count(self):
        tracking = m.Cost()
        with tempfile.TemporaryDirectory() as td:
            with mock.patch.object(m, "Cost", return_value=tracking):
                with mock.patch.object(
                    m,
                    "_projection_sha256_digest",
                    side_effect=RuntimeError("forced prepare sha failure"),
                ):
                    with self.assertRaises(RuntimeError):
                        m.prepare("chi_1", case(), Path(td))
        self.assertEqual(tracking.C_sha256_ops, 0)
        self.assertFalse(tracking.complete["C_sha256_ops"])

    def test_04_successful_chi1_prepare_records_two_completed_projection_hashes(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_1", case(), Path(td))
        self.assertEqual(prepared.cost.C_sha256_ops, 2)
        self.assertFalse(prepared.cost.complete["C_sha256_ops"])
        self.assertEqual(tuple(prepared.life.events), m.Life.ORDER[:2])

    def test_05_successful_chi3_prepare_records_three_projection_hashes_without_override(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_3", case(), Path(td))
        self.assertEqual(prepared.cost.C_sha256_ops, 3)
        self.assertFalse(prepared.cost.complete["C_sha256_ops"])

    def test_06_false_clean_custody_override_does_not_invent_projection_hash_work(self):
        override = hashlib.sha256(A).hexdigest()
        perturbed = case()
        perturbed = m.Case(
            semantic_case_id=perturbed.semantic_case_id,
            frozen_bytes=perturbed.frozen_bytes,
            materialized_bytes=perturbed.materialized_bytes,
            executed_bytes=perturbed.executed_bytes,
            declared_object_id=perturbed.declared_object_id,
            convenience_identity_match=perturbed.convenience_identity_match,
            custody_override=override,
        )
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_3", perturbed, Path(td))
        self.assertEqual(prepared.cost.C_sha256_ops, 2)

    def test_07_child_sha_path_remains_post_completion_event(self):
        source = m._complete._ops.architecture_source("chi_3")
        self.assertIn(
            'result=_h(data).hexdigest()\n    emit("SHA256_OPERATION")\n    return result',
            source,
        )
        self.assertNotIn(
            'emit("SHA256_OPERATION");return _h(data).hexdigest()',
            source,
        )

    def test_08_operation_measurement_still_starts_incomplete_after_prepare(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_3", case(), Path(td))
        for field in m._complete._OPERATION_FIELDS:
            self.assertFalse(prepared.cost.complete[field])
        self.assertFalse(prepared.cost.is_complete())

    def test_09_valid_zero_architecture_stream_can_complete_after_projection_counts(self):
        cost = m.Cost()
        cost.C_sha256_ops = 2
        m._complete._set_operation_measurement_complete(cost, False)
        delta = m._complete._merge_operation_events_fail_closed(cost, b"")
        self.assertEqual(delta, m.ArchitectureDelta(0, 0, 0))
        self.assertEqual(cost.C_sha256_ops, 2)
        for field in m._complete._OPERATION_FIELDS:
            self.assertTrue(cost.complete[field])

    def test_10_malformed_architecture_stream_still_leaves_total_sha_incomplete(self):
        cost = m.Cost()
        cost.C_sha256_ops = 2
        with self.assertRaises(m.ConformanceError):
            m._complete._merge_operation_events_fail_closed(
                cost, b"SHA256_OPERATION"
            )
        self.assertEqual(cost.C_sha256_ops, 2)
        self.assertFalse(cost.complete["C_sha256_ops"])


if __name__ == "__main__":
    unittest.main()
