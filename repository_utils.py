import datetime
import sys
import os
import importlib.util

import pandas as pd


def import_file_from_repository(relative_path):
    # Get the current directory (root directory of the repository)
    repository_root = os.path.dirname(os.path.abspath(__file__))

    # Construct the absolute path to the target file
    target_file_path = os.path.join(repository_root, relative_path)

    # Get the module name from the file name
    target_module_name = os.path.splitext(os.path.basename(target_file_path))[0]

    # Load the module from the file
    spec = importlib.util.spec_from_file_location(target_module_name, target_file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Return the imported module
    return module


def get_repo_root():
    return os.path.dirname(os.path.abspath(__file__))


def log(text, file=False):
    print(f"DEBUG {datetime.datetime.now().strftime('%H:%M:%S')}: {text}", file=sys.stderr)

    if file is not False:
        print(f"logging to {file}")
        with open(file, "w") as f:
            f.write(datetime.datetime.now().strftime('%H:%M:%S') + "\n")  # Write the current timestamp
            f.write(text)  # Write the text
