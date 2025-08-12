#!/bin/bash

# SPDX-FileCopyrightText: <text>Copyright 2025 Arm Limited and/or
# its affiliates <open-source-office@arm.com></text>
# SPDX-License-Identifier: Apache-2.0

set -e

# Create virtual environment and install dependencies
if [ ! -d "nb-env" ]; then
    echo "* Creating virtual environment [nb-env]"
    python -m venv nb-env
else
    echo "* Reusing existing virtual environment [nb-env]"
fi

source nb-env/bin/activate

echo "* Upgrading pip and installing requirements"
pip install --upgrade pip
pip install -r requirements.txt

# Make required runtime directories
echo "* Creating required runtime directories"
mkdir -p ./tutorials/nss/output/vgf
mkdir -p ./tutorials/nss/checkpoints/qat_checkpoints
mkdir -p ./tutorials/nss/tensorboard-logs

# Download datasets and pretrained weights from HuggingFace
echo "* Downloading datasets and pretrained weights"
python ./download_resources.py

echo "* Setup finished!"
echo "To activate the virtual environment run:"
echo "  source nb-env/bin/activate"
echo "To run the notebooks, follow the 'Running the tutorials' section of the README.md"