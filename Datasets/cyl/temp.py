import pandas as pd

df = pd.read_csv("stats.csv")

print(df)

# Convert the column to numeric and coerce non-numeric values to NaN
df.set_index("DateTime", inplace=True)

for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print(df)
# Drop rows with NaN values in the column
df = df.dropna()

print(df)

df.to_csv("stats.csv")