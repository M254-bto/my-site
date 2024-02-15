import streamlit as st
from PIL import Image
import streamlit.components.v1 as components



links = {
    "twitter": "https://twitter.com/Mickiey254",
    "linkedIn": "https://www.linkedin.com/in/michael-ngecha-57477019a/",
    "Github": "https://github.com/M254-bto",
    "Medium": "https://medium.com/@ngechamike26"
}

def homepage():

    col1, col2 = st.columns(2, gap='small')
    with col1:
        st.image(Image.open('assets/orange2.png'), width=230)
    with col2:
        st.title("Michael Ngecha")
        st.write('Data Scientist | Machine Learning | Deep Learning | Backend')    


        # ----- links ----#
        st.write("#")

        cols = st.columns(len(links))
        for index, (key, value) in enumerate(links.items()):
            cols[index].write(f'[{key}]({value})')

    st.write("#")
    st.write("#")

    st.subheader("Who am i?")

    st.write("""

       I am a proficient and enthusiastic Data Scientist, I have a strong foundation in Python programming and specialize in Data Science and Machine Learning. I am deeply committed to leveraging the power of data to extract insights that not only fuel business growth but also address different challenges in society. With a solid base in data science, analytics, and Machine Learning technologies, my dedication revolves around delivering innovative solutions that unearth data insights, ultimately empowering and informing decisions.
       
        ###### I am Also:
        - A student of Computer Science at Dedan Kimathi University of Technology.

        - Co-Founder and President of Data Science and Artificial Intelligence Club (DSAIC) in mentioned University.

        - Contributor and managing team member of Computer Society of Kimathi.

    """
    )

    st.write("#")
    st.write("#")


    st.subheader("What I do")

    st.write(
       """
       Basically everything Involved in a Data Science and ML project.
       ##### Data Science and Machine Learning;

        - ⭐ Web scrapping using tools like BeautifulSoup and Selenium.

        - ⭐ Working with structured (csv and tsv) data and unstructured data like photos and videos.

        - ⭐ Descriptive, prescriptive, and mostly, Predictive data Analysis.

        - ⭐ Machine Learning Modelling with Python's extensive library.

        - ⭐ Deep Learning and Neural Networks with Tensorflow and the Keras API.

        - ⭐ FastAI for making Deep learning tasks uncool again (Their words, not mine).

        - ⭐ Data ETL(ish).

       ##### Web Technologies

        - ⭐ Web APIs with python's Django and FastAPI.

    

        - ⭐ Structured databases(SQL) Postgre, sqlite.

        - ⭐ Streamlit Interfaces, like this site (built Entirely in Python).

       """
    )


    

   
    st.write("#")
    st.write("#")

    st.subheader("[IGS Capstone requirements](https://docs.google.com/document/d/1PLBwujrJZ7pWplpQ5MoqLwfIacj-nXkyJKvrboDf4-s/edit?usp=sharing)")


    st.write(
        """
        #### How to reach me?

        - Email: ngechamike26@gmail.com
        - phone(and M-Pesa 😂): +245798159691
        """
    )
