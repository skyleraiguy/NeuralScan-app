# data_transformer.py
from scipy.fftpack import fft

def apply_fourier_transform(meg_data):
    """
    Apply Fourier Transform to MEG data.
    """
    return fft(meg_data)
