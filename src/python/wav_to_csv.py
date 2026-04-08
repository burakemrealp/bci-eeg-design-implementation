import numpy as np
import pandas as pd
import scipy.io.wavfile as wav
import argparse
import os

def wav_to_csv(input_path, output_path):
    """
    Convert a Spike Recorder .wav EEG file into a CSV file.
    
    The CSV file will contain:
        - Time (seconds)
        - Voltage (raw amplitude values)
    """

    # Read WAV file
    fs, data = wav.read(input_path)

    # If stereo, convert to mono
    if len(data.shape) > 1:
        data = data[:, 0]

    # Create time vector
    duration = len(data) / fs
    time = np.linspace(0, duration, len(data))

    # Create DataFrame
    df = pd.DataFrame({
        "Time": time,
        "Voltage": data
    })

    # Save CSV
    df.to_csv(output_path, index=False)
    print(f"Saved CSV file to: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert EEG .wav file to .csv")
    parser.add_argument("--input", required=True, help="Path to input .wav file")
    parser.add_argument("--output", required=True, help="Path to output .csv file")
    args = parser.parse_args()

    # Ensure output directory exists
    os.makedirs(os.path.dirname(args.output), exist_ok=True)

    wav_to_csv(args.input, args.output)
