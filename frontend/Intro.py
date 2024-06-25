import streamlit as st

from streamlit_option_menu import option_menu

name = 'Data Devs Prediction System'
icono = 'data_devs_logo.ico'

st.set_page_config(page_title= name, page_icon= icono, layout='centered')

st.image(r'..\frontend\assets\data_devs_desk.jpg')
st.title(name)
st.markdown('''
         **Somos una empresa dedicada al desarrollo de sistemas de predicción basados en datos.**
                
                ''')
