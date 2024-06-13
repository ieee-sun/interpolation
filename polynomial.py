#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Name: Polynomial Interpolation
Description: A brief demo of inspecting, handling, imputating Curved Missing Data, i.e. 'NaN', with Polynomial Interpolation.

Credit / Prepared by: 
Sun CHUNG, SMIEEE 
M.Sc., HKU
License: MIT License
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample time series data with missing values
dates = pd.date_range(start='2020-01-01', end='2020-01-20')
sales = [200, np.nan, 210, np.nan, np.nan, 250, 260, np.nan, 280, 290,
         285, np.nan, 280, 270, np.nan, np.nan, 320, 325, np.nan, 330]
data = pd.DataFrame({'date': dates, 'sales': sales})

print("Original Data:")
print(data)

# Check for missing values
missing_data = data['sales'].isnull().sum()
total_data = len(data)
missing_percentage = (missing_data / total_data) * 100

print("\nMissing Values in Each Column:")
print(data.isnull().sum())
print(f"Percentage of Missing Data: {missing_percentage:.2f}%")

data['date_formatted'] = data['date'].dt.strftime('%d %b') 

# Plot the original data to observe its shape
plt.figure(figsize=(10, 5))
plt.plot(data['date_formatted'], data['sales'], label='Original Sales', marker='o')
plt.title('Original Sales Data with Missing Values')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

# Polynomial Interpolation (Order 2)
data['sales_poly'] = data['sales'].interpolate(method='polynomial', order=2)

print("\nData After Polynomial Interpolation (Order 2):")
print(data[['date', 'sales', 'sales_poly']])

# Plot the original and interpolated data
plt.figure(figsize=(10, 5))
plt.plot(data['date'], data['sales'], label='Original Sales', marker='o')
plt.plot(data['date'], data['sales_poly'], label='Polynomial Interpolation', marker='x')
plt.title('Sales Data with Polynomial Interpolation')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

# Spline Interpolation (Order 3)
data['sales_spline'] = data['sales'].interpolate(method='spline', order=3)

print("\nData After Spline Interpolation (Order 3):")
print(data[['date', 'sales', 'sales_spline']])

# Plot the original and interpolated data
plt.figure(figsize=(10, 5))
plt.plot(data['date'], data['sales'], label='Original Sales', marker='o')
plt.plot(data['date'], data['sales_spline'], label='Spline Interpolation', marker='x')
plt.title('Sales Data with Spline Interpolation')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.show()