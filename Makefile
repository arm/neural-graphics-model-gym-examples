# SPDX-FileCopyrightText: Copyright 2025 Arm Limited and/or its affiliates <open-source-office@arm.com>
# SPDX-License-Identifier: Apache-2.0

.PHONY: setup download-resources test lint format bandit copyright blocklint nb-lint nb-format

list: # List all available tasks
	@echo "Listing all available tasks"
	@grep '^[^#[:space:]].*:' Makefile | grep -v '.PHONY'


setup: # run setup script for tutorials
	@echo "Running the setup script"
	./setup.sh

download-resources: # download resources needed to run tutorials
	@echo "Downloading pretrained weights and datasets"
	python ./download_resources.py

test: # run notebook tutorial tests
	@echo "Running notebook tutorial tests"
	python -m unittest discover -s tests/ -p 'test_*.py'


lint: blocklint nb-lint # Run blocklint non-inclusive language checks and linting of all Python files recursively
	@echo "Running linting of all files"
	@find . -type f -name '*.py' -print0 | xargs -0 -r pylint --msg-template="pylint ERROR {path}:{line}:{column}: {msg_id}: {msg} ({symbol})"

format: nb-format # Format files
	@echo "Formatting files with black, isort and autoflake, including notebooks"
	autoflake .
	isort .
	black .

bandit: # Run security check
	@echo "Running security checks"
	python -m bandit -c pyproject.toml -r .

copyright: # Check that copyright headers exist for all required files
	@echo "Running copyright header check on all files"
	reuse lint

blocklint: # Run blocklint non-inclusive language checks
	@echo "Running blocklint to ensure no non-inclusive language"
	blocklint --skip-files=.blocklint,pyproject.toml

nb-lint: # Run pylint on notebooks
	@echo "Running linting of notebooks"
	nbqa pylint tutorials/

nb-format: # Run formatting of notebooks
	@echo "Formatting notebooks with black, isort and autoflake"
	nbqa autoflake tutorials/
	nbqa isort tutorials/
	nbqa black tutorials/
