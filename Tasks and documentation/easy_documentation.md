# Install all libraries used
Try `cd ..` in the terminal if it doesn't work, and then rerun the code below.
```shell
pip install -r requirements.txt
```

## Import the needed libraries
```python
import pyforest
import pandas
from numpy import nan as NaN
import matplotlib.pyplot as plt
```

or, use the libraries needed and add this at the end
```python
from repository_utils import auto_import
auto_import(pyforest.active_imports(), __file__)
```

## Plotting a df
```python
df.plot.__type__()
```
Replace `__type__` with the type of plot

## Showing df
```python
plt.show()
```




