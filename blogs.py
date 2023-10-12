import streamlit as st

def blogs():
    st.write(
        """
        ##### Ive been out and about
        """
    )

    st.write("Here's my Medium article:")
    embed_code = """<iframe src="https://medium.com/@ngechamike26/exploratory-data-analysis-eda-through-data-visualization-bc1bf1dce3b2" style="width:100%; height:600px; border:none;"></iframe>"""
    iframe_url = "https://medium.com/@alanjones/embed/f40ae8142e50"

# Use st.components.iframe to display the iframe
    # st.components.iframe(iframe_url, height=600, width=800)

# Paste the embed code into the Streamlit page
    st.markdown(embed_code, unsafe_allow_html=True)
