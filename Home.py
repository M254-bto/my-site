import streamlit as str
from streamlit_option_menu import option_menu
import homepage, projects, blogs


selected = option_menu(
    menu_title=None,
    options=['Home', 'Projects', 'Blog'],
    icons=['house-heart', 'code-slash', 'list'],
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
    homepage.homepage()
if selected == 'Projects':
    projects.projects()
if selected == 'Blog':
    blogs.blogs()
