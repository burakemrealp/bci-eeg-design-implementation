import numpy as np
import pandas as pd
from scipy.signal import butter, filtfilt

def bandpass_filter(signal, fs, low=1, high=40):
    """4th‑order Butterworth bandpass filter."""
    b, a = butter(4, [low/(fs/2), high/(fs/2)], btype='band')
    return filtfilt(b, a, signal)

def load_csv(path):
    """Load EEG CSV exported from your original analysis."""
    df = pd.read_csv(path)
    return df["Power"].values, df["Time"].values

def segment_signal(signal, segment_length):
    """Split signal into equal‑length segments."""
    segments = []
    for i in range(0, len(signal), segment_length):
        seg = signal[i:i+segment_length]
        if len(seg) == segment_length:
            segments.append(seg)
    return np.array(segments)

if __name__ == "__main__":
    # Example usage
    signal, time = load_csv("data/processed/datosyt.csv")
    filtered = bandpass_filter(signal, fs=500)
    segments = segment_signal(filtered, segment_length=500)

    np.save("data/processed/segments.npy", segments)
    print("Saved segments.npy with shape:", segments.shape)
