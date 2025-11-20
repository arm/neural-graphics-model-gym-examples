# SPDX-FileCopyrightText: <text>Copyright 2026 Arm Limited and/or
# its affiliates <open-source-office@arm.com></text>
# SPDX-License-Identifier: Apache-2.0

import subprocess  # nosec B404
import sys
from pathlib import Path

# Directories to check files in
ROOT_DIRS = ["scripts", "tests", "tutorials"]

# Message format for pylint output
MSG_TEMPLATE = "pylint ERROR {path}:{line}:{column}: {msg_id}: {msg} ({symbol})"


def collect_files():
    """Get list of files to run pylint on."""
    dirs_to_check = ROOT_DIRS
    files = []

    # Recursively collect .py files from directories to check
    for d in dirs_to_check:
        path = Path(d)

        if not path.exists():
            continue

        for p in path.rglob("*.py"):
            if p.is_file():
                files.append(str(p))

    # Append top level .py files
    files.extend(str(f) for f in Path(".").glob("*.py") if f.is_file())

    return files


def run_pylint(files):
    """Run pylint command."""
    base_cmd = ["pylint", "--msg-template", MSG_TEMPLATE]

    for i in range(0, len(files), 200):
        rc = subprocess.call(base_cmd + files[i : i + 200])  # nosec B603
        if rc:
            return rc

    return 0


def main():
    """Entry point for pylint script."""
    print("Running linting of all files")

    files = collect_files()

    if not files:
        return 0

    return run_pylint(files)


if __name__ == "__main__":
    sys.exit(main())
