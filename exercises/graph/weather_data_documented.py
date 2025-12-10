"""
Purpose: Weather Data Pre-processing
------------------------------------
This script loads raw meteorological data from a CSV file and prepares
wind metrics for vector analysis. It converts pandas Series to NumPy arrays
for computational efficiency and transforms wind direction from degrees
to radians to allow for trigonometric operations (e.g., calculating
wind vectors).
"""

import pandas as pd
import numpy as np

# Load weather data
# We use read_csv to parse the file into a DataFrame structure.
# Ensure 'april2024_station_data.csv' is in the same directory as this script.
weather_df = pd.read_csv('april2024_station_data.csv')

# Extract Wind Metrics to NumPy
# Converting to NumPy arrays removes the Pandas index overhead, making
# subsequent mathematical operations significantly faster.
wind_speed = weather_df['wind_speed'].to_numpy()
wind_direction = weather_df['wind_direction'].to_numpy()

# Convert Degrees to Radians
# Meteorological data is recorded in degrees (0-360), but numpy's trigonometric
# functions (sin, cos) require input in radians.
wind_direction_rad = np.deg2rad(wind_direction)