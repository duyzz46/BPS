import pandas as pd

# Read maintenance data from Excel file
maintenance_data = pd.read_excel('maintenance_data.xlsx')

# Read sensor data from Excel file
sensor_data = pd.read_excel('sensor_data.xlsx')

# Data Cleaning and Preprocessing
def clean_maintenance_data(maintenance_data):
    # Remove rows with missing values (if applicable)
    cleaned_data = maintenance_data.dropna()
    return cleaned_data

def clean_sensor_data(sensor_data):
    # Impute missing values (if applicable)
    cleaned_data = sensor_data.fillna(value=None)  # Replace NaN values with None
    return cleaned_data

def merge_data(maintenance_data, sensor_data):
    # Merge maintenance and sensor data based on machine_id
    merged_data = pd.merge(maintenance_data, sensor_data, on='machine_id')
    return merged_data

# Clean and preprocess maintenance data
cleaned_maintenance_data = clean_maintenance_data(maintenance_data)

# Clean and preprocess sensor data
cleaned_sensor_data = clean_sensor_data(sensor_data)

# Merge cleaned data
merged_data = merge_data(cleaned_maintenance_data, cleaned_sensor_data)

# Print the merged data for verification
print(merged_data)