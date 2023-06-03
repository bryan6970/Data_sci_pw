import pandas as pd

d1 = ["2023-05-30", 2, 3, 4, 2]
d2 = ["2023-06-30", 53, 1, 14, 2]
d3 = ["2023-07-30", 221, 32, 421, 2213]

df = pd.DataFrame([d1, d2, d3])

print(df.columns)

df[0] = pd.to_datetime(df[0])

print(df[0])

df.set_index(0, inplace=True)

print(df)

df = df.resample("30T").mean()

print("\n\n")
print(df)
