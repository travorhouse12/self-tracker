import streamlit as st
import pandas as pd
from PIL import Image
from sidebar import add_sidebar

# Read in the CSV file
df = pd.read_csv('/Users/macbook/Desktop/Data Science Personal/streamlit/total_sleep.csv')

# Set page layout
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded")

add_sidebar()

# Add the profile image
image_url = "https://datadayz.com/wp-content/uploads/2023/03/Group-310-1.png"
st.image(image_url, width=75)

# Set the title of the app
st.title("Travor's health tracker! 👋")