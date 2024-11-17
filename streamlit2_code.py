import numpy as np
import pandas as pd
import streamlit as st
import func2_code

#reading the dataset
df1 = pd.read_csv('summary of cases 2015-2020.csv')
#calling the custom melt function
melted_df1 = func2_code.melt_func(df1)
#sidebar
st.sidebar.title('Filters')

#Year filter
Select_year = func2_code.multiselect('Select Year',melted_df1['Year'].unique())

#State filter
Select_state = func2_code.multiselect('Select State', melted_df1['State'].unique())

#applying filter
filter_df = melted_df1[(melted_df1['Year'].isin(Select_year)) & (melted_df1['State'].isin(Select_state))]

st.image('rv_logo.webp',width = 100)

#display the title of the dashboard
st.title('Rape Violation Dashboard (2015-2020)')

#showing total cases
st.metric(label='Total Rape cases',value = int(filter_df['Total Cases'].sum()))


st.subheader('Trend analysis on different Rape cases')

#Yearly rape cases
yearly_cases = filter_df[['Year','State','Total Cases']].groupby('State').sum()

st.line_chart(yearly_cases, x_label='Year', y_label='Total cases', height=500, use_container_width=True )


#statewise cases
st.title('State count by case %')
state_count = func2_code.statewise_rape_case(filter_df)
state_count.set_index('percentage cases',inplace=True)
st.bar_chart(state_count, x_label='percentage cases', y_label='State count')


