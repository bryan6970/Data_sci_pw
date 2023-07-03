import pyforest
import pandas as pd
import os
from repository_utils import get_repo_root

df = pd.read_csv("stats.csv")

# File not completed yet
ElectricityDemand_df = pd.read_csv(os.path.join(get_repo_root(), "Datasets/Yu feng"))

ElectricityDemand_df.resample("Y").mean()

df.columns = df.iloc[0]
df = df[1:]

df.drop("Unnamed: 0", axis=1, inplace=True)

df.rename(columns={"Date Series": "DateTime"})

df.dropna()

df["DateTime"] = pd.to_datetime(df["DateTime"], format="mixed")

df.sort_values(by="Date", inplace=True)

correlation = df.corrwith(ElectricityDemand_df["DEMAND (MW)"])

for col, corr in correlation.items():
    if -0.5 <= corr <= 0.5:
        df.drop(col, axis=1)

print(df)

df.set_index("DateTime", inplace=True)

df.to_csv("stats.csv")
