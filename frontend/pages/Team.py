import streamlit as st


col1, col2,col3 = st.columns(3)
with col1:
    st.image(r'..\frontend\assets\team\IMG-20240622-WA0093.jpg',width=200)
    st.markdown('**Arnaldo Quiñones**')
    st.text('''Data Analytics, 
Marketing''')
    st.image(r'..\frontend\assets\team\IMG-20240622-WA0094.jpg',width=200)
    st.markdown('**Roman Acuña**')
    st.text('''Data Engineer,
Cloud Architect''')
with col2:
    st.image(r'..\frontend\assets\team\IMG-20240622-WA0095.jpg',width=200)
    st.markdown('**Leandro Funes**')
    st.text('''Machine Learning 
Engineer''')
    st.image(r'..\frontend\assets\team\IMG-20240622-WA0096.jpg',width=200)
    st.markdown('**Braulio Pierotti**')
    st.text('''  Data Analytics, 
Project Leader''')
with col3:
    st.image(r'..\frontend\assets\team\IMG-20240622-WA0097.jpg',width=200)
    st.markdown('**Federico Mamani**')
    st.text('''Data Engineer, 
Cloud Architect''')