# -*- coding: utf-8 -*-
"""Detailed_rape_cases.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UqGLiapp9GbmJ3hlkz49ECdx5FzSvjQf

Import Necessary Libraries:
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore') #supresses the warnings displayed by the code editor.

#load the dataset into a dataframe
detailed_cases = pd.read_csv('/content/Detailed Cases (Registered) sexual Assault 2001-2008.csv')

#display max rows and max columns
pd.set_option('display.max_rows',50,'display.max_columns',28)

#displaying the first fives of the dataframe
detailed_cases.head()

#checking the shape of the data
detailed_cases.shape #the dataset have 424 rows and 27 columns

#getting the basic information of the dataset
detailed_cases.info()

#getting the summary of the Numerical columns
detailed_cases.describe()

#checking for missing values in the dataset
detailed_cases.isnull().sum() #majority of the column having missing values and it is very less(<1%) compared to total data

#Handling Missing values
#we are going to drop those rows with missing values since it's less than 1% of the missing data
detailed_cases = detailed_cases.dropna() #dropping rows with null values
detailed_cases.shape #checking the shape after dropping the rows containing missing values now the dataset have 421 rows and 27 columns

#checking for duplicates in the dataset
detailed_cases.duplicated().sum() #there is no duplicate in the dataset

#Lets look the dataframe
detailed_cases

#we can see that 'Incest (Rape) - No. of Cases Reported' and 'Incest (Rape) No. of Victims - Total Victims' are representing the same values and its repeating for other rape cases and total rape cases so we can drop those columns
detailed_cases.drop(columns=['Incest (Rape) - No. of Cases Reported','Other (Rape) - No. of Cases Reported','Rape Cases (Total) - No. of Cases Reported'],inplace=True)

detailed_cases # three repeating columns are dropped from the dataframe.

detailed_cases['Incest (Rape) No. of Victims - Total Victims'].unique()

