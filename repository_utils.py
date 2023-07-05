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

def get_proper_cwd():
    return os.path.dirname(os.path.abspath(__file__))


def plot_df(df, plot_type="line", round_=2, save=False, together=False, figsize=(8, 6)):
    """
    Plot DataFrame columns against the index.

    Parameters:
        df (pandas.DataFrame): The DataFrame containing the data to be plotted.
        figsize (tuple, optional): Figure size in inches (width, height). Default is (8, 6).
        plot_type (str, optional): Type of plot. Can be "line", "bar", "barh", "hist", "box", "kde"/"density", "pie", or "area". Default is "line".
        together (bool, optional): If True, plots all columns on the same plot. If False, each column has a separate plot. Default is False.
        round_ (int or None, optional): Number of decimal places to round the values. Default is 2.
        save (bool, optional): If True, saves the plots as images. Default is False.

    Returns:
        None
    """

    def plot_according_to_type(plot_type_):
        if plot_type == "line":
            ax.plot(df.index, df[column].astype(str), label=column)
            return True
        elif plot_type == "bar":
            ax.bar(df.index, df[column].astype(str), label=column)
            return True
        elif plot_type == "barh":
            ax.barh(df.index, df[column].astype(str), label=column)
            return True
        elif plot_type == "hist":
            ax.hist(df[column].astype(str), label=column)
            return True
        elif plot_type == "box":
            ax.boxplot(df[column].astype(str), label=column)
            return True
        elif plot_type == "kde" or plot_type == "density":
            ax.plot(df.index, df[column].astype(str), label=column)
            ax.fill_between(df.index, df[column].astype(str), alpha=0.5, label=column)
            return True
        elif plot_type == "area":
            ax.fill_between(df.index, df[column].astype(str), alpha=0.5, label=column)
            return True
        elif plot_type == "pie":
            ax.pie(df[column].astype(str), labels=df.index, autopct="%1.1f%%")
            return False
        else:
            raise ValueError(f"{plot_type} is not available")

    set_label = False

    if round_:
        df = df.round(round_)

    if together:
        fig, ax = plt.subplots(figsize=figsize)
        for column in df.columns:
            set_label = plot_according_to_type(plot_type)

        if set_label:
            ax.set_xlabel(df.index.name)
            ax.set_ylabel("Columns")
            ax.legend()

        plt.title(f"Graph of {df.index.name} against Columns")
        plt.legend()

        if save:
            plt.savefig(f"Graph of {df.index.name} against Columns {df.columns}")

        plt.show()
    else:
        for column in df.columns:
            fig, ax = plt.subplots(figsize=figsize)
            set_label = plot_according_to_type(plot_type)

            if set_label:
                ax.set_xlabel(df.index.name)
                ax.set_ylabel(column)

            ax.set_title(f"Graph of {df.index.name} against Columns {column}")

            plt.legend()

            if save:
                plt.savefig(f"Graph of {df.index.name} against Columns {column}")

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
