import sys

import pyforest
import pandas as pd
import os
from repository_utils import get_repo_root

df = pd.read_csv("stats.csv")

ElectricityDemand_df = pd.read_csv("../Electricity price and demand/Cleaned singapore electricity usage and demand.csv")
ElectricityDemand_df["DateTime"] = pd.to_datetime(ElectricityDemand_df["DateTime"], format="%Y-%m-%d %H:%M:%S")

ElectricityDemand_df.set_index("DateTime", inplace=True)

ElectricityDemand_df = ElectricityDemand_df.resample("Y").mean()

ElectricityDemand_df.index = ElectricityDemand_df.index.shift(1, freq="D")

df.rename(columns={"Data Series": "DateTime"}, inplace=True)

df.dropna()

df.drop("Unnamed: 0", axis=1, inplace=True)

df['DateTime'] = df['DateTime'].astype(int)

df["DateTime"] = pd.to_datetime(df["DateTime"], format="%Y")

df = df.set_index("DateTime")

orginal_df = df

start_date = max(df.index.min(), ElectricityDemand_df.index.min())
end_date = min(df.index.max(), ElectricityDemand_df.index.max())

df = df[(df.index >= start_date) & (df.index <= end_date)]
ElectricityDemand_df = ElectricityDemand_df[
    (ElectricityDemand_df.index >= start_date) & (ElectricityDemand_df.index <= end_date)]

print(ElectricityDemand_df["DEMAND (MW)"])

print("Missing values in df:", df.isnull().sum())
print("Missing values in ElectricityDemand_selected_years:", ElectricityDemand_df.isnull().sum())

print(df["Total Population (Number)"])
print(ElectricityDemand_df["DEMAND (MW)"])

for col in df.columns:
    df[col] = pd.to_numeric(df[col])

correlation = df.corrwith(ElectricityDemand_df["DEMAND (MW)"])

with open("Corr coef population stats.csv", "w") as f:
    for col, corr in correlation.items():
        print(f"{col} had a corr of {corr}", file=sys.stderr)
        f.write(f"{col} had a corr of, {corr}")
        if -0.5 <= corr <= 0.5:
            df.drop(col, axis=1)
            orginal_df.drop(col, axis=1)

orginal_df.dropna(inplace=True)

orginal_df.to_csv("stats.csv")
