import numpy as np

def bandpower(segment):
    """Compute average power of a segment."""
    return np.mean(segment**2)

if __name__ == "__main__":
    segments = np.load("data/processed/segments.npy")
    features = np.array([bandpower(seg) for seg in segments])

    # Placeholder labels — you can later replace with real labels
    labels = np.zeros(len(features))

    np.save("data/processed/features.npy", features)
    np.save("data/processed/labels.npy", labels)

    print("Saved features.npy and labels.npy")
