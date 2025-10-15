<!---
SPDX-FileCopyrightText: Copyright 2025 Arm Limited and/or its affiliates <open-source-office@arm.com>
SPDX-License-Identifier: Apache-2.0
--->

# Neural Graphics Model Gym Examples

## Table of contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Setup](#setup)
4. [Running the tutorials](#running-the-tutorials)
5. [Testing](#testing)
6. [Code contributions](#code-contributions)
6. [License](#license)
7. [Trademarks and copyrights](#trademarks-and-copyrights)

## Introduction
This repository contains Jupyter® notebook tutorials demonstrating how to use the [Neural Graphics Model Gym](https://github.com/arm/neural-graphics-model-gym) Python® package.

These examples walk through key workflows such as training, fine-tuning, quantization-aware training, exporting, and evaluation using the **Neural Super Sampling (NSS)** PyTorch model.

### Included tutorials:

#### 1. [Training](./tutorials/nss/model_training_example.ipynb)
This notebook shows how to train the Neural Super Sampling model from scratch.

#### 2. [Quantization-aware training and exporting](./tutorials/nss/model_qat_example.ipynb)
This notebook shows how to perform quantization-aware training (QAT) and export the Neural Super Sampling model to a `VGF` file.

#### 3. [Evaluation](./tutorials/nss/model_evaluation_example.ipynb)
This notebook shows how to run evaluation of a trained Neural Super Sampling model on a sample dataset.

#### 4. [Fine-tuning](./tutorials/nss/model_finetuning_example.ipynb)
This notebook shows how to run fine-tuning of the Neural Super Sampling model using pretrained model weights.

#### 5. [Adding a custom model](./tutorials/nss/custom_model_example.ipynb)
This notebook shows how to add your own custom model to use within the Neural Graphics Model Gym.

## Prerequisites
To run these tutorials, the following are required:

* Ubuntu® >= 22.04
  * Neural Graphics Model Gym has been tested on 22.04 LTS and 24.04 LTS, but should work on other Linux® distributions
* 3.10 <= Python < 3.13
* Python development package (e.g. `python3-dev`)
* Python3.X-venv apt package
* NVIDIA® CUDA® capable GPU
* CUDA Toolkit v12.8 or later
* Git LFS

### Windows Environment
For a Windows machine, we support running these examples using [WSL 2](https://learn.microsoft.com/en-us/windows/wsl/about).
Ensure you have installed a supported Linux environment and that you execute the notebooks from the WSL 2 environment. Installation instructions can be found [here](https://learn.microsoft.com/en-us/windows/wsl/install).

Running the tutorials with other environments may be possible but are not currently supported.

## Setup

A setup script is provided which:
- creates a Python virtual environment
- installs the `ng-model-gym` package and required dependencies
- downloads the required datasets and pretrained weights needed to run the tutorials

The setup script can be run with:
```bash
./setup.sh
```

## Running the tutorials

### Running from the console
Before running the tutorials, make sure the virtual environment created during [setup](./README.md#setup) is activated with:

```bash
source nb-env/bin/activate
```

To launch the notebooks from the console, first start the Jupyter notebook server:

```bash
jupyter notebook
```

A URL like `http://127.0.0.1:8888/tree?token=...` will be output to the terminal. If a new browser window isn't automatically opened, copy and paste this link into your browser to open the notebook interface.

In the Jupyter interface, navigate to the `tutorials/` directory and open a notebook e.g. `model_training_example.ipynb`.

Set the Python interpreter of the notebook to the virtual environment (`nb-env`) in `Kernel > Change Kernel`.

To run all cells of the notebook, navigate to `Run > Run All Cells`. Alternatively individual cells can be run by clicking on the cell and pressing `Shift + Enter`.

### Running from VSCode

Navigate to the `tutorials/nss/` directory and open a notebook e.g. `model_training_example.ipynb`.

Click **Select Kernel** upper-right corner of the notebook, then choose the one inside `nb-env`.

If you don't see it as an option, first activate the virtual environment from the console and register the kernel with:

```bash
source nb-env/bin/activate

python -m ipykernel install --user --name=nb-env --display-name "Python (nb-env)"
```

You may need to reload your window (F1 -> 'Developer: Reload Window') in order to detect the new environment.

## Testing

Tests for the tutorial notebooks can be run with:
```bash
make test
```

Make can be installed with:
```bash
sudo apt install make
```

## Code contributions
Before making a pull request for any code changes, you must run the following checks:

```bash
make test       # Run all tests
make format     # Format files (black, isort, autoflake)
make lint       # Lints files (blocklint, pylint)
make bandit     # Run security check
make copyright  # Check copyright headers exist for all required files
```

### pre-commit module

pre-commit is used to run the checks mentioned above when making a new commit.

pre-commit, and any other code checking dependencies, will be installed when running:

```bash
pip install -r requirements-dev.txt
```

To install the pre-commit git hook, run the following command

```bash
pre-commit install
```

To check that all the pre-commit checks run successfully, run the following command

```bash
pre-commit run --all-files
```

## License

Neural Graphics Model Gym Examples is licensed under [Apache License 2.0](./LICENSE.md).

## Trademarks and copyrights

* Linux® is the registered trademark of Linus Torvalds in the U.S. and elsewhere.
* Python® is a registered trademark of the PSF.
* Ubuntu® is a registered trademark of Canonical.
* “Jupyter” and the Jupyter logos are trademarks or registered trademarks of LF Charities.
* NVIDIA and the NVIDIA logo are trademarks and/or registered trademarks of NVIDIA Corporation in the U.S. and other countries.