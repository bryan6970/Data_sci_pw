# Clean holidays dataset

import pandas as pd

# Get limitations
with open(r"limitations.txt", "r") as f:
    limitations = f.readlines()[-1].split(',')
    start_date, end_date = [pd.to_datetime(date) for date in limitations]

    # Special date cos this fucker doesn't wanna work
    end_date = pd.to_datetime('2020-01-01')

# Load dataset
holiday_df = pd.read_csv(r"/Datasets/Uncleaned_datasets/singapore residential datasets/short term/holiday.csv")

# Rename Date col to DateTime
holiday_df = holiday_df.rename(columns={"Date": "DateTime"})

print(holiday_df)

# Change format to datetime
holiday_df['DateTime'] = pd.to_datetime(holiday_df["DateTime"])

# Only get dates within limitations
holiday_df = holiday_df[(holiday_df['DateTime'] >= start_date) & (holiday_df['DateTime'] <= end_date)]

# Get unique holidays
unique_holidays = holiday_df['Holiday'].unique()

# Create a dictionary of unique numbers for each holiday
holiday_dict = {}
for i, holiday in enumerate(unique_holidays, start = 1):
    holiday_dict[holiday] = i

# Map the dictionary to the holiday column of the DataFrame
holiday_df['Holiday'] = holiday_df['Holiday'].map(holiday_dict)

# Set 'Date' column as index

holiday_df = holiday_df.set_index('DateTime')
holiday_df.index = pd.to_datetime(holiday_df.index)
holiday_df = holiday_df.resample('1D').asfreq(-1)
# Fill missing values in Holiday column with -1
holiday_df['Holiday'] = holiday_df['Holiday'].fillna(-1)

# Make each day a num
holiday_df = holiday_df.reset_index()

day_map = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}

# add a new column to the dataframe and map the days of the week to numerical labels
holiday_df['Day'] = holiday_df['DateTime'].dt.day_name()


# # Clean the day and holidays to a number
holiday_df['Day'] = holiday_df['Day'].map(day_map)

print(holiday_df)


### Make into half-hourly dataset ###
holiday_df = holiday_df.set_index("DateTime")
holiday_df = holiday_df.resample('30T').ffill()


print(holiday_df)


# Make DateTime not the index
holiday_df = holiday_df.reset_index()

input(holiday_df)

# Write to csv
holiday_df.to_csv(r"C:\Users\wong2\PycharmProjects\Data_sci_pw\Datasets\Cleaned_datasets\holiday.csv", index = False)

