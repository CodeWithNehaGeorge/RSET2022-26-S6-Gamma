import os
import pandas as pd
import numpy as np
from scipy.stats import skew

# Folder where all CSV files are stored
folder_path = "/home/nia/emg_project/C/dataset"

# Initialize a dictionary to hold skewness values for each patient
skewness_data = {f"P{str(i).zfill(2)}": [] for i in range(1, 21)}

# Loop through each patient
for patient_num in range(1, 21):  # P01 to P20
    patient_id = f"P{str(patient_num).zfill(2)}"
    
    for segment_num in range(1, 51):  # 50 segments per patient
        file_name = f"{patient_id}S{str(segment_num).zfill(2)}.csv"
        file_path = os.path.join(folder_path, file_name)
        
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            signal = df.iloc[:, 1].values  # Assumes second column is EMG signal
            skew_value = skew(signal)
            skewness_data[patient_id].append(skew_value)
        else:
            print(f"Missing file: {file_name}")
            skewness_data[patient_id].append(None)

# Convert to DataFrame
columns = [f"S{str(i).zfill(2)}" for i in range(1, 51)]
skewness_df = pd.DataFrame.from_dict(skewness_data, orient='index', columns=columns)

# Save to CSV
output_file = "skewness.csv"
skewness_df.to_csv(output_file)

print(f"Skewness values saved to {output_file}")

