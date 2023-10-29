from flask import Flask, render_template, jsonify
from NeuralScan.DataProcessing import load_from_csv
from NeuralScan.NeuralNetwork import create_model, train_model, evaluate_model
from NeuralScan.ResultsInterpretation import interpret_results, plot_results

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze_data():
    # Your logic here to get the data, run it through the neural network, etc.
    # This is just a stub.
    data = request.json['data']
    
    # Assume you have a function process_data that does everything from loading to prediction
    result = process_data(data) 
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
