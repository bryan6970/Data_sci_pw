# Example


import pandas as pd

# Get limitations (file does not exist anymore)
with open(r"../limitations.txt", "r") as f:
    limitations = f.readlines()[-1].split(',')
    start_date, end_date = [pd.to_datetime(date) for date in limitations]


# Clean energy consumption dataset
energy_df = pd.read_csv(r"Uncleaned_datasets\energy_consumption.csv")

# Rename column
energy_df = energy_df.rename(columns={'ds': 'DateTime'})

# Convert ds column to datetime format
energy_df['DateTime'] = pd.to_datetime(energy_df['DateTime'])

# Only get dates within limitations
energy_df = energy_df[(energy_df['DateTime'] >= start_date) & (energy_df['DateTime'] <= end_date)]

# Rename energy col to energy
energy_df = energy_df.rename(columns={"y":"Energy"})

input(energy_df)

# Write to csv
energy_df.to_csv(r"Cleaned_datasets\energy_consumption.csv", index = False)

