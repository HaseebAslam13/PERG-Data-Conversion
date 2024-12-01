# PERG-Data-Conversion

# 📊 PERG Dataset Analysis

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Pandas](https://img.shields.io/badge/Pandas-✔️-orange) ![SciPy](https://img.shields.io/badge/SciPy-✔️-green) ![Matplotlib](https://img.shields.io/badge/Matplotlib-✔️-yellow)

🧠 **PERG Dataset Analysis** is a Python project designed to process and analyze Pattern Electroretinography (PERG) signals. It includes functionalities for filtering noisy signals and extracting meaningful features for both the right and left eye.

---

## 🌟 Features
✨ Load and process PERG signal datasets.  
✨ Apply low-pass filters for noise reduction.  
✨ Extract statistical features (mean, standard deviation, peak-to-peak amplitude).  
✨ Visualize original vs. filtered signals for both eyes.


<img src="https://github.com/user-attachments/assets/0962cc92-2800-4dce-9788-64d00184fa25" width = "400" height = "200"/>

---

## 🛠️ Workflow Overview

### 1️⃣ Load Dataset
- The dataset is loaded from a CSV file using **Pandas**.
- Example dataset includes signals for **right eye (RE)** and **left eye (LE)**.

### 2️⃣ Signal Filtering
- A **low-pass Butterworth filter** removes high-frequency noise.
- Adjustable parameters:
  - **Cutoff frequency:** Default is 30 Hz.
  - **Sampling frequency (fs):** Default is 1700 Hz.

### 3️⃣ Feature Extraction
- Extract time-domain features for filtered signals:
  - **Mean**
  - **Standard Deviation**
  - **Peak-to-Peak Amplitude**

### 4️⃣ Visualization
- Plot the original and filtered signals for the right and left eye using **Matplotlib**.

---

### Reference
- Fernández, I., Cuadrado-Asensio, R., Larriba, Y. et al. A comprehensive dataset of pattern electroretinograms for ocular electrophysiology research. Sci Data 11, 1013 (2024). https://doi.org/10.1038/s41597-024-03857-1



## 🚀 How to Run the Project

### Prerequisites
- Python 3.x installed.
- Required libraries:
  ```bash
  pip install pandas scipy matplotlib
- Dataset linked in the reference
