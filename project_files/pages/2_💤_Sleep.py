import streamlit as st
import pandas as pd
from PIL import Image
import altair as alt
from sidebar import add_sidebar

# Read in the CSV file
df = pd.read_csv('https://raw.githubusercontent.com/travorhouse12/self-tracker/main/project_files/daily_sleep.csv')

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


seven_days_back = pd.to_datetime('today').date() - pd.Timedelta(days=7)

df = df.loc[df['day'] >= str(seven_days_back)]

altairers = alt.Chart(df).mark_area().encode(
    x="day",
    y="total_sleep",
    color="source:N"
)

st.altair_chart(altairers, use_container_width=True)

# st.area_chart(df, x='day', y='total_sleep')