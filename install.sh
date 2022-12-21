#!/bin/bash
python3 -m pip install -qq openai
mkdir -p $HOME/.openai
curl -sL https://raw.githubusercontent.com/dchassin/gridlabd-advisor/main/advisor.py -o $(gridlabd --version=install)/share/gridlabd/advisor.py && echo "Done. Use 'gridlabd advisor help' for more information." || echo "ERROR: install failed" > /dev/stderr
