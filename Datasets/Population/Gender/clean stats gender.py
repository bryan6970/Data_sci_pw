import pyforest
import pandas as pd
from numpy import nan as NaN
import repository_utils

df = pd.read_csv("statsgender.csv")

# Change the orientation of the df
df = df.transpose()

# Make the first row columns
df.columns = df.iloc[0]
df = df[1:]

# Make the index a DateTime index

print(df.index)

df.index = df.index.str.replace(" ", "")

df.replace("na", NaN, inplace=True)

df.index = pd.to_datetime(df.index, format="%Y", errors="coerce")
# %Y basically means only year in YYYY format, "coerce" means that any errors will just become a NaT (Not a Time) value

df.index.name = "DateTime"

repository_utils.plot_df(df, together=True)
