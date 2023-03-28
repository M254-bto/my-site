import streamlit as st
from PIL import Image


links = {
    "twitter": "https://twitter.com/Mickiey254",
    "linkedIn": "https://www.linkedin.com/in/michael-ngecha-57477019a/",
    "Github": "https://github.com/M254-bto"
}

def homepage():

    col1, col2 = st.columns(2, gap='large')
    with col1:
        st.image(Image.open('assets/orange2.png'), width=230)
    with col2:
        st.title("Michael Ngecha")
        st.write('Data Scientist | Machine Learning | Deep Learning')    


        