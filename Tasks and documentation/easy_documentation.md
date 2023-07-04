# Warning
---  
```diff
- In no way is this piece of documentation accurate or reliable, use it at your own risk  
```
# Install all libraries used
Try `cd ..` in the terminal if it doesn't work, and then rerun the code below.
```shell
pip install -r requirements.txt
```

# For after 26/6/23
```shell
```

pip install matplotlib
# Pandas
## Import the library
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

## Working with missing values
Leave the missing values there first, I need to read through the documentation to be sure what to do.
If you are brave, you can read the [documentation](https://pandas.pydata.org/docs/user_guide/missing_data.html).

## Do math with column
```python
df[name] * number
```

## Changing to DateTime Format
You may want to change dates to [DateTime format](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html) so it is easier to work with.  
```python
iter = ['2022-01-01', '2022-01-02']
pd.to_datetime(iter)
```
## Time delta
[TimeDelta](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html?highlight=timedelta#pandas.Timedelta) is a format that represents a set amount of time.
DateTime values can be added to TimeDelta values to advance the DateTime.
```python
dt = pd.to_datetime("03:03:2020")
dt += pd.TimeDelta(minutes=30)
```    
It can also be used to add time to a df.  
`df["DateTime"] += pd.TimeDelta(30, unit="minutes")`  
For details, please read the [documentation](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html?highlight=timedelta#pandas.Timedelta) by pandas.

## Date range
[Date Range](https://pandas.pydata.org/docs/reference/api/pandas.date_range.html) is a format that has a range of dates. This can be useful to get rid of values that are out of the studied date range.   
Use `df = df[df['Date'].isin(date_range)]`. [Details on the `isin()` method.](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isin.html?highlight=isin#pandas.DataFrame.isin)

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

## Merging 2 DataFrames
The [documentation](https://pandas.pydata.org/docs/user_guide/merging.html#automatic-alignment) is really straightforward, take a look at it.

## Saving a Dataframe
```python
df.to_csv("__name__")
```
# Plotting
## Import the library
```python
import matplotlib.pyplot as plt
```


# How to plot a graph
The function `df.plot()` is `df.plot(*args, **kwargs)`

A parameter that you will pass in is x and y.
This will label your axes  
`df.plot(x="Name of col that you want to be the x axis", y="Name of col that you want to be the y axis")`

## Pandas plot documentation
I strongly recommend you look at the [Pandas plot documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html) as well, it will give you a very good understanding of what is going on.

## Adding titles
`df.plot(tittle:str)`

## There are different kinds of plots
>‘line’ : line plot (default)
>
>‘bar’ : vertical bar plot
>
>‘barh’ : horizontal bar plot
>
>‘hist’ : histogram
>
>‘box’ : boxplot
>
>‘kde’ : Kernel Density Estimation plot
>
>‘density’ : same as ‘kde’
>
>‘area’ : area plot
>
>‘pie’ : pie plot
>
>‘scatter’ : scatter plot (DataFrame only)
>
>‘hexbin’ : hexbin plot (DataFrame only)

## Plotting different kinds of graphs
`df.plot(kind:str)`

`kind` is a parameter in df.plot, and you can input a string from above into it. The default input is a line plot.









