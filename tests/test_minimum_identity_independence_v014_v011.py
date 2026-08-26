import ast
import hashlib
import inspect
import json
import tempfile
import unittest
from pathlib import Path

from tools.minimum_identity_independence_v014_v011 import *

A = b"mii-conformance:v1\ncondition=ALPHA\npayload=A"
B = b"mii-conformance:v1\ncondition=ALPHA\npayload=B"


def c(**kw):
    data = dict(
        semantic_case_id="SEM_ONLY",
        frozen_bytes=A,
        materialized_bytes=A,
        executed_bytes=A,
        declared_object_id="ALPHA",
        convenience_identity_match=True,
        custody_override=None,
    )
    data.update(kw)
    return Case(**data)


class T(unittest.TestCase):
    def test_schema_hashes(self):
        verify_schemas()

    def test_alias_resolution(self):
        oracle = {
            "version": ORACLE_VERSION,
            "objects": {
                "R": {"bytes": A.decode(), "sha256": hashlib.sha256(A).hexdigest()},
                "SECRET": {"bytes": B.decode(), "sha256": hashlib.sha256(B).hexdigest()},
            },
            "critical_clean_controls": [],
            "critical_failures": [{
                "id": "E", "frozen": "R", "materialized": "R", "executed": "SECRET",
                "declared_condition": "ALPHA", "convenience_identity_match": True,
            }],
            "diagnostic_cases": [],
        }
        case = resolve_case(oracle, "E")
        self.assertEqual(case.executed_bytes, B)
        with tempfile.TemporaryDirectory() as td:
            self.assertNotIn(b"SECRET", prepare("chi_3", case, Path(td)).view_bytes)

    def test_forbidden_extra(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = prepare("chi_0", c(), Path(td))
            view = json.loads(prepared.view_bytes)
            view["oracle_mismatch"] = True
            with self.assertRaises(ConformanceError):
                validate("chi_0", view)

    def test_handles(self):
        with tempfile.TemporaryDirectory() as a, tempfile.TemporaryDirectory() as b:
            x = prepare("chi_0", c(), Path(a)).attestation["case_handle"]
            y = prepare("chi_0", c(), Path(b)).attestation["case_handle"]
            self.assertRegex(x, r"^[0-9a-f]{64}$")
            self.assertNotEqual(x, y)

    def test_architecture_api_is_view_only(self):
        for fn in (chi_0, chi_1, chi_2, chi_3):
            self.assertEqual(list(inspect.signature(fn).parameters), ["view_bytes"])
        self.assertEqual(list(inspect.signature(evaluate).parameters), ["chi", "view_bytes"])

    def test_hidden_instrumentation_state_cannot_change_behavior(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = prepare("chi_3", c(), Path(td))
            view = prepared.view_bytes
            hidden_a = Cost(C_view_bytes=1, C_sha256_ops=2, C_persist_bytes=7)
            hidden_b = Cost(C_view_bytes=999, C_sha256_ops=123, C_persist_bytes=4567)
            hidden_a.complete["C_view_bytes"] = True
            hidden_b.complete["C_view_bytes"] = True
            r1 = evaluate("chi_3", view)
            r2 = evaluate("chi_3", view)
            self.assertNotEqual(hidden_a.vector(), hidden_b.vector())
            self.assertEqual(r1, r2)

    def test_stateless(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = prepare("chi_3", c(), Path(td))
            self.assertEqual(evaluate("chi_3", prepared.view_bytes), evaluate("chi_3", prepared.view_bytes))

    def test_architecture_purity(self):
        forbidden = ("open", "socket", "subprocess", "environ", "getenv", "chdir", "time", "secrets", "Path")
        for fn in (chi_0, chi_1, chi_2, chi_3):
            tree = ast.parse(inspect.getsource(fn))
            text = ast.dump(tree)
            for token in forbidden:
                self.assertNotIn(token, text)

    def test_chi1_unresolved(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = prepare("chi_1", c(), Path(td))
            self.assertEqual(evaluate("chi_1", prepared.view_bytes).terminal, "IDENTITY_UNRESOLVED")

    def test_chi2_chi3_authority_split(self):
        fake = hashlib.sha256(A).hexdigest()
        case = c(executed_bytes=B, custody_override=fake)
        with tempfile.TemporaryDirectory() as a, tempfile.TemporaryDirectory() as b:
            p2 = prepare("chi_2", case, Path(a))
            p3 = prepare("chi_3", case, Path(b))
            self.assertEqual(evaluate("chi_2", p2.view_bytes).terminal, "IDENTITY_PASS")
            self.assertEqual(evaluate("chi_3", p3.view_bytes).terminal, "IDENTITY_MISMATCH")

    def test_lifecycle_and_post_freeze_merge(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = prepare("chi_3", c(), Path(td))
            pre = prepared.cost.vector()
            self.assertEqual(tuple(prepared.life.events), Life.ORDER[:3])
            frozen = run("chi_3", prepared)
            self.assertEqual(prepared.life.events[-1], Life.ORDER[3])
            post = prepared.cost.vector()
            self.assertGreater(post[3], pre[3])
            self.assertGreater(post[4], pre[4])
            self.assertGreater(post[5], pre[5])
            self.assertEqual(score(prepared, frozen, False), 1)
            self.assertEqual(prepared.life.events[-1], Life.ORDER[4])

    def test_referee_early_reject(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = prepare("chi_0", c(), Path(td))
            frozen = Frozen("IDENTITY_PASS", b"{}", hashlib.sha256(b"{}").hexdigest())
            with self.assertRaises(ConformanceError):
                score(prepared, frozen, False)

    def test_persist_cumulative(self):
        with tempfile.TemporaryDirectory() as td:
            cost = Cost()
            store = Store(Path(td), cost)
            store.write("x", b"abcde")
            store.write("x", b"xy")
            store.truncate("x", 1)
            self.assertEqual(store.retained(), 1)
            store.delete("x")
            self.assertEqual(store.retained(), 0)
            self.assertEqual(cost.C_persist_bytes, 7)

    def test_view_bytes(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = prepare("chi_0", c(), Path(td))
            self.assertEqual(prepared.cost.C_view_bytes, len(prepared.view_bytes))

    def test_missing_not_zero(self):
        self.assertFalse(Cost().is_complete())

    def test_aggregate(self):
        costs = []
        for _ in range(6):
            cost = Cost()
            cost.mark_view(b"abc")
            costs.append(cost)
        self.assertEqual(aggregate(costs), (18, 0, 0, 0, 0, 0))
        costs[0].complete["C_persist_bytes"] = False
        with self.assertRaises(ConformanceError):
            aggregate(costs)

    def test_pareto(self):
        vectors = {
            "a": (1, 1, 1, 1, 1, 1),
            "b": (2, 2, 2, 2, 2, 2),
            "c": (0, 3, 1, 1, 1, 1),
        }
        self.assertTrue(dominates(vectors["a"], vectors["b"]))
        self.assertEqual(pareto(vectors), {"a", "c"})


if __name__ == "__main__":
    unittest.main()
