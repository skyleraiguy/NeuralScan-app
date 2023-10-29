from NeuralScan.DataProcessing import load_from_csv, filter_noise, normalize_data, remove_outliers, apply_fourier_transform
from NeuralScan.NeuralNetwork import create_model, train_model, evaluate_model

# Step 1: Load Data
# Replace 'path/to/data.csv' and 'path/to/labels.csv' with the actual paths to your MEG data and labels
meg_data = load_from_csv('path/to/data.csv')
labels = load_from_csv('path/to/labels.csv')

# Step 2: Data Preprocessing
meg_data = filter_noise(meg_data)
meg_data = remove_outliers(meg_data)
meg_data = normalize_data(meg_data)
meg_data = apply_fourier_transform(meg_data)

# Step 3: Split Data into Training and Testing Sets
# This is a simplified example, you should use proper cross-validation in a real-world application
train_size = int(0.8 * len(meg_data))
x_train, x_test = meg_data[:train_size], meg_data[train_size:]
y_train, y_test = labels[:train_size], labels[train_size:]

# Step 4: Create Model
input_shape = (x_train.shape[1],)  # Assuming x_train is a 2D array
model = create_model(input_shape)

# Step 5: Train Model
train_model(model, x_train, y_train, epochs=10)

# Step 6: Evaluate Model
results = evaluate_model(model, x_test, y_test)
print("Evaluation Results:", results)
