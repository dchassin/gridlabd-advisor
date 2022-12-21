#!/bin/bash
python3 -m pip install -q openai
mkdir -p $HOME/.openai
curl -sL https://raw.githubusercontent.com/dchassin/gridlabd-advisor/main/advisor.py -o $(gridlabd --version=install)/share/gridlabd/advisor.py || echo "ERROR: install failed" > /dev/stderr
