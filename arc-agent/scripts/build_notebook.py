from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AGENT_SRC = ROOT / 'agent' / 'my_agent.py'
NOTEBOOK_PATH = ROOT / 'notebooks' / 'submission.ipynb'

def code_cell(source: str) -> dict:
    return {'cell_type':'code','metadata':{'trusted':True},'outputs':[],'execution_count':None,'source':source}

def markdown_cell(source: str) -> dict:
    return {'cell_type':'markdown','metadata':{},'source':source}

def build() -> dict:
    agent_body=AGENT_SRC.read_text(encoding='utf-8')
    install=code_cell("!pip install --no-index --find-links \\\n    /kaggle/input/competitions/arc-prize-2026-arc-agi-3/arc_agi_3_wheels \\\n    arc-agi python-dotenv")
    write_agent=code_cell('%%writefile /tmp/my_agent.py\n'+agent_body)
    slim = "from typing import Type\nfrom dotenv import load_dotenv\nfrom .agent import Agent, Playback\nfrom .swarm import Swarm\nfrom .templates.random_agent import Random\nfrom .templates.my_agent import MyAgent\nload_dotenv()\nAVAILABLE_AGENTS: dict[str, Type[Agent]] = {'random': Random, 'myagent': MyAgent}\n"
    env = "SCHEME=http\nHOST=gateway\nPORT=8001\nARC_API_KEY=test-key-123\nARC_BASE_URL=http://gateway:8001/\nOPERATION_MODE=online\nENVIRONMENTS_DIR=\nRECORDINGS_DIR=/kaggle/working/server_recording\n"
    run_source=(
        "import os\n"
        "if os.getenv('KAGGLE_IS_COMPETITION_RERUN'):\n"
        "    !curl --fail --retry 999 --retry-all-errors --retry-delay 5 --retry-max-time 600 http://gateway:8001/api/games\n"
        "    !cp -r /kaggle/input/competitions/arc-prize-2026-arc-agi-3/ARC-AGI-3-Agents /kaggle/working/ARC-AGI-3-Agents\n"
        "    !cp /tmp/my_agent.py /kaggle/working/ARC-AGI-3-Agents/agents/templates/my_agent.py\n"
        f"    open('/kaggle/working/ARC-AGI-3-Agents/agents/__init__.py','w').write({slim!r})\n"
        f"    open('/kaggle/working/ARC-AGI-3-Agents/.env','w').write({env!r})\n"
        "    !cd /kaggle/working/ARC-AGI-3-Agents && MPLBACKEND=agg python main.py --agent myagent\n"
    )
    run=code_cell(run_source)
    dummy=code_cell(
        "import os\n"
        "if not os.getenv('KAGGLE_IS_COMPETITION_RERUN'):\n"
        "    import pandas as pd\n"
        "    submission = pd.DataFrame(data=[['1_0','1',True,1]], columns=['row_id','game_id','end_of_game','score'])\n"
        "    submission.to_parquet('/kaggle/working/submission.parquet', index=False)\n"
        "    submission.head()\n"
    )
    return {
      'metadata':{
        'kernelspec':{'language':'python','display_name':'Python 3','name':'python3'},
        'language_info':{'name':'python','mimetype':'text/x-python','file_extension':'.py','pygments_lexer':'ipython3'},
        'kaggle':{'accelerator':'none','isInternetEnabled':False,'isGpuEnabled':False,'language':'python','sourceType':'notebook'}},
      'nbformat_minor':4,'nbformat':4,
      'cells':[markdown_cell('# White Rabbit Submission-0\n\nCompetition lane. Built from `agent/my_agent.py`; frozen research artifacts are not imported.'),install,write_agent,run,dummy]
    }

def main() -> None:
    NOTEBOOK_PATH.parent.mkdir(parents=True,exist_ok=True)
    NOTEBOOK_PATH.write_text(json.dumps(build(),indent=1),encoding='utf-8')
    print(f'wrote {NOTEBOOK_PATH}')

if __name__=='__main__': main()
