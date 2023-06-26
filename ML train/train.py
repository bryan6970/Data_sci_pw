"""
Place where the model will be trained
Using task scheduler in microsoft to train
"""

import tensorflow as tf
import numpy as np
import pandas as pd

from tensorflow.keras.layers import LSTM, Dense, Input, concatenate
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam

from collections import namedtuple


# Train the model with your data
x_train_1 = ...  # Your data for the first LSTM model
x_train_2 = ...  # Your data for the second LSTM model

x_train_data = []
y_train = ...  # Your target data


LSTM_Models = {}

# Define input shape (Time steps, Features)
Model_input_shapes = [(10, 1)]

# Create LSTM models
for i, input_shape in enumerate(Model_input_shapes):
    input_1 = Input(shape=input_shape)
    lstm_1 = LSTM(64)(input_1)
    LSTM_Models[f"LSTM_Model_{i}"] = Model(inputs=input_1, outputs=lstm_1)


# Combine LSTM models
combined = concatenate([model.output for model in LSTM_Models.values()])
dense = Dense(1)(combined)
Final_model = Model(inputs=[model.input for model in LSTM_Models.values()], outputs=dense)

# Compile the model with an optimizer, loss function, and metric(s)
optimizer = Adam(learning_rate=0.001)
Final_model.compile(optimizer=optimizer, loss='mean_squared_error', metrics=['mae'])

"""
Place where the model will be trained
"""

import tensorflow as tf
import numpy as np
import pandas as pd

from tensorflow.keras.layers import LSTM, Dense, Input, concatenate
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam

from collections import namedtuple

# Train the model with your data
x_train_1 = ...  # Your data for the first LSTM model
x_train_2 = ...  # Your data for the second LSTM model

x_train_data = []
y_train = ...  # Your target data


LSTM_Models = {}

# Define input shape (Time steps, Features)
Model_input_shapes = [(10, 1)]

# Create LSTM models
for i, input_shape in enumerate(Model_input_shapes):
    input_1 = Input(shape=input_shape)
    lstm_1 = LSTM(64)(input_1)
    LSTM_Models[f"LSTM_Model_{i}"] = Model(inputs=input_1, outputs=lstm_1)


# Combine LSTM models
combined = concatenate([model.output for model in LSTM_Models.values()])
dense = Dense(1)(combined)
Final_model = Model(inputs=[model.input for model in LSTM_Models.values()], outputs=dense)

# Compile the model with an optimizer, loss function, and metric(s)
optimizer = Adam(learning_rate=0.001)
Final_model.compile(optimizer=optimizer, loss='mean_squared_error', metrics=['mae'])


# Or just load an old model
# Final_model = load_model('my_model.h5')


Final_model.fit([x_train for x_train in x_train_data], y_train, epochs=10, batch_size=32)

# Save the trained model
Final_model.save('my_model.h5')



# Or just load an old model
# Final_model = load_model('my_model.h5')


Final_model.fit([x_train for x_train in x_train_data], y_train, epochs=10, batch_size=32)

# Save the trained model
Final_model.save('my_model.h5')


