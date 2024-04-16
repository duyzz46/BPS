import pandas as pd
import random
import os
from datetime import datetime, timedelta

# Generate maintenance data
maintenance_data = []
start_date = datetime(2023, 1, 1)
for machine_id in range(1, 11):
    for _ in range(10):  # Generate 10 maintenance records per machine
        maintenance_date = start_date + timedelta(days=random.randint(0, 365))
        maintenance_type = random.choice(["preventive", "corrective"])
        downtime_hours = random.randint(1, 8)
        maintenance_data.append({"machine_id": machine_id, "maintenance_date": maintenance_date, "maintenance_type": maintenance_type, "downtime_hours": downtime_hours})

# Convert maintenance data to DataFrame
maintenance_df = pd.DataFrame(maintenance_data)

# Generate sensor data
sensor_data = []
for machine_id in range(1, 11):
    for _ in range(10):  # Generate 10 sensor readings per machine
        temperature = random.randint(60, 90)
        vibration = round(random.uniform(0.01, 0.05), 2)
        pressure = random.randint(20, 40)
        sensor_data.append({"machine_id": machine_id, "temperature": temperature, "vibration": vibration, "pressure": pressure})

# Convert sensor data to DataFrame
sensor_df = pd.DataFrame(sensor_data)

# Get the current working directory
current_directory = os.getcwd()

# Specify the full path where you want to save the Excel files
excel_directory = os.path.join(current_directory, 'excel_files')

# Create the directory if it doesn't exist
os.makedirs(excel_directory, exist_ok=True)

try:
    # Save maintenance data to Excel file
    maintenance_df.to_excel(os.path.join(excel_directory, 'maintenance_data.xlsx'), index=False)

    # Save sensor data to Excel file
    sensor_df.to_excel(os.path.join(excel_directory, 'sensor_data.xlsx'), index=False)

    print("Sample data saved to Excel files: maintenance_data.xlsx and sensor_data.xlsx")
except Exception as e:
    print("An error occurred:", e)
