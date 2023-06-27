import pandas as pd


df = pd.read_csv("1979-2021.csv")

df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")


df.rename(columns={"Date":"DateTime"}, inplace=True)

# List of columns to keep
columns_to_keep = ["DateTime", "Europe(EUR)"]

# Drop all columns except the ones to keep
df = df.drop(columns=df.columns.difference(columns_to_keep))


df.to_csv("1979-2021 gold prices datetime changed.csv")