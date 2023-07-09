import pandas as pd
import matplotlib.pyplot as plt
import pyforest
from repository_utils import auto_import

df = pd.read_csv("Cleaned singapore electricity usage and demand.csv")

df.set_index("DateTime", inplace=True)

df["USEP (Milligrams of gold/MWh)"] = df["USEP (Milligrams of gold/MWh)"].rolling(window=7, min_periods=1).mean()

print(df)

df.plot.line()
plt.show()

auto_import(pyforest.active_imports(), __file__)
