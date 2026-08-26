from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest import mock

import tools.minimum_identity_independence_v014_v016 as m

A = b"mii-completeness-conformance:v1\ncondition=ALPHA\npayload=A"


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


class OperationMeasurementCompletenessConformance(unittest.TestCase):
    def test_01_prepare_leaves_operation_dimensions_pending(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_3", case(), Path(td))
        for field in m._OPERATION_FIELDS:
            self.assertFalse(prepared.cost.complete[field])
        self.assertFalse(prepared.cost.is_complete())

    def test_02_valid_zero_event_stream_is_complete_zero(self):
        cost = m.Cost()
        m._set_operation_measurement_complete(cost, False)
        delta = m._merge_operation_events_fail_closed(cost, b"")
        self.assertEqual(delta, m.ArchitectureDelta(0, 0, 0))
        for field in m._OPERATION_FIELDS:
            self.assertTrue(cost.complete[field])
        self.assertEqual(cost.C_sha256_ops, 0)
        self.assertEqual(cost.C_extract_ops, 0)
        self.assertEqual(cost.C_identity_compare_ops, 0)

    def test_03_valid_event_stream_is_complete_with_counts(self):
        cost = m.Cost()
        m._set_operation_measurement_complete(cost, False)
        stream = (
            b"IDENTITY_COMPARE_OPERATION\n"
            b"EXTRACT_OPERATION\n"
            b"SHA256_OPERATION\n"
            b"IDENTITY_COMPARE_OPERATION\n"
        )
        delta = m._merge_operation_events_fail_closed(cost, stream)
        self.assertEqual(delta, m.ArchitectureDelta(1, 1, 2))
        for field in m._OPERATION_FIELDS:
            self.assertTrue(cost.complete[field])
        self.assertEqual(cost.C_sha256_ops, 1)
        self.assertEqual(cost.C_extract_ops, 1)
        self.assertEqual(cost.C_identity_compare_ops, 2)

    def test_04_truncated_event_stream_marks_all_operation_dimensions_incomplete(self):
        cost = m.Cost()
        with self.assertRaises(m.ConformanceError):
            m._merge_operation_events_fail_closed(cost, b"SHA256_OPERATION")
        for field in m._OPERATION_FIELDS:
            self.assertFalse(cost.complete[field])

    def test_05_unknown_event_marks_all_operation_dimensions_incomplete(self):
        cost = m.Cost()
        with self.assertRaises(m.ConformanceError):
            m._merge_operation_events_fail_closed(cost, b"UNKNOWN_OPERATION\n")
        for field in m._OPERATION_FIELDS:
            self.assertFalse(cost.complete[field])

    def test_06_non_ascii_event_marks_all_operation_dimensions_incomplete(self):
        cost = m.Cost()
        with self.assertRaises(m.ConformanceError):
            m._merge_operation_events_fail_closed(cost, b"\xff\n")
        for field in m._OPERATION_FIELDS:
            self.assertFalse(cost.complete[field])

    def test_07_valid_zero_is_distinct_from_measurement_incomplete(self):
        complete_zero = m.Cost()
        m._set_operation_measurement_complete(complete_zero, False)
        m._merge_operation_events_fail_closed(complete_zero, b"")

        incomplete = m.Cost()
        m._set_operation_measurement_complete(incomplete, False)

        self.assertEqual(
            (
                complete_zero.C_sha256_ops,
                complete_zero.C_extract_ops,
                complete_zero.C_identity_compare_ops,
            ),
            (0, 0, 0),
        )
        self.assertTrue(all(complete_zero.complete[f] for f in m._OPERATION_FIELDS))
        self.assertFalse(any(incomplete.complete[f] for f in m._OPERATION_FIELDS))

    def test_08_aggregate_rejects_any_incomplete_operation_dimension(self):
        costs = []
        for _ in range(6):
            cost = m.Cost()
            cost.mark_view(b"abc")
            costs.append(cost)
        costs[3].complete["C_extract_ops"] = False
        with self.assertRaises(m.ConformanceError):
            m.aggregate(costs)

    def test_09_post_t3_decode_failure_leaves_operation_dimensions_incomplete(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_3", case(), Path(td))

        def fake_invoke(chi, view_bytes, life):
            life.mark(m.Life.ORDER[2])
            return m.ArchitectureResult(
                "IDENTITY_PASS",
                b'{"terminal":"IDENTITY_PASS"}',
                b"SHA256_OPERATION",
            )

        with mock.patch.object(m._ops, "_invoke_architecture_with_life", fake_invoke):
            with self.assertRaises(m.ConformanceError):
                m.run("chi_3", prepared)
        self.assertEqual(tuple(prepared.life.events), m.Life.ORDER[:4])
        for field in m._OPERATION_FIELDS:
            self.assertFalse(prepared.cost.complete[field])

    def test_10_pre_result_acquisition_failure_never_promotes_operation_completeness(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_3", case(), Path(td))

        def fail_invoke(chi, view_bytes, life):
            life.mark(m.Life.ORDER[2])
            raise m.ConformanceError("synthetic acquisition failure")

        with mock.patch.object(m._ops, "_invoke_architecture_with_life", fail_invoke):
            with self.assertRaises(m.ConformanceError):
                m.run("chi_3", prepared)
        self.assertEqual(tuple(prepared.life.events), m.Life.ORDER[:3])
        for field in m._OPERATION_FIELDS:
            self.assertFalse(prepared.cost.complete[field])

    def test_11_successful_run_promotes_operation_completeness(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_3", case(), Path(td))
            frozen = m.run("chi_3", prepared)
        self.assertEqual(frozen.terminal, "IDENTITY_PASS")
        for field in m._OPERATION_FIELDS:
            self.assertTrue(prepared.cost.complete[field])
        self.assertTrue(prepared.cost.is_complete())


if __name__ == "__main__":
    unittest.main()
