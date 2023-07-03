# This is just a document for final tweaks


import pyforest
import pandas as pd


def clean_gold_price_dataset():
    df = pd.read_csv("1979-2021 gold prices datetime changed.csv")

    df.drop(axis=1, inplace=True, labels="Unnamed: 0")

    print(df)

    df["DateTime"] = pd.to_datetime(df["DateTime"])

    df.set_index("DateTime", inplace=True)

    print(df)

    df["Europe(EUR)"].interpolate(method="time", inplace=True)

    df.to_csv("1979-2021 gold prices datetime changed.csv")

