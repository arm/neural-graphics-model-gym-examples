# SPDX-FileCopyrightText: Copyright 2025 Arm Limited and/or its affiliates <open-source-office@arm.com>
# SPDX-License-Identifier: Apache-2.0

setup: # run setup script for tutorials
	@echo "Running the setup script"
	./setup.sh
download-resources: # download resources needed to run tutorials
	@echo "Downloading pretrained weights and datasets"
	python ./download_resources.py
test: # run notebook tutorial tests
	@echo "Running notebook tutorial tests"
	python -m unittest discover -s tests/ -p 'test_*.py'
