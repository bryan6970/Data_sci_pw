# This is just a document for final tweaks


import pyforest
import pandas as pd


def clean_gold_price_dataset():
    df = pd.read_csv("1979-2021 gold prices datetime changed.csv")

    df["DateTime"] = pd.to_datetime(df["DateTime"])

    df.set_index("DateTime", inplace=True)

    # Assuming the DataFrame has a DateTime index
    df.resample('D').interpolate(method='linear', inplace=True)

    df.fillna(0, inplace=True)

    print(len(df.isna()))

    df.to_csv("1979-2021 gold prices datetime changed.csv")


clean_gold_price_dataset()
