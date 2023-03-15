"""
Place where the model will be trained
"""

import tensorflow as tf
import numpy as np
import pandas as pd


# Load data
df = pd.read_csv(r"C:\Users\wong2\PycharmProjects\Data_sci_pw\Datasets\final_dataset.csv")

# Parse dataset
print(df)

# # Remove DateTime col
# df = df.shuffle(frac=1)
# df = df.drop("DateTime", axis=1)

# Separate the Energy col
energy_data = df[["Energy"]]

normal_data = df.drop("Energy", axis=1)

print(energy_data)

print("\n\n\n\n")

print(normal_data)

# Get training and testing data
# 2225 rows allocated to testing

# Randomly select the rows to remove
test_energy_df = energy_data.sample(2225)
test_normal_df = normal_data.sample(2225)

# Remove the test rows from the original DataFrame
train_energy_df = df.drop(test_energy_df.index)
train_normal_df = df.drop(test_normal_df.index)

print('Normal df', test_normal_df)

### Choose to either Define or load existing model ###

# Define model
model = tf.keras.Sequential([
    tf.keras.layers.LSTM(64, activation='relu', return_sequences=True, input_shape= (11,50000)),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.LSTM(32, activation='relu'),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.LSTM(32, activation='relu'),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(2)
])

# # Load model
# model = load_model('.h5')

# Compile model
model.compile(optimizer='adam', loss='mse')

# Train model
model.fit(train_normal_df, train_energy_df, epochs=100, batch_size=32)

# Evaluate model
loss = model.evaluate(test_normal_df, test_energy_df)

# Make predictions
predictions = model.predict(test_normal_df)

model.save('Model')
