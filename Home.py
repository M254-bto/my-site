import streamlit as str
from streamlit_option_menu import option_menu
from homepage import homepage


selected = option_menu(
    menu_title=None,
    options=['Home', 'Projects', 'Blog', 'Contact'],
    icons=['house-heart', 'code-slash', 'list', 'envelope'],
    orientation='horizontal',
    styles={
    "nav-link-selected":{
    "background-color": 'purple'
    },
    "container":{'background-color': 'transparent',
                 'margin-top': ''
                },
    }
)


if selected == 'Home':
    homepage()
if selected == 'Projects':
    str.write("This is projects")
if selected == 'Blog':
    str.write("This is blogs")
if selected == 'Contact':
    str.write("Contact")

