# -*- coding: utf-8 -*-
"""Summary of cases (rape) 2015-2020.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11ZMZX0nTzBSyK8MHDdZzNZee1SZ9pJD3

Import Necessary Libraries:
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore') #suppresses the warnings displayed by the code editor.

#load the dataset into the dataframe
Rape_df = pd.read_csv('/content/Summary of cases (rape) 2015-2020.csv')

#display max rows and max columns
pd.set_option('display.max_rows',50,'display.max_columns',28)

#display the first five rows of the dataframe
Rape_df.head()

#checking the shape of the dataframe
Rape_df.shape #the dataset have 36 rows and 8 columns

#getting the basic information of the dataset
Rape_df.info()

#getting the summary of the Numerical columns
Summary_stats = Rape_df.describe()
Summary_stats

#drop the unnecessary column from the dataframe which is not required for analysis
Rape_df = Rape_df.drop('Sl. No.',axis=1)
Rape_df

# Rename columns for easier access (remove spaces and hyphens)
Rape_df.columns = ['State_UT', '2015_CR', '2016_CR', '2017_CR', '2018_CR', '2019_CR', '2020_CR']

#checking for null values in the dataframe
Rape_df.isnull().sum() #there is no null value

#checking for duplicate entries in the dataframe
Num_duplicates = Rape_df.duplicated().sum()
Num_duplicates #there is no duplicate entry in the dataframe





