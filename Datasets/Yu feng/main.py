import warnings

import pyforest  # this will import any common modules that you missed, more of just a timesaver
import pandas as pd
import os
from repository_utils import get_repo_root

Gold_dataset = pd.read_csv(
    os.path.join(get_repo_root(), "Datasets/Ruiwen/Gold prices/1979-2021 gold prices datetime changed.csv"))

Gold_dataset["DateTime"] = pd.to_datetime(Gold_dataset["DateTime"])
PRICE_OF_GOLD_IN_2018 = Gold_dataset[Gold_dataset["DateTime"].dt.year == 2018].mean()

print(PRICE_OF_GOLD_IN_2018)

dataset_dict = {}


def load_csv_files(folder_path):
    data = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path, filename)
            df = pd.read_csv(file_path)
            data[filename] = df
    return data


# Call the function to load the CSV files into a dictionary
csv_data = load_csv_files(r"Datasets/Raw/USEP_from_01-Jan-2018_to_31-Dec-2018")

# Access the data from the dictionary using the file names as keys
for filename, df in csv_data.items():
    dataset_dict[filename[5:8]] = df

for key, df in dataset_dict.items():
    df.drop("INFORMATION TYPE", inplace=True, axis=1)

    df["DATE"] = pd.to_datetime(df["DATE"])

    df["DATE"] = df.apply(lambda row: row["DATE"] + pd.Timedelta(minutes=row["PERIOD"] * 30), axis=1)

    df.drop("PERIOD", inplace=True, axis=1)

    df["USEP ($/MWh)"] = (df["USEP ($/MWh)"] / PRICE_OF_GOLD_IN_2018)

    df.drop("LCP ($/MWh)", inplace=True, axis=1)

    df.drop("TCL (MW)", inplace=True, axis=1)

    df.rename(columns={"USEP ($/MWh)": "Grams of gold / MWh"}, inplace=True)

    df.to_csv(f"2018 {key}.csv")

if pyforest.active_imports(): warnings.warn(f"{pyforest.active_imports()} modules are not imported")
