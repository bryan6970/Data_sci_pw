import pandas as pd

# Creating a DataFrame
```python
df = pd.DataFrame([[1, 2], [1, 2]])  
df = pd.read_csv(filepath)  
```

# Getting Rows of a DataFrame
```python
row_number = 0   
row_numbers = [0, 1]  
row_name = 'row_label'  
row_names = ['row_label1', 'row_label2']  

df.iloc[row_number].values  
df.iloc[row_numbers].values   
df.loc[row_name]  
df.loc[row_names]  
```
# Getting Columns of a DataFrame
col_name = 'column_name'
df[col_name]

# Get Column Names
index = 0
df.columns[index]

# Changing Column Names
original_name = 'original_name'
final_name = 'final_name'
df.rename(columns={original_name: final_name}, inplace=True)

# Changing to DateTime Format
iter = ['2022-01-01', '2022-01-02']
pd.to_datetime(iter)

# Getting Unique Values in an Array
df.iloc[0].unique()

# Setting Column as Index
colname = 'column_name'
df.set_index(colname, inplace=True)
df.reset_index(inplace=True)

# Filling in Missing Values
fill_with_something = 0
df["test_col"].fillna(fill_with_something)

# Resampling the Timeframe
timeframe = 'D'
df.resample(timeframe).mean()

# Mapping
day_map = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}
df["day"].map(day_map)
