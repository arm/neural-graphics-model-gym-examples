#!/usr/bin/env bash

# SPDX-FileCopyrightText: <text>Copyright 2025 Arm Limited and/or
# its affiliates <open-source-office@arm.com></text>
# SPDX-License-Identifier: Apache-2.0

# Exit immediately if there is a pipeline failure
# Enable tracing so errors are displayed
set -e
set -x

# Run under a virtual environment to isolate Python packages.
# This is done as jupyter notebooks can install python packages and we don't
# want to pollute the system packages.

# Create environment if it doesn't already exist
if [ ! -d "nb-env" ]; then
	python -m venv nb-env --system-site-packages --clear
fi

source nb-env/bin/activate 2> /dev/null

# Install package so it's available in the notebook without restarting
pip install --upgrade pip setuptools wheel packaging

pip install -r ./requirements.txt

# Install the packages required for executing jupyter from the virtual environment
pip install --quiet nbconvert
