"""Portable local runner following the official ARC-AGI-3 Kaggle starter."""
from __future__ import annotations
import argparse, importlib.util, logging, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
VENDOR=ROOT/'vendor'/'ARC-AGI-3-Agents'
if not VENDOR.exists(): raise SystemExit(f'Framework not found at {VENDOR}. Run `make setup`.')
sys.path.insert(0,str(VENDOR))
import arc_agi
from arc_agi import OperationMode

def load_agent():
    spec=importlib.util.spec_from_file_location('user_agent_module',ROOT/'agent'/'my_agent.py')
    if spec is None or spec.loader is None: raise SystemExit('could not load agent')
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod.MyAgent

def main():
    p=argparse.ArgumentParser(); p.add_argument('--game'); p.add_argument('--max-steps',type=int,default=220); p.add_argument('--list',action='store_true'); a=p.parse_args()
    logging.basicConfig(level=logging.INFO,format='%(message)s')
    arc=arc_agi.Arcade(operation_mode=OperationMode.NORMAL)
    envs=arc.get_environments()
    if a.list:
        for e in envs: print(e.game_id); return
    ids=[e.game_id.split('-')[0] for e in envs]
    if a.game:
        want={x.strip().split('-')[0] for x in a.game.split(',')}; ids=[x for x in ids if x in want]
    C=load_agent(); C.MAX_ACTIONS=min(C.MAX_ACTIONS,a.max_steps)
    for gid in ids:
        env=arc.make(gid); agent=C(card_id='local-dev',game_id=gid,agent_name=f'MyAgent.local.{gid}',ROOT_URL='http://localhost',record=False,arc_env=env,tags=['local-dev']); agent.main(); f=agent.frames[-1]; print(gid,f.levels_completed,agent.action_counter,f.state)
    print('Aggregate scorecard score:',arc.get_scorecard().score)
if __name__=='__main__': main()
