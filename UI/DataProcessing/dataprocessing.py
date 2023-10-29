import numpy as np
import scipy.signal as signal

def filter_noise(meg_data):
    """
    Filter out noise from the MEG data using a Butterworth filter.
    
    Parameters:
    - meg_data: np.array
        The raw MEG data.
        
    Returns:
    - np.array
        The filtered MEG data.
    """
    b, a = signal.butter(4, 0.5, 'low')
    filtered_data = signal.filtfilt(b, a, meg_data)
    return filtered_data

def normalize_data(meg_data):
    """
    Normalize the MEG data to have zero mean and unit variance.
    
    Parameters:
    - meg_data: np.array
        The raw or filtered MEG data.
        
    Returns:
    - np.array
        The normalized MEG data.
    """
    mean = np.mean(meg_data)
    std = np.std(meg_data)
    normalized_data = (meg_data - mean) / std
    return normalized_data
