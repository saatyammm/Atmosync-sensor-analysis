import csv
from pathlib import Path

# Find the project folder
project_folder = Path(__file__).resolve().parent.parent

# Locate the CSV file
csv_file = project_folder / "data" / "sensor_readings.csv"

temperatures = []
humidities = []
vibrations = []

# Read sensor data
with open(csv_file, "r", newline="") as file:

    reader = csv.DictReader(file)

    for row in reader:
        temperatures.append(float(row["temperature"]))
        humidities.append(float(row["humidity"]))
        vibrations.append(float(row["vibration"]))

# Calculate averages
avg_temp = sum(temperatures) / len(temperatures)
avg_humidity = sum(humidities) / len(humidities)
avg_vibration = sum(vibrations) / len(vibrations)

# Display results
print("===== ATMOSYNC DATA ANALYSIS =====")

print("Total readings:", len(temperatures))

print("Average Temperature:", round(avg_temp, 2))
print("Average Humidity:", round(avg_humidity, 2))
print("Average Vibration:", round(avg_vibration, 2))

print("===== ANALYSIS COMPLETED =====")