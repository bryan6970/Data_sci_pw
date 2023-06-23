# Clean data

import pandas as pd

# Parse code into final dataset

# Load weather df
weather_df = pd.read_csv(r"C:\Users\wong2\PycharmProjects\Data_sci_pw\Datasets\Cleaned_datasets\weather.csv")
print(weather_df)

# Load in holiday file
holiday_df = pd.read_csv(r"C:\Users\wong2\PycharmProjects\Data_sci_pw\Datasets\Cleaned_datasets\holiday.csv")
print(holiday_df)

# Load energy consumption file
energy_df = pd.read_csv(r"C:\Users\wong2\PycharmProjects\Data_sci_pw\Datasets\Cleaned_datasets\energy_consumption.csv")

print(energy_df)

# Merge the dfs
merged_df_1 = pd.merge(energy_df, weather_df, on='DateTime', how='left')
final_df = pd.merge(merged_df_1, holiday_df, on='DateTime', how='left')

final_df['DateTime'] = pd.to_datetime(final_df['DateTime'])

# Get rid of date but keep time
final_df['Time'] = final_df['DateTime'].dt.time

final_df = final_df.drop('DateTime', axis = 1)

final_df.insert(0, 'Time', final_df.pop('Time'))

# Remove all NaN vals
final_df = final_df.dropna()

input(final_df)

# Write to CSV file
final_df.to_csv(r"C:\Users\wong2\PycharmProjects\Data_sci_pw\Datasets\final_dataset.csv", index=False)

