#!/usr/bin/env bash
pip-compile --output-file base.txt base.in
pip-compile --output-file dev.txt dev.in
