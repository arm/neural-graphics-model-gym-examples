# SPDX-FileCopyrightText: <text>Copyright 2025-2026 Arm Limited and/or
# its affiliates <open-source-office@arm.com></text>
# SPDX-License-Identifier: Apache-2.0

import logging
import subprocess
import unittest
from pathlib import Path
from unittest import TestCase

logging.basicConfig(level=logging.INFO)


class JupyterNotebookTests(TestCase):
    """Test class for Jupyter notebooks"""

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
