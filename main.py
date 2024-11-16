import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import Preprocessor as Pre

import pydeck as pdk
import seaborn as sns

# changing the layout of streamlit
st.set_page_config(layout = "wide")

import warnings
warnings.filterwarnings('ignore') #suppresses the warnings displayed by the code editor.


# Load the dataset
df = pd.read_csv("Detailed Register and Unregistered cases (Sexual assault) (Punished Release) 2018.csv")

# cleaning the data
df = df.dropna()
# droping all the values


st.sidebar.title("Filters")

# Sidebar for selecting a year range
st.sidebar.header("Filter by ")
st.sidebar.multiselect("State Filter",df["State/UT"])


# Plotting the data
plt.figure(figsize=(10, 5))
sns.barplot(x="State/UT", y="Rape (Total) (Sec.376 IPC)")
plt.xlabel("State/UT")
plt.ylabel("Rape (Total) (Sec.376 IPC)")
plt.title("Total Rape Cases by State/UT (Filtered)")

# Display the plot
st.pyplot(plt)



