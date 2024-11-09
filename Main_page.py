import streamlit as st
from streamlit_option_menu import option_menu
import Home
import snake_and_ladder
import About_us
import resources_refered
import rules
import snake_and_ladder_computer

#setting page configuration 
st.set_page_config(
    page_title="Project",
    layout='wide'
)


def run():
    #creating side bar
    with st.sidebar:
        
        #creating option menu in the side bar
        app=option_menu(
            menu_title='Project',
            options=['🏡Home','🐍Game','❓About Us❔','🛜Resources Used/Refered',"🧾Rule Book "],
            icons=['h', 'g','h','j','a'],
            default_index=0
        )
    if app=='🏡Home':
        Home.run()
    if app=='🐍Game':
       
        ap = option_menu(
            menu_title="Game Mode",
            options = ["Player🧍‍♂️ vs Player🧍‍♂️", "Player🧍‍♂️ vs Computer"],
            default_index=0
        )
        if ap == "Player🧍‍♂️ vs Player🧍‍♂️":
            snake_and_ladder.run()
        if ap  == "Player🧍‍♂️ vs Computer":
            snake_and_ladder_computer.run()       
    if app=='❓About Us❔':
        About_us.run()
    if app == '🛜Resources Used/Refered':
        resources_refered.run()
    if app == "🧾Rule Book ":
        rules.run()
        
run()
