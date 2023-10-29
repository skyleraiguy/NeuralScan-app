import tensorflow as tf
import numpy as np

def create_model(input_shape):
    """
    Create a deep neural network model using TensorFlow.
    
    Parameters:
    - input_shape: tuple
        The shape of the input data.
        
    Returns:
    - tf.keras.Model
        The compiled model.
    """
    model = tf.keras.Sequential([
        tf.keras.layers.InputLayer(input_shape=input_shape),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')  # Binary classification
    ])
    
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    
    return model

def train_model(model, x_train, y_train, epochs=10):
    """
    Train the neural network model.
    
    Parameters:
    - model: tf.keras.Model
        The neural network model.
    - x_train: np.array
        The training data.
    - y_train: np.array
        The training labels.
    - epochs: int
        The number of epochs for training.
        
    Returns:
    - History
        The training history.
    """
    history = model.fit(x_train, y_train, epochs=epochs)
    return history

def evaluate_model(model, x_test, y_test):
    """
    Evaluate the neural network model.
    
    Parameters:
    - model: tf.keras.Model
        The neural network model.
    - x_test: np.array
        The testing data.
    - y_test: np.array
        The testing labels.
        
    Returns:
    - dict
        The evaluation results.
    """
    results = model.evaluate(x_test, y_test)
    return dict(zip(model.metrics_names, results))
