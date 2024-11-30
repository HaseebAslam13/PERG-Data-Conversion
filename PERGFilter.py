#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd

# Load the CSV file (adjust the file path as needed)
data = pd.read_csv(r"C:\Users\My PC\Downloads\PERG_Dataset\Data\csv\0333.csv")


# Display the first few rows to inspect the data
#data_new = data_old.head(20)
#print(data_new)


# In[31]:


# Select a subset of the data (e.g., first 100 rows for a few subjects)
subset_data = data.iloc[:20, 3:]


# In[32]:


import scipy.signal as signal

# Apply a low-pass filter (adjust cutoff frequency as needed)
def low_pass_filter(data_new, cutoff=30, fs=1700):
    # Design the filter
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = signal.butter(5, normal_cutoff, btype='low', analog=False)
    # Apply the filter
    filtered_data = signal.filtfilt(b, a, data_new)
    return filtered_data

# Apply the filter to the right and left eye signals
subset_data['filtered_RE'] = low_pass_filter(subset_data['RE_2'])  # Right eye
subset_data['filtered_LE'] = low_pass_filter(subset_data['LE_2'])  # Left eye


# In[19]:


# Extract time-domain features
def extract_features(data, column_name):
    mean_val = data[column_name].mean()
    std_val = data[column_name].std()
    max_val = data[column_name].max()
    min_val = data[column_name].min()
    peak_to_peak = max_val - min_val
    return mean_val, std_val, peak_to_peak

# Apply feature extraction for right eye
mean_RE, std_RE, peak_to_peak_RE = extract_features(subset_data, 'filtered_RE')

# Apply feature extraction for left eye
mean_LE, std_LE, peak_to_peak_LE = extract_features(subset_data, 'filtered_LE')

# Print features
print(f"Right Eye: Mean = {mean_RE}, Std = {std_RE}, Peak-to-Peak = {peak_to_peak_RE}")
print(f"Left Eye: Mean = {mean_LE}, Std = {std_LE}, Peak-to-Peak = {peak_to_peak_LE}")


# In[ ]:





# In[30]:


import matplotlib.pyplot as plt

# Plot original and filtered signals for the right eye
plt.figure(figsize=(10, 6))
plt.plot(subset_data['TIME_2'], subset_data['RE_2'], label='Original RE', alpha=0.5)
plt.plot(subset_data['TIME_2'], subset_data['filtered_RE'], label='Filtered RE', color='red')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (µV)')
plt.title('Right Eye Signal - Original vs Filtered')
plt.legend()
plt.show()

# Plot original and filtered signals for the left eye
plt.figure(figsize=(10, 6))
plt.plot(subset_data['TIME_2'], subset_data['LE_2'], label='Original LE', alpha=0.5)
plt.plot(subset_data['TIME_2'], subset_data['filtered_LE'], label='Filtered LE', color='blue')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (µV)')
plt.title('Left Eye Signal - Original vs Filtered')
plt.legend()
plt.show()


# In[ ]:




