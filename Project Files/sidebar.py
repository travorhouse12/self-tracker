import streamlit as st

# Create a Streamlit sidebar that contains a profile image and a name
def add_sidebar():
    with st.sidebar:
        st.markdown(
            """
            <style>
                [data-testid="stSidebarNav"] {
                    background-image: url(https://datadayz.com/wp-content/uploads/2023/03/Group-310-1.png);
                    background-repeat: no-repeat;
                    padding-top: 10px;
                    margin-top: 40px;
                    background-position: 10px 10px;
                    background-position-x: center;
                    background-size: 20%;
                    text-align: center;
                }
                [data-testid="stSidebarNav"]::before {
                    content: "Travor House";
                    font-size: 20px;
                    font-weight: bold;
                    position: relative;
                    top: 80px;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )