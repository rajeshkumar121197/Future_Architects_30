import numpy as np
import pandas as pd
import streamlit as st
import func_code

#reading the dataset
df = pd.read_csv('Detailed Cases sexual Assault 2001-2008.csv')

#sidebar
st.sidebar.title('Filters')

#Year filter
Select_year = func_code.multiselect('Select Year',df['Year'].unique())

#State filter
Select_state = func_code.multiselect('Select State', df['States/ UTs/Cities'].unique())

#applying filter
filter_df = df[(df['Year'].isin(Select_year)) & (df['States/ UTs/Cities'].isin(Select_state))]

st.image('rv_logo.webp',width = 100)

#display the title of the dashboard
st.title('Rape Violation Dashboard (2001-2008)')

col1,col2,col3,col4,col5 = st.columns(5)

with col1:
    st.metric(label='Total Rape cases',value = int(filter_df['Rape Cases (Total) No. of Victims - Total Victims'].sum()))
with col2:
    st.metric(label='Total incest cases',value = int(filter_df['Incest (Rape) No. of Victims - Total Victims'].sum()))
with col3:
    st.metric(label='Total Other cases',value = int(filter_df['Other (Rape) No. of Victims - Total Victims'].sum()))
with col4:
    st.metric(label='Incest cases in %',value = float(round(filter_df['Incest (Rape) No. of Victims - Total Victims'].sum()/filter_df['Rape Cases (Total) No. of Victims - Total Victims'].sum()*100,2)))
with col5:
    st.metric(label='Other cases in %',value = float(round(filter_df['Other (Rape) No. of Victims - Total Victims'].sum()/filter_df['Rape Cases (Total) No. of Victims - Total Victims'].sum()*100,2)))

st.subheader('Trend analysis on different Rape cases')

#Yearly rape cases
yearly_cases = filter_df[['Year','Incest (Rape) No. of Victims - Total Victims','Other (Rape) No. of Victims - Total Victims','Rape Cases (Total) No. of Victims - Total Victims']].groupby('Year').sum()

st.line_chart(yearly_cases, x_label='Year', y_label='Total cases')

st.subheader('Trend analysis of Rape cases on different age groups')
#rename for better readability
filter_df.rename(columns={'Rape Cases (Total) No. of Victims - Upto 10 Years':'upto 10',
                         'Rape Cases (Total) No. of Victims - (10-14) Years':'10-14',
                         'Rape Cases (Total) No. of Victims - (14-18) Years':'14-18',
                         'Rape Cases (Total) No. of Victims - (18-30)Years':'18-30',
                         'Rape Cases (Total) No. of Victims - (30-50) Years':'30-50',
                         'Rape Cases (Total) No. of Victims - Above 50 Years':'Above 50'},inplace=True)

age_wise = filter_df[['Year','upto 10','10-14','14-18','18-30','30-50','Above 50']].groupby('Year').sum()

st.line_chart(age_wise, x_label='Year', y_label='Total cases')

#statewise cases
st.title('State count by case %')
state_count = func_code.statewise_rape_case(filter_df)
state_count.set_index('percentage cases',inplace=True)
st.bar_chart(state_count, x_label='percentage cases', y_label='State count')


