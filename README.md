# Brain–Computer Interface (BCI) Design and Implementation

This repository contains the software components of a Brain–Computer Interface (BCI) system developed as a senior capstone project at Bahçeşehir University. The system acquires EEG signals using a custom analog front‑end circuit and a 3D‑printed headset, digitizes the signal using an Arduino‑based interface, visualizes and records the data through Spike Recorder, and processes the recorded signals using Python.

The repository includes both the **original analysis code used during the capstone project** and an **extended machine‑learning module** for offline EEG classification.

---

## 🧠 Project Overview

The BCI system consists of:

- **3D‑printed EEG headset**  
  Designed using Blender and Fusion 360 to fit different head sizes and provide long‑term comfort.

- **Custom analog front‑end circuit**  
  Built using:
  - AD620 instrumentation amplifier  
  - High‑pass filter (HPF)  
  - Low‑pass filter (LPF)  
  - Notch filter (50/60 Hz)  
  - Non‑inverting amplifier stage  

- **Arduino interface**  
  Configures the ATmega328P ADC and streams EEG samples to Spike Recorder.

- **Spike Recorder**  
  Used for real‑time visualization and recording of EEG signals in `.wav` format.

- **Python analysis scripts**  
  Used for:
  - Converting `.wav` recordings to `.csv`
  - Spectrogram generation
  - Alpha‑band extraction
  - Eyes‑open vs. eyes‑closed comparison
  - Offline EEG classification (SVM)

---

## 📂 Repository Structure

| Path | Description |
|------|-------------|
| `src/python/eeg_analysis_original.py` | Original capstone EEG analysis code |
| `src/python/wav_to_csv.py` | Converts Spike Recorder `.wav` to `.csv` |
| `src/python/classification/preprocess_for_svm.py` | Filtering + segmentation |
| `src/python/classification/extract_features.py` | Feature extraction (band power) |
| `src/python/classification/svm_classifier.py` | SVM training & evaluation |
| `src/arduino/eeg_spike_recorder_bridge.ino` | Arduino → Spike Recorder interface |
| `data/raw/` | Raw EEG recordings |
| `data/processed/` | Processed CSV, segments, features |
| `results/` | Plots and analysis outputs |
| `README.md` | Project documentation |



---

## ⚙️ 1. Original EEG Analysis (Capstone Code)

The file `src/python/eeg_analysis_original.py` contains the **exact analysis workflow used during the capstone project**.  
This script performs:

- Reading EEG recordings exported from Spike Recorder (`.wav`)
- Resampling and spectrogram generation
- Extracting the alpha band (7–12 Hz)
- Smoothing using a triangular filter
- Computing alpha‑power over time
- Eyes‑open vs. eyes‑closed comparison
- Statistical testing (t‑test)

This file is preserved exactly as implemented during the project.

---

## 📊 2. EEG Recording with Spike Recorder

Spike Recorder is used for:

- Real‑time visualization of EEG signals  
- Recording EEG sessions to `.wav` files  

Workflow:

1. Connect Arduino  
2. Open Spike Recorder  
3. Select the serial input  
4. Adjust scaling  
5. Record EEG sessions  
6. Save `.wav` files under `data/raw/`  

---

## 🧪 3. WAV → CSV Conversion

The original analysis pipeline uses `.wav` files exported from Spike Recorder.  
These files are converted to `.csv` for easier processing.

Example:

```bash
python src/python/eeg_analysis_original.py
```

This generates:

- Frequencies.csv
- datosyt.csv
- Spectrogram images
- Alpha‑power plots

## 4. Offline EEG Classification (SVM Module)

In addition to the original analysis pipeline, this repository includes an extended machine‑learning module for offline EEG classification using Support Vector Machines (SVM).

This module demonstrates a complete ML workflow:

### 4.1 Preprocessing
preprocess_for_svm.py performs:

- Band‑pass filtering (1–40 Hz)
- Segmentation into fixed‑length windows
- Saving segments as segments.npy

### 4.2 Feature Extraction

extract_features.py computes:

- Band‑power features for each segment
- Saves:
-- features.npy
-- labels.npy (placeholder labels)

### 4.3 SVM Classification

svm_classifier.py performs:

- Train/test split
- SVM training (RBF kernel)
- Prediction
- Evaluation:
-- Accuracy
-- Classification report
-- Confusion matrix

Run:

```bash
python src/python/classification/svm_classifier.py
```

## Future Work

- Multi‑channel EEG acquisition
- Real‑time classification
- Advanced feature extraction (PSD, wavelets, CSP)
- Integration with BCI control applications
- Deep learning models (CNN, LSTM)

## Acknowledgements

This work is based on the capstone project “Brain–Computer Interface Design and Implementation” completed at Bahçeşehir University, Faculty of Engineering and Natural Sciences, by a joint EEE–BME team.

## License
License of Bahcesehir University
