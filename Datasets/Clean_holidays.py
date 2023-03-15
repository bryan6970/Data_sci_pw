
# Clean holidays dataset

import pandas as pd

# Get limitations
with open(r"Cleaned_datasets\limitations.txt", "r") as f:
    limitations = f.readlines()[-1].split(',')
    start_date, end_date = [pd.to_datetime(date) for date in limitations]


# Load dataset
holiday_df = pd.read_csv(r"C:\Users\wong2\PycharmProjects\Data_sci_pw\Datasets\Uncleaned_datasets\holiday.csv")

# Rename Date col to DateTime
holiday_df = holiday_df.rename(columns={"Date": "DateTime"})

# Change format to datetime
holiday_df['DateTime'] = pd.to_datetime(holiday_df["DateTime"])

# Only get dates within limitations
holiday_df = holiday_df[(holiday_df['DateTime'] >= start_date) & (holiday_df['DateTime'] <= end_date)]

# Make each day a num
day_map = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}

# add a new column to the dataframe and map the days of the week to numerical labels
holiday_df['Day'] = holiday_df['Day'].map(day_map)


# Clean the day and holidays to a number

# Get unique holidays
unique_holidays = holiday_df['Holiday'].unique()

# Create a dictionary of unique numbers for each holiday
holiday_dict = {}
for i, holiday in enumerate(unique_holidays, start = 1):
    holiday_dict[holiday] = i

# Map the dictionary to the holiday column of the DataFrame
holiday_df['Holiday'] = holiday_df['Holiday'].map(holiday_dict)

# Make time into half hourly time separation
# Set 'Date' column as index
holiday_df = holiday_df.set_index('DateTime')

# Resample to half-hourly frequency and fill with the previous day's value
holiday_df = holiday_df.resample('30T').ffill()

# Make DateTime not the index
holiday_df = holiday_df.reset_index()

input(holiday_df)

# Write to csv
holiday_df.to_csv(r"C:\Users\wong2\PycharmProjects\Data_sci_pw\Datasets\Cleaned_datasets\holiday.csv", index = False)

