#!/bin/bash
curl -sL https://raw.githubusercontent.com/dchassin/gridlabd-advisor/main/advisor.py -o $(gridlabd --version=install)/share/gridlabd/advisor.py || echo "ERROR: install failed" > /dev/stderr
