import pandas as pd
import numpy as np
import streamlit as st

def melt_func(df):
    # Melt the dataframe df5 to combine year columns into a single column
    melted_df = pd.melt(
        df,
        id_vars=["State/UT"],  # Column to keep 
        value_vars=["2015 - CR", "2016 - CR", "2017 - CR", "2018 - CR", "2019 - CR", "2020 - CR"],  # Columns to melt
        var_name="Year",  # Name for the new column for years
        value_name="Total Cases"  # Name for the values column
    )

    # Clean the 'Year' column to extract only the year as an integer
    melted_df["Year"] = melted_df["Year"].str.extract(r"(\d{4})").astype(int)
    #rename the column for our convenience
    melted_df.rename(columns={'State/UT':'State'},inplace=True)

    return melted_df


#multiselect function
def multiselect(title,options_list):
    selected = st.sidebar.multiselect(title,options_list)
    select_all = st.sidebar.checkbox('Select all', value = True, key = title)
    if select_all:
        selected_options = options_list
    else:
        selected_options = selected
    return selected_options


#Statewise rape case distribution
def statewise_rape_case(df):
    statewise_case = df[['State','Total Cases']].groupby('State').sum().reset_index().sort_values('Total Cases',ascending=False)
    total_cases = statewise_case['Total Cases'].sum()
    percentage = [100,90,80,70,60,50,40,30,20,10]
    state_count = []
    for i in percentage:
        mark = 0.01*i*total_cases
        loop = 1
        while loop <= len(statewise_case) and statewise_case.iloc[:loop,1].sum() <= mark:
            loop += 1
        state_count.append(loop)
    states = pd.DataFrame(data = {'percentage cases': percentage,'state_count':state_count})
    return states