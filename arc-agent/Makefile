PYTHON ?= python3.12
VENV := .venv
PIP := $(VENV)/bin/pip
PY := $(VENV)/bin/python
KAGGLE := KAGGLE_API_TOKEN=$$(cat .kaggle/access_token) $(VENV)/bin/kaggle
FRAMEWORK := vendor/ARC-AGI-3-Agents
GAME ?=
STEPS ?= 220
.PHONY: setup play-local notebook submit status clean
setup:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install "arc-agi>=0.9.8" "kaggle>=2.2" python-dotenv pandas pyarrow numpy
	mkdir -p vendor
	@if [ ! -d $(FRAMEWORK)/.git ]; then git clone --depth 1 https://github.com/arcprize/ARC-AGI-3-Agents.git $(FRAMEWORK); else git -C $(FRAMEWORK) pull --ff-only; fi
	$(PY) scripts/slim_framework.py
play-local:
	$(PY) scripts/play_local.py $(if $(GAME),--game $(GAME)) --max-steps $(STEPS)
notebook:
	$(PY) scripts/build_notebook.py
submit: notebook
	@test -s .kaggle/access_token || (echo 'missing .kaggle/access_token' && exit 1)
	@! grep -q REPLACE_WITH_YOUR_USERNAME notebooks/kernel-metadata.json || (echo 'replace Kaggle username in notebooks/kernel-metadata.json' && exit 1)
	$(KAGGLE) kernels push -p notebooks/
status:
	@KERNEL_ID=$$($(PY) -c "import json;print(json.load(open('notebooks/kernel-metadata.json'))['id'])"); $(KAGGLE) kernels status $$KERNEL_ID
clean:
	rm -rf $(VENV) vendor environment_files recordings
