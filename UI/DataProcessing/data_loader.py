# data_loader.py
import numpy as np

def load_from_csv(file_path):
    """
    Load MEG data from a CSV file.
    """
    return np.genfromtxt(file_path, delimiter=',')
