import pyforest
import pandas as pd

df = pd.read_csv("statsgender.csv")

# Change the orientation of the df
df = df.transpose()

# Make the first row columns
df.columns = df.iloc[0]
df = df[1:]

# Make the index a DateTime index

print(df.index)

# There is a better way do this for sure, but i'm not sure how sorry
df.index = [str.strip(no) for no in df.index]

df.index = pd.to_datetime(df.index, format="%Y", errors="coerce")
# %Y basically means only year in YYYY format, "coerce" means that any errors will just become a NaT (Not a Time) value

