# SPDX-FileCopyrightText: <text>Copyright 2026 Arm Limited and/or
# its affiliates <open-source-office@arm.com></text>
# SPDX-License-Identifier: Apache-2.0

import argparse
import platform
import subprocess  # nosec B404
import sys
import venv
from pathlib import Path


def run(cmd, **kwargs):
    """Run commands."""
    print("*", " ".join(map(str, cmd)))
    subprocess.run(cmd, check=True, **kwargs)  # nosec B603


def main(args) -> None:
    """Script to create development environment with Hatch."""

    venv_dir = args.venv_name

    # Create virtual environment if it doesn't already exist
    if not Path(venv_dir).exists():
        print(f"* Creating virtual environment [{venv_dir}]")
        venv.EnvBuilder(with_pip=True).create(venv_dir)
    else:
        print(f"* Reusing existing virtual environment [{venv_dir}]")

    if platform.system() == "Linux":
        venv_cmd = Path(venv_dir) / "bin"
        venv_py = venv_cmd / "python"
        venv_activate = f"source {venv_cmd / 'activate'}"

    else:
        raise OSError(
            f"Unsupported OS: {platform.system()!r} for setup. Requires Linux."
        )

    print("* Upgrading pip")
    run([venv_py, "-m", "pip", "install", "--upgrade", "pip"])

    if not args.dev:
        print("* Installing dependencies")
        run([venv_py, "-m", "pip", "install", "."])

    else:
        print("* Creating Hatch environment")
        run([venv_py, "-m", "pip", "install", "hatch==1.15.1", "click<=8.2.0"])
        run([venv_py, "-m", "hatch", "-v", "env", "create"])

    print("* Creating required runtime directories")

    for d in [
        "tutorials/output/vgf",
        "tutorials/checkpoints/qat_checkpoints",
        "tutorials/tensorboard-logs",
    ]:
        Path(d).mkdir(parents=True, exist_ok=True)

    if not args.skip_downloads:
        print("* Downloading datasets and pretrained weights")
        if not args.dev:
            download_cmd = [venv_py, "scripts/download_resources.py"]

        else:
            download_cmd = [
                venv_py,
                "-m",
                "hatch",
                "run",
                "python",
                "scripts/download_resources.py",
            ]

        with subprocess.Popen(  # nosec B603
            download_cmd,
            stdout=sys.stdout,
            stderr=subprocess.PIPE,
            text=True,
        ) as process:
            for line in process.stderr:
                sys.stderr.write(line)
                sys.stderr.flush()

            return_code = process.wait()

        if return_code:
            print(
                f"* download_resources.py failed with exit code {return_code}",
                file=sys.stderr,
            )
            return return_code

    print("* Setup finished!")
    print("To use the created environment:")
    print(f"  Activate the virtual environment by running: {venv_activate}")
    print(
        "To run the notebooks, follow the 'Running the tutorials' section of the README.md"
    )

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--venv-name",
        help="Name of the virtual environment directory",
        default="nb-env",
    )
    parser.add_argument(
        "--dev",
        help="Dev install of Hatch environment for tools such as linting and testing.",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "--skip-downloads",
        help="Skip downloading datasets and pretrained weights",
        action="store_true",
        default=False,
    )

    parsed_args = parser.parse_args()

    sys.exit(main(parser.parse_args()))
