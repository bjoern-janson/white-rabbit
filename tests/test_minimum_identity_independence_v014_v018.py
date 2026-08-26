from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest import mock

import tools.minimum_identity_independence_v014_v018 as m

A = b"mii-capture-conformance:v1\ncondition=ALPHA\npayload=A"


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


class CaptureCompletionConformance(unittest.TestCase):
    def test_01_successful_capture_counts_actual_returned_bytes(self):
        cost = m.Cost()
        out = cost.capture(b"abc")
        self.assertEqual(out, b"abc")
        self.assertEqual(cost.C_capture_bytes, len(out))
        self.assertTrue(cost.complete["C_capture_bytes"])

    def test_02_failed_capture_does_not_increment_and_is_incomplete(self):
        cost = m.Cost()
        before = cost.C_capture_bytes
        with mock.patch.object(
            m, "_capture_identity_bytes", side_effect=RuntimeError("forced capture failure")
        ):
            with self.assertRaises(RuntimeError):
                cost.capture(b"abc")
        self.assertEqual(cost.C_capture_bytes, before)
        self.assertFalse(cost.complete["C_capture_bytes"])

    def test_03_partial_capture_counts_only_actual_bytes_and_is_incomplete(self):
        cost = m.Cost()
        with mock.patch.object(m, "_capture_identity_bytes", return_value=b"ab"):
            with self.assertRaises(m.ConformanceError):
                cost.capture(b"abc")
        self.assertEqual(cost.C_capture_bytes, 2)
        self.assertFalse(cost.complete["C_capture_bytes"])

    def test_04_failed_required_capture_during_prepare_never_becomes_complete_zero(self):
        tracking = m.Cost()
        with tempfile.TemporaryDirectory() as td:
            with mock.patch.object(m, "Cost", return_value=tracking):
                with mock.patch.object(
                    m,
                    "_capture_identity_bytes",
                    side_effect=RuntimeError("forced prepare capture failure"),
                ):
                    with self.assertRaises(RuntimeError):
                        m.prepare("chi_2", case(), Path(td))
        self.assertEqual(tracking.C_capture_bytes, 0)
        self.assertFalse(tracking.complete["C_capture_bytes"])

    def test_05_chi2_prepare_captures_exact_executed_bytes(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_2", case(), Path(td))
        self.assertEqual(prepared.cost.C_capture_bytes, len(A))
        self.assertTrue(prepared.cost.complete["C_capture_bytes"])

    def test_06_chi3_prepare_captures_exact_executed_bytes(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_3", case(), Path(td))
        self.assertEqual(prepared.cost.C_capture_bytes, len(A))
        self.assertTrue(prepared.cost.complete["C_capture_bytes"])

    def test_07_chi0_valid_no_capture_path_is_complete_zero(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_0", case(), Path(td))
        self.assertEqual(prepared.cost.C_capture_bytes, 0)
        self.assertTrue(prepared.cost.complete["C_capture_bytes"])

    def test_08_chi1_valid_no_capture_path_is_complete_zero(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_1", case(), Path(td))
        self.assertEqual(prepared.cost.C_capture_bytes, 0)
        self.assertTrue(prepared.cost.complete["C_capture_bytes"])

    def test_09_projection_sha_completed_work_semantics_are_retained(self):
        cost = m.Cost()
        before = cost.C_sha256_ops
        cost.projection_sha(b"abc")
        self.assertEqual(cost.C_sha256_ops, before + 1)

    def test_10_operation_measurement_remains_pending_after_prepare(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_3", case(), Path(td))
        for field in m._sha._complete._OPERATION_FIELDS:
            self.assertFalse(prepared.cost.complete[field])

    def test_11_aggregate_rejects_incomplete_required_capture(self):
        costs = []
        for _ in range(6):
            cost = m.Cost()
            cost.mark_view(b"abc")
            m._sha._complete._set_operation_measurement_complete(cost, True)
            costs.append(cost)
        costs[2].complete["C_capture_bytes"] = False
        with self.assertRaises(m.ConformanceError):
            m.aggregate(costs)


if __name__ == "__main__":
    unittest.main()
