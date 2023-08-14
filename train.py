import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import matplotlib.pyplot as plt

# Load your dataset
raw_data = pd.read_csv("Final_dataset.csv", parse_dates=["DateTime"], index_col="DateTime")

# Create a date range covering the desired time period
start_date = "2018-09-01"
end_date = "2021-09-30"
freq = "30T"  # 30 minutes frequency
date_range = pd.date_range(start=start_date, end=end_date, freq=freq)

# Create a DataFrame with the date range as index
data = pd.DataFrame(index=date_range)

# Load your dataset and merge with the date range DataFrame
data = data.merge(raw_data, how="left", left_index=True, right_index=True)
data.fillna(0, inplace=True)


print(data)

# Fit Exponential Smoothing model
alpha = 0.2  # Smoothing parameter
model = ExponentialSmoothing(data['DEMAND (MW)'], seasonal=None, trend='add', dates=data.index)
model_fit = model.fit(smoothing_level=alpha)

# Make forecasts
forecast_steps = 50 # number of steps to forecast
forecast = model_fit.forecast(steps=forecast_steps)

# Plot forecasts
# plt.plot(data['DEMAND (MW)'])
plt.plot(forecast, color='red')
print(forecast)
plt.show()
