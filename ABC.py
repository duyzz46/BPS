# Sample data for illustration purposes
maintenance_data = [
    {"machine_id": 1, "maintenance_date": "2023-01-01", "maintenance_type": "preventive", "downtime_hours": 2},
    {"machine_id": 2, "maintenance_date": "2023-01-03", "maintenance_type": "corrective", "downtime_hours": 4},
    # Add more data as needed
]

sensor_data = [
    {"machine_id": 1, "temperature": 75, "vibration": 0.02, "pressure": 30},
    {"machine_id": 2, "temperature": 80, "vibration": 0.03, "pressure": 35},
    # Add more data as needed
]

# Data Cleaning and Preprocessing
def clean_maintenance_data(maintenance_data):
    # Remove rows with missing values (if applicable)
    cleaned_data = [record for record in maintenance_data if all(record.values())]
    return cleaned_data

def clean_sensor_data(sensor_data):
    # Impute missing values (if applicable)
    for record in sensor_data:
        for key, value in record.items():
            if value == '':
                record[key] = None  # Replace empty string with None (missing value)
    return sensor_data

def merge_data(maintenance_data, sensor_data):
    merged_data = []
    for maintenance_record in maintenance_data:
        for sensor_record in sensor_data:
            if maintenance_record["machine_id"] == sensor_record["machine_id"]:
                merged_record = {
                    "machine_id": maintenance_record["machine_id"],
                    "maintenance_date": maintenance_record["maintenance_date"],
                    "maintenance_type": maintenance_record["maintenance_type"],
                    "downtime_hours": maintenance_record["downtime_hours"],
                    "temperature": sensor_record["temperature"],
                    "vibration": sensor_record["vibration"],
                    "pressure": sensor_record["pressure"]
                }
                merged_data.append(merged_record)
    return merged_data

# Clean and preprocess maintenance data
cleaned_maintenance_data = clean_maintenance_data(maintenance_data)

# Clean and preprocess sensor data
cleaned_sensor_data = clean_sensor_data(sensor_data)

# Merge cleaned data
merged_data = merge_data(cleaned_maintenance_data, cleaned_sensor_data)

# Print the merged data for verification
for record in merged_data:
    print(record)