import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title="Data",
    page_icon=":guardsman:",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("Data")
st.selectbox(
    "Selecciona un estado",
    ["California", "Florida", "Illinois", "New York", "Texas", "Washington"],
    key="data_source",
)