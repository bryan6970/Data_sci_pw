"""
Place where the model will be trained

This is currently only a baseline code to follow
"""

import tensorflow as tf
import numpy as np
import pandas as pd

# Load data
data = pd.read_csv("data.csv")

# Preprocess data
# ...

# Define model
model = tf.keras.Sequential([
    tf.keras.layers.LSTM(64, activation='relu', return_sequences=True),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.LSTM(32, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(1)
])

# Compile model
model.compile(optimizer='adam', loss='mse')

# Train model
model.fit(params, correct answer, epochs=100, batch_size=32)

# Evaluate model
loss = model.evaluate(params, correct answer)

# Make predictions
predictions = model.predict(params)
