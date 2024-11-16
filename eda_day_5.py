# -*- coding: utf-8 -*-
"""EDA-day-4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1x1ksXlRmKRopEoekCHfDU6szrFvzCFHW
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

# Univariate Analysis of Yearly Counts
plt.figure(figsize=(10, 6))
sns.histplot(data['No. Of Cases In Which Offenders Were Known To The Victims'], bins=20, kde=True)
plt.title('Distribution of Yearly Counts')
plt

import seaborn as sns
import matplotlib.pyplot as plt

# Scatter plot to visualize the relationship between two numerical variables

sns.scatterplot(x='No. Of Cases In Which Offenders Were Known To The Victims', y='Total Cases', data=data)
plt.title('Scatter Plot of Cases with Known Offenders vs. Total Cases')
plt.show()

# Box plot to compare the distribution of a numerical variable across different categories

sns.boxplot(x='Year', y='No. Of Cases In Which Offenders Were Known To The Victims', data=data)
plt.title('Box Plot of Cases with Known Offenders by Year')
plt.xticks(rotation=45)
plt.show()

# Sum across years for each state
yearly_counts = data.groupby('State')['No. Of Cases In Which Offenders Were Known To The Victims'].sum()

# Modify the groupby operation to use the correct column name
yearly_counts = data.groupby('STATE/UT')['No. Of Cases In Which Offenders Were Known To The Victims'].sum()

#Comparative Analysis Across Years:
plt.figure(figsize=(12, 6))
sns.barplot(x=yearly_counts.index, y=yearly_counts.values)
plt.xticks(rotation=90)
plt.xlabel('State/UT')
plt.ylabel('Total Yearly Counts')
plt.title('Comparative Analysis Across Years')
plt.show()

# Calculate correlation matrix across years, excluding non-numeric columns
correlation_matrix = data.select_dtypes(include=np.number).corr()

# Select numerical columns for correlation analysis using iloc
# Assuming the first column is 'STATE/UT' and needs to be excluded
correlation = data.iloc[:, 1:].select_dtypes(include=np.number).corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap="Blues")
plt.title("Correlation Between Case Counts by Year")
plt.show()

#Insight 1: Distribution of Cases Where Offenders Were Known to Victims
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
sns.histplot(data['No. Of Cases In Which Offenders Were Known To The Victims'], bins=20, kde=True)
plt.title('Distribution of Cases Where Offenders Were Known to Victims')
plt.xlabel('Number of Cases')
plt.ylabel('Frequency')
plt.show()

#Insight 2: Relationship between Cases with Known Offenders and Total Cases
data.rename(columns={'STATE/UT': 'State_UT'}, inplace=True)
numeric_data = data.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')
data['Total Cases'] = numeric_data.sum(axis=1)

sns.scatterplot(x='No. Of Cases In Which Offenders Were Known To The Victims', y='Total Cases', data=data)
plt.title('Relationship between Cases with Known Offenders and Total Cases')
plt.xlabel('Cases with Known Offenders')
plt.ylabel('Total Cases')
plt.show()

#Insight 3: Trend of Cases with Known Offenders over Time
sns.boxplot(x='YEAR', y='No. Of Cases In Which Offenders Were Known To The Victims', data=data)
plt.title('Trend of Cases with Known Offenders over Time')
plt.xlabel('YEAR')
plt.ylabel('Number of Cases')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()

#Insight 4: State-wise Comparison of Total Yearly Counts
yearly_counts = data.groupby('State_UT')['No. Of Cases In Which Offenders Were Known To The Victims'].sum()
plt.figure(figsize=(12, 6))
sns.barplot(x=yearly_counts.index, y=yearly_counts.values)
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.title('State-wise Comparison of Total Yearly Counts')
plt.xlabel('State/UT')
plt.ylabel('Total Yearly Counts')
plt.show()

#Insight 5: Correlation between Different Case Types
correlation_matrix = data.select_dtypes(include=np.number).corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="Blues")
plt.title("Correlation Between Different Case Types")
plt.show()

#Insight 6: Yearly Trend in Top States with Highest Total Cases
# Calculate top 5 states based on total cases across all years
top_5_states = data.groupby('State_UT')['Total Cases'].sum().nlargest(5).index
top_5_states_data = data[data['State_UT'].isin(top_5_states)]
yearly_trend = top_5_states_data.groupby(['YEAR', 'State_UT'])['Total Cases'].sum().unstack()

# Plot the yearly trend
yearly_trend.plot(kind='bar', figsize=(15, 8), width=0.8)
plt.title("Yearly Trend of Cases in Top 5 States with Highest Rape Cases")
plt.xlabel("Year")
plt.ylabel("Number of Cases")
plt.legend(title="States", loc="upper left")
plt.xticks(rotation=0)
plt.show()