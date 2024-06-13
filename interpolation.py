#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Name: Linear Interpolation
Description: A brief demo of inspecting, handling, imputating Missing Data, i.e. 'NaN', with Linear Interpolation.

Credit / Prepared by: 
Sun CHUNG, SMIEEE 
M.Sc., HKU
License: MIT License
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample time series data with missing values
dates = pd.date_range(start='2020-01-01', end='2020-01-10')
sales = [200, np.nan, 210, np.nan, np.nan, 250, 260, np.nan, 280, 290]
data = pd.DataFrame({'date': dates, 'sales': sales})

print("Original Data:")
data

### By Observing this example, we know it is 'sales' data with the most missing data.

# Check for missing values
missing_data = data['sales'].isnull().sum()
total_data = len(data)
missing_percentage = (missing_data / total_data) * 100

print("\nMissing Values in Each Column:")
print(data.isnull().sum())
print(f"Percentage of Missing Data: {missing_percentage:.2f}%")

# Plot the original data to observe its shape
plt.figure(figsize=(10, 5))
plt.plot(data['date'], data['sales'], label='Original Sales', marker='o')
plt.title('Original Sales Data with Missing Values')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

# Apply linear interpolation
data['sales_interpolated'] = data['sales'].interpolate(method='linear')

print("\nData After Linear Interpolation:")
print(data)

# Plot the original and interpolated data
plt.figure(figsize=(10, 5))
plt.plot(data['date'], data['sales'], label='Original Sales', marker='o')
plt.plot(data['date'], data['sales_interpolated'], label='Interpolated Sales', marker='x')
plt.title('Sales Data with Linear Interpolation')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.show()