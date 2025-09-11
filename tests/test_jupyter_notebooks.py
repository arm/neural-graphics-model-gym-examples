# SPDX-FileCopyrightText: <text>Copyright 2025 Arm Limited and/or
# its affiliates <open-source-office@arm.com></text>
# SPDX-License-Identifier: Apache-2.0

import logging
import shutil
import subprocess
import unittest
from pathlib import Path
from unittest import TestCase

logging.basicConfig(level=logging.INFO)


class JupyterNotebookTests(TestCase):
    """Test class for jupyter notebooks"""

    _created_venv = False
    _venv_path = Path("nb-env")

    @classmethod
    def setUpClass(cls):  # pylint: disable=invalid-name
        """Run set up script for running notebooks."""
        notebook_setup = Path("tests/setup_notebook_env.sh")

        if not cls._venv_path.exists():
            cls._created_venv = True

        result = subprocess.run([notebook_setup.absolute()], check=False)
        assert result.returncode == 0, "Failed to set up notebook environment"

    @classmethod
    def tearDownClass(cls):  # pylint: disable=invalid-name
        """Remove the virtual env if it was created by the test."""
        if cls._created_venv and cls._venv_path.exists():
            shutil.rmtree(cls._venv_path)

    def test_notebooks(self):
        """Test function that generates a sub-test for each notebook"""
        script_path = Path("tests/run_jupyter_notebook.sh")
        notebooks_folder = Path("tutorials")

        # Run each notebook as a subtest
        for notebook in notebooks_folder.rglob("*.ipynb"):
            if ".ipynb_checkpoints" in notebook.parts:
                continue
            logging.info("Running the notebook %s", notebook.name)

            with self.subTest(notebook=notebook.name):
                completed_process = subprocess.run(
                    [script_path.absolute(), notebook.absolute()], check=False
                )
                self.assertEqual(completed_process.returncode, 0)


if __name__ == "__main__":
    unittest.main()
