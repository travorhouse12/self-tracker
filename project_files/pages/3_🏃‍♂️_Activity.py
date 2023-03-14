import streamlit as st
import pandas as pd
from PIL import Image
from sidebar import add_sidebar

# Read in the CSV file
df = pd.read_csv('https://raw.githubusercontent.com/travorhouse12/self-tracker/main/project_files/total_sleep.csv')

# Set page layout
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded")

add_sidebar()

# Set the title of the app
st.title("Activity Hub")

# Set empty space
space = st.empty()
space.header("")

# Create a bar chart to display the activity data
df['date'] = df['date'].astype('category')
st.bar_chart(df, x='date', y='Total Sleep Duration')
