import pyforest
import pandas as pd


df = pd.read_csv(
    "SGD_EUR Historical Data.csv")

df["DateTime"] = pd.to_datetime(df['Date'])

df = df[["DateTime", "SGD to EUR"]]

df.set_index(keys="DateTime", inplace=True)

df["SGD to EUR"].interpolate(method="time", inplace=True)

df.to_csv("SGD_EUR Historical Data.csv")

