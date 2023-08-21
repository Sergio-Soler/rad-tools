from argparse import ArgumentParser
import os
from termcolor import colored
import sys

ROOT_DIR = "."


def main(name: str):
    if name == "None":
        sys.tracebacklimit = 0
        raise ValueError(
            "".join(
                [
                    colored("\nName is undefined\n", "red"),
                    "For the make command use the syntax:\n\n",
                    "    make new-script NAME=name\n",
                ]
            )
        )
    name_py = name.replace("-", "_")
    # Check if the script already exists
    if os.path.isfile(os.path.join(ROOT_DIR, "radtools", "score", f"{name_py}.py")):
        sys.tracebacklimit = 0
        raise FileExistsError(
            "".join(
                [
                    colored("\nScript implementation file already exists\n", "red"),
                    "If you want to rewrite it, delete it manually\n",
                ]
            )
        )
    if os.path.isfile(os.path.join(ROOT_DIR, "scripts", f"rad-{name}.py")):
        sys.tracebacklimit = 0
        raise FileExistsError(
            "".join(
                [
                    colored("\nScript file already exists\n", "red"),
                    "If you want to rewrite it, delete it manually\n",
                ]
            )
        )
    if os.path.isfile(
        os.path.join(
            ROOT_DIR, "docs", "source", "user-guide", "scripts", f"rad-{name}.rst"
        )
    ):
        sys.tracebacklimit = 0
        raise FileExistsError(
            "".join(
                [
                    colored("\nDocumentation file already exists\n", "red"),
                    "If you want to rewrite it, delete it manually\n",
                ]
            )
        )

    # Script interface
    with open(os.path.join(ROOT_DIR, "scripts", f"rad-{name}.py"), "w") as file:
        file.write(
            "#! /usr/local/bin/python3\n"
            + "\n"
            + "from radtools._osfix import _winwait\n"
            + f"from radtools.score.{name_py} import create_parser, manager\n"
            + "\n"
            + 'if __name__ == "__main__":\n'
            + "    parser = create_parser()\n"
            + "    args = parser.parse_args()\n"
            + "    manager(**vars(args))\n"
            + "    _winwait()\n"
        )

    # Script implementation
    with open(
        os.path.join(ROOT_DIR, "radtools", "score", f"{name_py}.py"), "w"
    ) as file:
        file.write(
            "from argparse import ArgumentParser\n"
            + "\n"
            + "# This function is called by the script\n"
            + "def manager(input_filename):\n"
            + "    pass\n"
            + "\n"
            + "# Arguments of the parser have to be the same as arguments of the manager()\n"
            + '# You can use "-" here, but substitute it with "_" in manager()\n'
            + "def create_parser():\n"
            + "    parser = ArgumentParser()\n"
            + "    parser.add_argument(\n"
            + '        "-if",\n'
            + '        "--input-filename",\n'
            + '        metavar="filename",\n'
            + "        type=str,\n"
            + "        required=True,\n"
            + '        help="Help message"\n'
            + "    )\n"
            + "    return parser\n"
        )

    # Docs
    with open(
        os.path.join(
            ROOT_DIR, "docs", "source", "user-guide", "scripts", f"rad-{name}.rst"
        ),
        "w",
    ) as file:
        N = len(f"rad-{name}.py")
        file.write(
            f".. _rad-{name}:\n"
            + "\n"
            + "*" * N
            + "\n"
            + f"rad-{name}.py"
            + "\n"
            + "*" * N
            + "\n"
            "\n"
            f".. _rad-{name}_arguments:\n"
            "\n"
            "Arguments\n"
            "=========\n"
            "\n"
            f".. _rad-{name}_input-filename:\n"
            "\n"
            "-if, --input-filename\n"
            "---------------------\n"
            "Help message\n"
            "\n"
            ".. code-block:: text\n"
            "\n"
            "    required\n"
            "    type : str\n"
        )


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-n",
        "--name",
        type=str,
        required=True,
        help='Name of the script with no "rad-" prefix',
    )
    args = parser.parse_args()
    main(args.name)
