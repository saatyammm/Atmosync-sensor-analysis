import pandas as pd
import matplotlib.pyplot as plt

# Read sensor data
df = pd.read_csv("data/sensor_readings.csv")

# Create graphs
plt.figure(figsize=(12, 6))

plt.plot(df["temperature"], label="Temperature")
plt.plot(df["humidity"], label="Humidity")
plt.plot(df["vibration"], label="Vibration")

plt.title("AtmoSync Sensor Data Analysis")
plt.xlabel("Sensor Reading")
plt.ylabel("Sensor Values")

plt.legend()
plt.grid()

plt.show()