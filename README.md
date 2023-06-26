# Install all libraries used
```shell
pip install -r requirements.txt
```

# For after 26/6/23
```shell
pip install matplotlib
```

# Usage of Pandas
Import the library
```python
import pandas
```

## Creating a DataFrame
```python
df = pd.DataFrame([[1, 2], [1, 2]])  
df = pd.read_csv(filepath)  
```

## Getting Rows of a DataFrame
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
## Getting Columns of a DataFrame
```python
col_name = 'column_name'
df[col_name]
```

## Get Column Names
```python
index = 0
df.columns[index]
```

## Changing Column Names
```python 
original_name = 'original_name'
final_name = 'final_name'
df.rename(columns={original_name: final_name}, inplace=True)
```

## Delete column
```python
df.drop(name, inplace=True, axis=1)
```

## Delete/Replace NA values
```python
df.dropna(inplace=True)

df.fillna(method=METHOD, inplace = True) 
# ffill Fills with the previous value 
# bfill Fills with the next value 

df.fillna(str/int, inplace = True)
```
## Do math with colum
```python
df[name] * number
```

## Changing to DateTime Format
```python
iter = ['2022-01-01', '2022-01-02']
pd.to_datetime(iter)
```
## Getting Unique Values in an Array
```python 
df.iloc[0].unique()
```
## Setting Column as Index
```python 
colname = 'column_name'
df.set_index(colname, inplace=True)
df.reset_index(inplace=True)
```
## Filling in Missing Values
```python
fill_with_something = 0
df["test_col"].fillna(fill_with_something)
```
## Resampling the Timeframe
```python
timeframe = 'D'
df.resample(timeframe).mean()
```
## Mapping
```python
day_map = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}
df["day"].map(day_map)
```
## Saving a Dataframe
```python
df.to_csv("__name__")
```
