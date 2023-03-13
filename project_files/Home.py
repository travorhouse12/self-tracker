import streamlit as st
import pandas as pd
from PIL import Image
from sidebar import add_sidebar

# Read in the CSV file
df = pd.read_csv('https://raw.githubusercontent.com/travorhouse12/self-tracker/total_sleep.csv')

# Set page layout
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded")

add_sidebar()

# Set the title of the app
st.title("Travor's health tracker! 👋")

# Set empty space
space = st.empty()
space.header("")

# Number for the chart
number = (df['Total Sleep Duration'].loc[df['date'] == '2023-02-03'].sum() / 3600).round(2)

# Function that creates a summar number card with a background
def summary(title, metric, font_size=56, background_color = '#242424'):
    """Create a custom summary number using the st.write function that enables custom sizing, backgrounds, and more."""
    summary_metric = st.write(f"<div style='background-color: {(background_color)}; padding-top: 30px; padding-bottom: 20px; padding-left: 30px; border-radius: 20px; font-size:{(font_size)}px;'><h5>{(title)}</h5><strong>{(metric)}</strong></div>", unsafe_allow_html=True)
    return summary_metric

# Create 3 individual cards
col1, col2, col3 = st.columns(3)

with col1:
    summary(title = "Average Readiness →", metric = number, background_color = '#3E712C')

with col2:
    summary(title = "Average Sleep →", metric = number, background_color= '#551D78')

with col3:
    summary(title = "Average Activity →", metric = number, background_color = '#927221')
