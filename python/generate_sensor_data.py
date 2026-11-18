
import csv
import random
from datetime import datetime
from pathlib import Path

# Create sample container sensor data
container_id = "CONTAINER_A"

# Prepare the output CSV file
project_folder = Path(__file__).resolve().parent.parent
output_folder = project_folder / "data"
output_folder.mkdir(exist_ok=True)

output_file = output_folder / "sensor_readings.csv"

# Generate 20 sensor readings
with open(output_file, "w", newline="") as file:

    writer = csv.writer(file)

    # CSV column headings
    writer.writerow([
        "timestamp",
        "container_id",
        "temperature",
        "humidity",
        "vibration"
    ])

    for i in range(20):

        timestamp = datetime.now().isoformat()

        temperature = round(random.uniform(2, 12), 2)
        humidity = round(random.uniform(60, 95), 2)
        vibration = round(random.uniform(0, 5), 2)

        writer.writerow([
            timestamp,
            container_id,
            temperature,
            humidity,
            vibration
        ])

print("AtmoSync sensor data generated successfully!")
print("Total readings: 20")
print("Saved file:", output_file)