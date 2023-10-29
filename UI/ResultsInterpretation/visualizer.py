# visualizer.py
import matplotlib.pyplot as plt

def plot_results(model, x_test, y_test):
    """
    Visualize the model's predictions on a test set.
    
    Parameters:
    - model: tf.keras.Model
        The trained neural network model.
    - x_test: np.array
        The testing data.
    - y_test: np.array
        The testing labels.
    """
    y_pred = model.predict(x_test)
    
    plt.scatter(range(len(y_test)), y_test, c='g', label='True Labels')
    plt.scatter(range(len(y_pred)), y_pred, c='r', label='Predicted Labels')
    plt.xlabel('Sample')
    plt.ylabel('Prediction')
    plt.legend(loc='upper right')
    plt.title('True vs Predicted Labels')
    plt.show()
