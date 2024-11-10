import time
import streamlit as st
from PIL import Image
def run():
    st.title("Welcome to Snakes And Ladder Game🐍🪜🎲")
    st.write("""
# 𝓣𝓮𝓪𝓶 1 𝓟𝓻𝓸𝓳𝓮𝓬𝓽
""")
    #Writing HTML Code for background color(REFERED FROM INTERNET)
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #000000; /* Black color */
            color: #ffffff; /* Optional: Set text color to white for better contrast */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    img=Image.open("crown.jpg")
    st.image(img,width=800)
    st.write("""
## *You are born to win, but to be a winner, you must plan to win, prepare to win, and expect to win.*""")
