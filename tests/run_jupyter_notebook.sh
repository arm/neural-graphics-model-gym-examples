#!/usr/bin/env bash

# SPDX-FileCopyrightText: <text>Copyright 2025 Arm Limited and/or
# its affiliates <open-source-office@arm.com></text>
# SPDX-License-Identifier: Apache-2.0

set -e
set -x

source nb-env/bin/activate 2>/dev/null

NOTEBOOK="$1"
NOTEBOOK_DIR="$(dirname "$NOTEBOOK")"
NOTEBOOK_FILENAME="$(basename "$NOTEBOOK")"

cd "$NOTEBOOK_DIR"

# Run the notebook and pass the output to /dev/null
# This prevents the notebook being written to the filesystem
jupyter nbconvert --to notebook --execute "$NOTEBOOK_FILENAME" --stdout > /dev/null