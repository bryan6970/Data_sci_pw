import datetime
import pyforest
import matplotlib.pyplot as plt
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

def plot_df(df, figsize=(8, 6), plot_type="line", together=False):
    """
    Plot DataFrame columns against the index.

    Parameters:
        df (pandas.DataFrame): The DataFrame containing the data to be plotted.
        figsize (tuple, optional): Figure size in inches (width, height). Default is (8, 6).
        plot_type (str, optional): Type of plot. Can be "line", "bar", "scatter", or "area". Default is "line".
        together (bool, optional): If True, plots all columns on the same plot. If False, each column has a separate plot. Default is False.

    Returns:
        None
    """
    if together:
        fig, ax = plt.subplots(figsize=figsize)
        for column in df.columns:
            if plot_type == "line":
                ax.plot(df.index, df[column].astype(str), label=column)
            elif plot_type == "bar":
                ax.bar(df.index, df[column].astype(str), label=column)
            elif plot_type == "scatter":
                ax.scatter(df.index, df[column].astype(str), label=column)
            elif plot_type == "area":
                ax.fill_between(df.index, df[column].astype(str), alpha=0.5, label=column)

        ax.set_xlabel('Index')
        ax.set_ylabel('Value')
        ax.legend()
        plt.show()
    else:
        for column in df.columns:
            fig, ax = plt.subplots(figsize=figsize)
            if plot_type == "line":
                ax.plot(df.index, df[column].astype(str))
            elif plot_type == "bar":
                ax.bar(df.index, df[column].astype(str))
            elif plot_type == "scatter":
                ax.scatter(df.index, df[column].astype(str))
            elif plot_type == "area":
                ax.fill_between(df.index, df[column].astype(str), alpha=0.5)

            ax.set_xlabel('Index')
            ax.set_ylabel('Value')
            ax.set_title(column)
            plt.show()
    fig, ax = plt.subplots(figsize=figsize)

def get_repo_root():
    return os.path.dirname(os.path.abspath(__file__))


def log(text, file=False):
    print(f"DEBUG {datetime.datetime.now().strftime('%H:%M:%S')}: {text}", file=sys.stderr)

    if file is not False:
        print(f"logging to {file}")
        with open(file, "w") as f:
            f.write(datetime.datetime.now().strftime('%H:%M:%S') + "\n")  # Write the current timestamp
            f.write(text)  # Write the text
