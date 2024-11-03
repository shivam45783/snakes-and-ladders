import streamlit as st
from streamlit_option_menu import option_menu
import Home
import snake_and_ladder
import About_us
import resources_refered

#setting page configuration 
st.set_page_config(
    page_title="Project",
    layout='wide'
)

# creating a MultiApp class to store all the files 
class MultiApp:
    def __init__(self) -> None:
        self.apps=[]
    def add_app(self,title,func):
        self.apps.append({
            'title':title,
            'function':func
        })
    def run():
        #creating side bar
        with st.sidebar:
            
            #creating option menu in the side bar
            app=option_menu(
                menu_title='Project',
                options=['🏡Home','🐍Game','❓About Us❔','🛜Resources Used/Refered'],
                icons=['h', 'g','h','j'],
                default_index=0
            )
        if app=='🏡Home':
            Home.run()
        if app=='🐍Game':
            # snake_ladder.run()
            snake_and_ladder.run()
        if app=='❓About Us❔':
            About_us.run()
        if app == '🛜Resources Used/Refered':
            resources_refered.run()
        
    run()
