# Example file


import pandas as pd


# Get limitations
with open(r"../limitations.txt", "r") as f:
    limitations = f.readlines()[-1].split(',')
    start_date, end_date = [pd.to_datetime(date) for date in limitations]


# Merge amk, tuas, and changi datasets

# load dfs
df_locationA = pd.read_csv(r"Datasets\Uncleaned_datasets\angmokio.csv")

df_locationB= pd.read_csv(r"/Datasets/Uncleaned_datasets/singapore residential datasets/short term/changi.csv")

df_locationC= pd.read_csv(r"Datasets\Uncleaned_datasets\tuassouth.csv")

# Merge dfs
merged_df = pd.concat([df_locationA, df_locationB, df_locationC])

# Ground the dfs and mean the vals like temp
weather_df = merged_df.groupby(['Year', 'Month', 'Day']).mean(numeric_only=True).reset_index()

# Convert weather datetime df into pd datetime
weather_df['DateTime'] = pd.to_datetime(weather_df[['Year', 'Month', 'Day']].astype(str).apply('-'.join, 1) + ' ' + '00:00:00')


weather_df = weather_df.drop(['Year', 'Month', 'Day'], axis=1)

# Make the Datetime col the first col
weather_df.insert(0, 'DateTime', weather_df.pop('DateTime'))

# Drop unnamed col
weather_df = weather_df.drop("Unnamed: 0", axis=1)

# Remove dates out of allowed range
weather_df = weather_df[(weather_df['DateTime'] >= pd.to_datetime(start_date)) & (weather_df['DateTime'] <= pd.to_datetime(end_date))]

# Make time into half hourly time seperation
# Set 'Date' column as index
weather_df = weather_df.set_index('DateTime')

# Resample to half-hourly frequency and fill with the previous day's value
weather_df = weather_df.resample('30T').ffill()

weather_df = weather_df.reset_index()

input(f"Press enter to confirm \n\n\n{weather_df}\n\n\nPress enter to confirm" )

# Write to csv
weather_df.to_csv(r"Datasets\Cleaned_datasets\weather.csv", index=False)
