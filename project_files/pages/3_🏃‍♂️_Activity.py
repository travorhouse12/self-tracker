import streamlit as st
import pandas as pd
from PIL import Image
import altair as alt
from datetime import datetime, timedelta
from sidebar import add_sidebar

# Read in the CSV file
df = pd.read_csv('https://raw.githubusercontent.com/travorhouse12/self-tracker/main/project_files/activity.csv')

# Set page layout
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded")

add_sidebar()

# Set the title of the app
st.title("🏃‍♂️ Activity Hub")

# Set empty space
space = st.empty()
space.header("")


# Filter to only include the date range needed for the chart
df['activity_time'] = (df['activity_time'] / 3600).round(2)

# Create a bar chart to display the activity data
chart = alt.Chart(df).mark_bar().encode(
    x='day',
    y=alt.Y('activity_time', title='Total Hours'),
    color='activity_type:N'
)

st.altair_chart(chart)