import pyforest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("statsgender.csv").transpose()

df.columns = df.iloc[0]

df = df.iloc[1:]

df.index = df.index.str.replace(" ", "")

df.index = pd.to_datetime(df.index, format="%Y")

df.index.name = "DateTime"

df = df[df.index > pd.to_datetime('2017')]

df = df.replace("na",np.nan )

df["Median Age At First Marriage For Females (Years)"] = pd.to_numeric(df["Median Age At First Marriage For Females (Years)"])

# df.plot(y="Median Age At First Marriage For Females (Years)", x=df.index)

plt.plot(df.index.to_pydatetime(), df["Median Age At First Marriage For Females (Years)"])

plt.show()


df = df.resample("30T").interpolate(method="ffill")


print(df)

# df.to_csv("statsgender cleaned.csv")