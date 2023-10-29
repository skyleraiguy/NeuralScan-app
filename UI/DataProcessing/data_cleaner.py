# data_cleaner.py
import numpy as np

def remove_outliers(meg_data, threshold=1.5):
    """
    Remove outlier values that are `threshold` standard deviations away from the mean.
    """
    mean = np.mean(meg_data)
    std = np.std(meg_data)
    filtered_data = [x for x in meg_data if (mean - threshold * std < x < mean + threshold * std)]
    return np.array(filtered_data)
