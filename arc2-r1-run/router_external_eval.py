from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

RUNNER = Path('/tmp/r1')
sys.path.insert(0, str(RUNNER))
from r1_solver import r0_b2_solver as r0
from r1_solver.r1_solver import solve_task_r1


def visible_truth(task):
    visible = {
        'train': task['train'],
        'test': [{'input': ex['input']} for ex in task['test']],
    }
    truths = [r0.to_grid(ex['output']) for ex in task['test']]
    return visible, truths


def grid_from_attempt(a):
    return r0.to_grid(a['output'])


def distinct_attempts(attempts):
    out = []
    seen = set()
    for a in attempts:
        g = grid_from_attempt(a)
        if g in seen:
            continue
        out.append(a)
        seen.add(g)
    return out


def conservative_router(r0res, r1res, ti):
    r0a = distinct_attempts(r0res['predictions'][ti]['attempts'])
    r1a = distinct_attempts(r1res['predictions'][ti]['attempts'])

    routed = []
    seen = set()

    if r0res['candidate_count'] > 0:
        for a in r0a:
            g = grid_from_attempt(a)
            if g in seen:
                continue
            routed.append({'source': 'R0', 'attempt': a})
            seen.add(g)
            if len(routed) == 2:
                break
        if len(routed) < 2:
            for a in r1a:
                g = grid_from_attempt(a)
                if g in seen:
                    continue
                routed.append({'source': 'R1', 'attempt': a})
                seen.add(g)
                if len(routed) == 2:
                    break
    else:
        for a in r1a:
            g = grid_from_attempt(a)
            if g in seen:
                continue
            routed.append({'source': 'R1', 'attempt': a})
            seen.add(g)
            if len(routed) == 2:
                break

    if not routed:
        # Existing R0 schema-safe fallback if neither route source has an admitted route.
        for a in r0res['predictions'][ti]['attempts']:
            routed.append({'source': 'R0_FALLBACK', 'attempt': a})
            if len(routed) == 2:
                break
    if len(routed) == 1:
        routed.append({'source': routed[0]['source'], 'attempt': dict(routed[0]['attempt'])})
    return routed[:2]


def correct(attempts, truth):
    return any(grid_from_attempt(a) == truth for a in attempts)


def task_files(root: Path):
    return sorted(p for p in root.glob('*.json') if p.is_file())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('corpus', type=Path)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()

    rows = []
    totals = Counter()

    for p in task_files(args.corpus):
        task = json.loads(p.read_text())
        if not isinstance(task, dict) or not task.get('train') or not task.get('test'):
            continue
        if any('output' not in ex for ex in task['test']):
            continue

        visible, truths = visible_truth(task)
        r0res = r0.solve_task(visible)
        r1res = solve_task_r1(visible, truths)

        r0oks = []
        r1oks = []
        routeroks = []
        source_by_test = []
        attempt_set_changed_vs_r1 = 0
        complementary_test = []

        for ti, truth in enumerate(truths):
            r0attempts = r0res['predictions'][ti]['attempts']
            r1attempts = r1res['predictions'][ti]['attempts']
            routed = conservative_router(r0res, r1res, ti)
            router_attempts = [x['attempt'] for x in routed]

            a0 = correct(r0attempts, truth)
            a1 = correct(r1attempts, truth)
            ar = correct(router_attempts, truth)
            r0oks.append(a0)
            r1oks.append(a1)
            routeroks.append(ar)
            source_by_test.append([x['source'] for x in routed])

            r1set = {grid_from_attempt(a) for a in r1attempts}
            rset = {grid_from_attempt(a) for a in router_attempts}
            if r1set != rset:
                attempt_set_changed_vs_r1 += 1

            correct_sources = {
                x['source'] for x in routed if grid_from_attempt(x['attempt']) == truth
            }
            complementary_test.append(sorted(correct_sources))

        r0_task = all(r0oks)
        r1_task = all(r1oks)
        router_task = all(routeroks)

        # Complementary task gain: router solves; neither source alone solves the task;
        # and correct routed outputs across the task use both source families.
        correct_route_sources = set()
        for srcs in complementary_test:
            correct_route_sources.update(s for s in srcs if s in {'R0', 'R1'})
        complementary = (
            router_task and not r0_task and not r1_task and
            correct_route_sources == {'R0', 'R1'}
        )

        r1_only_full = r1_task and not r0_task
        row = {
            'task': p.name,
            'n_test': len(truths),
            'r0_candidate_count': r0res['candidate_count'],
            'r1_representation_count': r1res['r1_representation_count'],
            'r1_candidate_count': r1res['r1_candidate_count'],
            'r0_correct_outputs': sum(r0oks),
            'r1_correct_outputs': sum(r1oks),
            'router_correct_outputs': sum(routeroks),
            'r0_task_solved': r0_task,
            'r1_task_solved': r1_task,
            'router_task_solved': router_task,
            'r0_regression_under_router': r0_task and not router_task,
            'r1_regression_under_router': r1_task and not router_task,
            'router_gain_vs_r1': router_task and not r1_task,
            'r1_only_full_solve': r1_only_full,
            'r1_only_full_solve_retained': r1_only_full and router_task,
            'complementary_gain': complementary,
            'attempt_set_differences_vs_r1': attempt_set_changed_vs_r1,
            'router_sources_by_test': source_by_test,
        }
        rows.append(row)

        vals = {
            'tasks': 1,
            'outputs': len(truths),
            'r0_tasks': int(r0_task),
            'r1_tasks': int(r1_task),
            'router_tasks': int(router_task),
            'r0_outputs': sum(r0oks),
            'r1_outputs': sum(r1oks),
            'router_outputs': sum(routeroks),
            'r0_regressions': int(r0_task and not router_task),
            'r1_regressions': int(r1_task and not router_task),
            'router_gains_vs_r1': int(router_task and not r1_task),
            'r1_only_full_solves': int(r1_only_full),
            'r1_only_full_solves_retained': int(r1_only_full and router_task),
            'complementary_gains': int(complementary),
            'attempt_set_differences_vs_r1': attempt_set_changed_vs_r1,
        }
        totals.update(vals)

    if totals['tasks'] == 0:
        raise SystemExit('No compatible Mini-ARC tasks found')

    summary = {
        'protocol': 'Fresh external Mini-ARC test: frozen R1.0 vs conservative R0+R1 routing',
        'corpus': 'KSB21ST/MINI-ARC data/MiniARC',
        'task_count': totals['tasks'],
        'output_count': totals['outputs'],
        'r0_task_solve_rate': totals['r0_tasks'] / totals['tasks'],
        'r1_task_solve_rate': totals['r1_tasks'] / totals['tasks'],
        'router_task_solve_rate': totals['router_tasks'] / totals['tasks'],
        'delta_router_vs_r1_task_rate': (totals['router_tasks'] - totals['r1_tasks']) / totals['tasks'],
        'r0_output_accuracy': totals['r0_outputs'] / totals['outputs'],
        'r1_output_accuracy': totals['r1_outputs'] / totals['outputs'],
        'router_output_accuracy': totals['router_outputs'] / totals['outputs'],
        'delta_router_vs_r1_output_accuracy': (totals['router_outputs'] - totals['r1_outputs']) / totals['outputs'],
        'r0_full_task_regressions_under_router': totals['r0_regressions'],
        'r1_full_task_regressions_under_router': totals['r1_regressions'],
        'router_new_full_tasks_vs_r1': totals['router_gains_vs_r1'],
        'r1_only_full_solves': totals['r1_only_full_solves'],
        'r1_only_full_solves_retained': totals['r1_only_full_solves_retained'],
        'complementary_full_task_gains': totals['complementary_gains'],
        'test_outputs_with_attempt_set_difference_vs_r1': totals['attempt_set_differences_vs_r1'],
        'claim_ceiling': [
            'Mini-ARC was not used in prior B0-B3/R1/ConceptARC development.',
            'The router was frozen before reading Mini-ARC task JSON contents or outputs.',
            'R0 and R1 solver hashes are unchanged; only route allocation differs.',
        ],
        'rows': rows,
    }
    args.out.write_text(json.dumps(summary, indent=2))
    print(json.dumps({k: v for k, v in summary.items() if k != 'rows'}, indent=2))


if __name__ == '__main__':
    main()
