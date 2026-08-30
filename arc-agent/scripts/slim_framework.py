from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
INIT=ROOT/'vendor'/'ARC-AGI-3-Agents'/'agents'/'__init__.py'
SLIM='''from typing import Type\nfrom dotenv import load_dotenv\nfrom .agent import Agent, Playback\nfrom .swarm import Swarm\nfrom .templates.random_agent import Random\nload_dotenv()\nAVAILABLE_AGENTS: dict[str, Type[Agent]] = {"random": Random}\n'''
if __name__=='__main__':
    if not INIT.exists(): raise SystemExit(f'framework not found: {INIT}')
    INIT.write_text(SLIM,encoding='utf-8'); print(f'slimmed {INIT}')
