# -*- coding: utf-8 -*-
"""EDA-day-2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GKWXrfnO5qUX5wdiZvZkEx4CoD9C4rwO
"""

#loading file
from google.colab import files
uploaded = files.upload()

#importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 # Stop warnings
import warnings
warnings.filterwarnings('ignore')

#loading dataset
data = pd.read_csv('State wise Sexual Assault (Detailed) 1999 - 2013.csv')

# View the first few rows to get an overview of the data
print(data.head())

# Examine data types and check for missing values
print(data.info())

# Get summary statistics
print(data.describe())

# Get the column names
print("column names-",data.columns)

# Check the shape of the data
print(data.shape)

# Check for missing values
print(data.isnull().sum())

# Handling Missing Values (Example: Fill with mean for a specific column)
# Convert the column to numeric, handling errors
data['No. Of Cases In Which Offenders Were Known To The Victims'] = pd.to_numeric(data['No. Of Cases In Which Offenders Were Known To The Victims'], errors='coerce')
# Now fill NaN values with the mean
data['No. Of Cases In Which Offenders Were Known To The Victims'].fillna(
    data['No. Of Cases In Which Offenders Were Known To The Victims'].mean(),
    inplace=True
)