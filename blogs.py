import streamlit as st

def blogs():
    st.write(
        """
        ##### Ive been out and about
        """
    )

    st.write("Here's my Medium article:")
    medium_url = "https://medium.com/@ngechamike26/advanced-python-concepts-27d7d42f276e"
    st.components.v1.iframe(medium_url, height=100, scrolling=True)