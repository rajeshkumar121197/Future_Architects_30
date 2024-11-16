import pandas as pd
import numpy as np
import streamlit as st

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
    statewise_case = df[['States/ UTs/Cities','Rape Cases (Total) No. of Victims - Total Victims']].groupby('States/ UTs/Cities').sum().reset_index().sort_values('Rape Cases (Total) No. of Victims - Total Victims',ascending=False)
    total_cases = statewise_case['Rape Cases (Total) No. of Victims - Total Victims'].sum()
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