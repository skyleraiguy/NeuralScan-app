# results_interpreter.py

def interpret_results(model_output):
    """
    Interpret the output from the neural network model.
    
    Parameters:
    - model_output: np.array
        The output from the neural network.
        
    Returns:
    - str
        The interpreted results.
    """
    if model_output >= 0.5:
        return "The MEG signals suggest a potential neurological disorder."
    else:
        return "The MEG signals appear to be normal."
