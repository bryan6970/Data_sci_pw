import pyforest
import pandas as pd
import os
from repository_utils import get_repo_root, log

api_token = os.environ.get('OPEN_AI_API_TOKEN')

print(api_token)


# llm = OpenAI(api_token=api_token)
# pandas_ai = PandasAI(llm, conversational=False)


def load_csv_files(folder_path):
    data = {}
    for folder in os.listdir(folder_path):
        folder_path_full = os.path.join(folder_path, folder)
        if os.path.isdir(folder_path_full):
            for filename in os.listdir(folder_path_full):
                if filename.endswith(".csv"):
                    file_path = os.path.join(folder_path_full, filename)
                    df = pd.read_csv(file_path)
                    data[filename[-8:-4]] = df
    return data


GOLD_PRICE_df = pd.read_csv(
    os.path.join(get_repo_root(), "Datasets/Ruiwen/Gold prices/1979-2021 gold prices datetime changed.csv"))

GOLD_PRICE_df["DateTime"] = pd.to_datetime(GOLD_PRICE_df["DateTime"])

GOLD_PRICE_df = GOLD_PRICE_df.reset_index(drop=True)

# Call the function to load the CSV files into a dictionary
datasets = load_csv_files(r"Datasets/Raw")

df = pd.concat(datasets.values())

print(df)

df["TCL(MW)"].fillna(df["TCL (MW)"], inplace=True)

df["DATE"].dropna(inplace=True)
df["DATE"] = pd.to_datetime(df["DATE"], format="mixed")
df["DATE"] = df.apply(lambda row: row["DATE"] + pd.Timedelta(minutes=row["PERIOD"] * 30), axis=1)

df.drop(["TCL (MW)", "LCP ($/MWh)", "INFORMATION TYPE", "PERIOD"], axis=1, inplace=True)

# Map SGD to EUR
# day_to_value = dict(zip(GOLD_PRICE_df["DateTime"].dt.day, GOLD_PRICE_df["Europe(EUR)"]))
# df["USEP ($/MWh)"] /= df["DATE"].dt.day.map(day_to_value)

# Map the $ to the day
day_to_value = dict(zip(GOLD_PRICE_df["DateTime"].dt.day, GOLD_PRICE_df["Europe(EUR)"]))
df["USEP ($/MWh)"] /= df["DATE"].dt.day.map(day_to_value)

df.rename(columns={"USEP ($/MWh)":"USEP (Gram of gold/MWh)"})

df.fillna(0)


print(df)

# df.to_csv("Cleaned singapore electricity usage and demand")