"""
    Participation in increasing order:
    1.)Avani Jain (2406309): Attended all meetings seriously,Debugging and created About_us.py
    2.)Dasarapalli Paul Nikesh (2403114): Attended all meetings seriously,Debugging,Editting and created rules.py
    3.)Tanuja Potnuru (2404229): Attended all meetings seriously and Debugging and created resourses_refered.py
    4.)Ajinkya Temburne (2404238): Code for Player Vs Computer Mode
    5.)Shivam Rajan (2404233): Code for Logic part,Styling and Debugging
    6.)Ankit Kumar (2403104): Code for displaying board and graph,Logic part and Debugging and Player Vs Player
    Members: 1,2,3,4 have equale contribution in project
"""

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
            default_index=0,
            orientation='horizontal'
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
import time
import streamlit as st
from PIL import Image
def run():
    st.title("Welcome to Snakes And Ladder Game🐍🪜🎲")
    st.write("""
# 𝓣𝓮𝓪𝓶 1 𝓟𝓻𝓸𝓳𝓮𝓬𝓽
""")
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
import streamlit as st 
def run():
    st.title("Modules Used")
    st.write(
    """
    ### 1.StreamLit🛜
    ### 2.Random🎲
    ### 3.MatPlotLib📊
    ### 4.Time⌚
    ### 5.StreamLit Option Menu🎨
    """
    )
    st.write(
    """
    Help from Internet 
    """
    )
    st.write("(1). Used ChatGPT to check errors in our code if any")
    st.write("(2). For drawing snakes and ladders")
    st.write("(3). For chaning background color of home page")
    import streamlit as st 
def run():
    st.markdown(f"## <span style='color:red'>Rule Book 🧾</span>", unsafe_allow_html=True)

    st.write("""
###### 1.) It is a Snake And Ladder Game with 2 game modes:\n
######     1V1\n
######     Player Vs Computer\n
###### 2.) Green lines represent ladders\n
###### 3.) Red lines represent snakes\n
###### 4.) You can choose color of your choice\n
###### 5.) If both the players coincide at the same position, it will be represeted in violet \n
""")
import streamlit as st
import matplotlib.pyplot as plt
import random
import time
from PIL import Image


def run():
    st.write("""    
    # Player vs Computer Snakes and Ladder Game🐍🪜🎲
    """)
    x = 9
    
    c1, c2 = st.columns(2)
    p1 = c1.text_input('Player 1 Name:', placeholder='Type name here..')
    clr1 = c1.selectbox("Select Player 1's color", ['blue', 'green', 'orange','grey','violet'])
    clr2 = 'red'
    if p1:
        d1, d2 = st.columns(2)
        if "player1_position" not in st.session_state:
            st.session_state.player1_position = 0
        if "computer_position" not in st.session_state:
            st.session_state.computer_position = 0
        if "turn" not in st.session_state:
            st.session_state.turn = 1
        snake = {(16,6), (49, 11), (62, 19), (93, 90), (95, 61), (98, 78), (50,66)}
        ladder = {(1, 38), (4, 14), (9, 31), (21, 42), (28, 84), (51, 67), (71, 92), (80, 99)}
        org_snake_pos = {96:85,90:59,82:32,31:6,60:36,31:6,23:3,20:8}
        org_ladder_pos = {2:21,9:30,14:78,37:50,52:71,63:91,70:99,87:94}
        snakes = {i[0]: i[1] for i in snake}
        ladders = {j[0]: j[1] for j in ladder}
        a = 0   
        b = 0
    
        def draw_board(player1_position, computer_position):
            fig, ax = plt.subplots(figsize=(14,14))
            for row in range(10):
                for col in range(10):
                    cell_num = (9 - row) * 10 + col + 1 if row % 2 == 0 else (9 - row) * 10 + (9 - col) + 1
                    if cell_num == player1_position and cell_num == computer_position:
                        color = 'purple'  
                    elif cell_num == player1_position:
                        color = clr1
                    elif cell_num == computer_position:
                        color = 'red'
                    else:
                        color = 'white'
                    ax.text(col + 0.5, 9 - row + 0.5, str(cell_num), va='center', ha='center',
                            bbox=dict(facecolor=color, edgecolor='black', boxstyle='round,pad=1'), fontsize=15)
                    # ax.plot([col, col + 1], [9 - row, 9 - row], color='black')
                    # ax.plot([col, col + 1], [10 - row, 10 - row], color='black')
                    # ax.plot([col, col], [9 - row, 10 - row], color='black')
                    # ax.plot([col + 1, col + 1], [9 - row, 10 - row], color='black')
                    for i in range(11):
                        ax.axhline(i,color='black')
                        ax.axvline(i,color='black')
        

            for start, end in snakes.items():
                start_x, start_y = (start - 1) % 10, 9 - (start - 1) // 10
                end_x, end_y = (end - 1) % 10, 9 - (end - 1) // 10
                ax.plot([start_x + 0.5, end_x + 0.5], [start_y + 0.5, end_y + 0.5], 'r', linewidth=20, alpha=0.4)
            
            for start, end in ladders.items():
                start_x, start_y = (start - 1) % 10, 9 - (start - 1) // 10
                end_x, end_y = (end - 1) % 10, 9 - (end - 1) // 10
                ax.plot([start_x + 0.5, end_x + 0.5], [start_y + 0.5, end_y + 0.5], 'g', linewidth=20, alpha=0.4)
            
            ax.axis('off')
            ax.set_xlim(0, 10)
            ax.set_ylim(0, 10)
            return fig
        # def change_coordinate(n):
        #     org_pos = (9 - n%10) * 10 + int(str(n)[-1]) + 1 if (n%10) % 2 == 0 else (9 - ) * 10 + (9 - col) + 1
            
        def move_player(position, roll):
            if position + roll <= 100:
                new_position = position + roll
                if new_position in org_snake_pos.keys():
                    new_position = org_snake_pos[new_position]
                elif new_position in org_ladder_pos.keys():
                    new_position = org_ladder_pos[new_position]
                return new_position
            return position

        with c1:
            col1, col2, col3, col4 = st.columns(4)
            
            with col2:
                st.write(f"#### :{clr1}[{p1}]")
                button1 = st.button(f"{p1}'s Move")
                if button1 and st.session_state.turn == 1:
                    roll = random.randint(1, 6)
                    a = roll
                    image=["face_1.jpg","face_2.jpg","face_3.jpg","face_4.jpg","face_5.jpg","face_6.jpg"]
                    lst=[]
                    for i in range(random.randint(1,4)):
                        random.shuffle(image)
                        lst=lst+image
                    placeholder = st.empty()
                    if True:
                        for image_path in lst:
                            img = Image.open(image_path)
                            placeholder.image(img)
                            time.sleep(0.1)
                    placeholder.image(f'face_{roll}.jpg')    
                    st.session_state.player1_position = move_player(st.session_state.player1_position, roll)
                    st.session_state.turn = 2
                    if st.session_state.player1_position == 100:
                        st.balloons()
                        st.write(f"🎉 Congratulations! {p1} wins!")
                        st.session_state.turn = None
                        time.sleep(3)
                    elif move_player(st.session_state.player1_position,roll) == st.session_state.player1_position:
                        st.write("Roll Exceeded 🙂!! Try Again")
                # with c2:
                #     placeholder1 = st.empty
                #     placeholder1.pyplot(draw_board(st.session_state.player1_position,st.session_state.computer_position))

                

            with col3:
                time.sleep(2)
                st.write(f"#### :{clr2}[Computer]")
                
                if st.session_state.turn == 2:
                    roll = random.randint(1, 6)
                    b = roll
                    image=["face_1.jpg","face_2.jpg","face_3.jpg","face_4.jpg","face_5.jpg","face_6.jpg"]
                    lst=[]
                    for i in range(random.randint(1,4)):
                        random.shuffle(image)
                        lst=lst+image
                    placeholder = st.empty()
                    if True:
                        for image_path in lst:
                            img = Image.open(image_path)
                            placeholder.image(img)
                            time.sleep(0.1)
                    placeholder.image(f'face_{roll}.jpg')
                    st.session_state.computer_position = move_player(st.session_state.computer_position, roll)
                    st.session_state.turn = 1
                    if st.session_state.computer_position == 100:
                        st.balloons()
                        st.write(f"🎉 Better Luck Next Time")
                        time.sleep(2)
                    elif move_player(st.session_state.computer_position,roll) == st.session_state.computer_position:
                        st.write("Roll Exceeded 🙂!! Try Again")
                # with c2:
                #     placeholder1.pyplot(draw_board(st.session_state.player1_position,st.session_state.computer_position))
        # st.write(""" 
        # # First Player Move -> """,a)
        # st.write("""
        # # First Player Position -> """, st.session_state.player1_position)
        # st.write("""
        # # Second Player Move -> """,b)
        # st.write("""
        # # Second Player Position""", st.session_state.player2_position)  
        
        st.markdown(f""" 
        # :{clr1}[{p1}'s Move ->] {a}""")
        st.markdown(f"""
        # :{clr1}[{p1}'s Position ->]  {st.session_state.player1_position}""")
        st.markdown(f"""
        # :red[Computer's  Move ->] {b}""")
        st.markdown(f"""
        # :red[Computer's Position ->] {st.session_state.computer_position}""")

        fig, ax = plt.subplots()
        positions = [st.session_state.player1_position, st.session_state.computer_position]
        ax.bar([f'{p1}', f'computer'], positions, color=[clr1, "red"])
        ax.set_title("Current Positions")
        st.pyplot(fig)

        

        if st.session_state.turn == 1:
            with col1:
                st.markdown(f"""
            #### :{clr1}[{p1}'s Move]""")
        else:
            with col4:
                st.markdown(f"""
            ####:red [Computer's Move]""")
        with c2:
            st.pyplot(draw_board(st.session_state.player1_position, st.session_state.computer_position))
import streamlit as st
import matplotlib.pyplot as plt
import random
import time
from PIL import Image

def run():
    st.write("""    
    # 1 vs 1 Snakes and Ladder Game🐍🪜🎲
    """)
    # taking input of names and colours from user
    c1, c2 = st.columns(2)
    p1 = c1.text_input('Player 1 Name:', placeholder='Type name here..')
    p2 = c2.text_input('Player 2 Name', placeholder='Type name here..')
    if p1 and p2:
        clr1 = c1.selectbox("Select Player 1's color", ['red', 'blue', 'green', 'orange','grey','violet'])
        clr2 = c2.selectbox("Select Player 2's color", ['blue', 'red', 'green', 'orange','grey','violet'])
        
        #splitting screen into two columns d1 and d2
        d1, d2 = st.columns(2)
        
        # Assigning variables for player1_position , player2_Position,and turn
        if "player1_position" not in st.session_state:
            st.session_state.player1_position =0
        if "player2_position" not in st.session_state:
            st.session_state.player2_position =0
        if "turn" not in st.session_state:
            st.session_state.turn = 1
            
        #Coordinates of snake and ladder 
        snake = {(16,6), (49, 11), (62, 19), (93, 90), (95, 61), (98, 78), (50,66)}
        ladder = {(1, 38), (4, 14), (9, 31), (21, 42), (28, 84), (51, 67), (71, 92), (80, 99)}
        org_snake_pos = {96:85,90:59,82:32,31:6,60:36,31:6,23:3,20:8}
        org_ladder_pos = {2:21,9:30,14:78,37:50,52:71,63:91,70:99,87:94}
        snakes = {i[0]: i[1] for i in snake}
        ladders = {j[0]: j[1] for j in ladder}
        
        #assigning variable for dice roll for both players
        a = 0 #for player 1
        b = 0 #for player 2
        
        #Drawing board
        def draw_board(player1_position, player2_position):
            fig, ax = plt.subplots(figsize=(14,14))
            for row in range(10):
                for col in range(10):
                    cell_num = (9 - row) * 10 + col + 1 if row % 2 == 0 else (9 - row) * 10 + (9 - col) + 1
                    if cell_num == player1_position and cell_num == player2_position:
                        color = 'purple'  
                    elif cell_num == player1_position:
                        color = clr1
                    elif cell_num == player2_position:
                        color = clr2
                    else:
                        color = 'white'
                    ax.text(col + 0.5, 9 - row + 0.5, str(cell_num), va='center', ha='center',
                            bbox=dict(facecolor=color, edgecolor='black', boxstyle='round,pad=1'), fontsize=15)
                   
            for i in range(11):
                ax.axhline(i,color='black')
                ax.axvline(i,color='black')
            
            #Drawing snakes
            for start, end in snakes.items():
                start_x, start_y = (start - 1) % 10, 9 - (start - 1) // 10
                end_x, end_y = (end - 1) % 10, 9 - (end - 1) // 10
                ax.plot([start_x + 0.5, end_x + 0.5], [start_y + 0.5, end_y + 0.5], 'r', linewidth=20, alpha=0.4)
            
            #Drawing ladders
            for start, end in ladders.items():
                start_x, start_y = (start - 1) % 10, 9 - (start - 1) // 10
                end_x, end_y = (end - 1) % 10, 9 - (end - 1) // 10
                ax.plot([start_x + 0.5, end_x + 0.5], [start_y + 0.5, end_y + 0.5], 'g', linewidth=20, alpha=0.4)
            
            ax.axis('off')
            ax.set_xlim(0, 10)
            ax.set_ylim(0, 10)
            return fig
        
        # function for changing player's position
        def move_player(position, roll):
            if position + roll <= 100:
                new_position = position + roll
                if new_position in org_snake_pos.keys():
                    new_position = org_snake_pos[new_position]
                elif new_position in org_ladder_pos.keys():
                    new_position = org_ladder_pos[new_position]
                return new_position
            return position

        #inside d1
        with d1:
            #splitting d1 into four columns
            col1, col2, col3, col4 = st.columns(4)
            
            #inside col2
            with col2:
                st.write(f"#### :{clr1}[{p1}]")
               
                #creating button for player1's move
                button1 = st.button(f"{p1}'s Move")
                if button1 and st.session_state.turn == 1:
                    roll = random.randint(1, 6)
                    a = roll
                    
                    #Creating a list containing the path of images of different faces of dice
                    image=["face_1.jpg","face_2.jpg","face_3.jpg","face_4.jpg","face_5.jpg","face_6.jpg"]
                    lst=[]
                    for i in range(5):
                        #Shuffling the image list and adding it to lst
                        random.shuffle(image)
                        lst=lst+image
                        
                    #creating an empty space for placing an image of dice faces further
                    placeholder = st.empty()
                    
                    #Displaying images at the empty spaces randomly
                    if True:
                        for image_path in lst:
                            img = Image.open(image_path)
                            placeholder.image(img)
                            time.sleep(0.1)
                    
                    #placing the final image
                    placeholder.image(f'face_{roll}.jpg')    
                    
                    #Assigning new position to player 1 after the roll of dice
                    st.session_state.player1_position = move_player(st.session_state.player1_position, roll)
                    
                    #Changing the turn to player 2
                    st.session_state.turn = 2
                    
                    # Winning condition for player 1
                    if st.session_state.player1_position == 100:
                        st.balloons()
                        st.write(f"🎉 Congratulations! {p1} wins!")
                        st.session_state.turn = None
                    elif move_player(st.session_state.player1_position,roll) == st.session_state.player1_position:
                        st.write("Roll Exceeded 🙂!! Try Again")
                    
                
            #inside col3
            with col3:
                #same logic as above for player 2
                st.write(f"#### :{clr2}[{p2}]")
                
                button2 = st.button(f"{p2}'s "" Move")
                
                if button2 and st.session_state.turn == 2:
                    roll = random.randint(1, 6)
                    b = roll
                    image=["face_1.jpg","face_2.jpg","face_3.jpg","face_4.jpg","face_5.jpg","face_6.jpg"]
                    lst=[]
                    for i in range(random.randint(1,4)):
                        random.shuffle(image)
                        lst=lst+image
                    placeholder = st.empty()
                    if True:
                        for image_path in lst:
                            img = Image.open(image_path)
                            placeholder.image(img)
                            time.sleep(0.1)
                    placeholder.image(f'face_{roll}.jpg')
                    
                    st.session_state.player2_position = move_player(st.session_state.player2_position, roll)
                    st.session_state.turn = 1
                    
                    if st.session_state.player2_position == 100:
                        st.balloons()
                        st.write(f"🎉 Congratulations! {p2} wins!")
                        st.session_state.turn = None
                    elif move_player(st.session_state.player2_position,roll) == st.session_state.player2_position:
                        st.write("Roll Exceeded 🙂!! Try Again")
    
        # To play again if any player wins 
        if st.session_state.player1_position==100 or st.session_state.player2_position==100:
            st.markdown("""
            ### :blue[Play Again..]""")
            
            #creating reload button to play again
            reload_button = st.button("Play Again")
            
            if reload_button:
                st.session_state.player2_position = 0
                st.session_state.player1_position = 0
                
        #Marking players move and their current position
        st.markdown(f""" 
        # :{clr1}[{p1}'s Move ->] {a}""")
        st.markdown(f"""
        # :{clr1}[{p1}'s Position ->]  {st.session_state.player1_position}""")
        st.markdown(f"""
        # :{clr2}[{p2}'s  Move ->] {b}""")
        st.markdown(f"""
        # :{clr2}[{p2}'s Position ->] {st.session_state.player2_position}""")

        #Plotting bar graph representing their current position
        fig, ax = plt.subplots()
        positions = [st.session_state.player1_position, st.session_state.player2_position]
        ax.bar([f'{p1}', f'{p2}'], positions, color=[clr1, clr2])
        ax.set_title("Current Positions")
        st.pyplot(fig)

        #Showing player's turn 
        if st.session_state.turn == 1:
            with col1:
                st.markdown(f"""
            ### :{clr1}[{p1}'s Move]""")
        else:
            with col4:
                st.markdown(f"""
        ### :{clr2}[{p2}'s Move]""")
        
        #plotting board in column d2
        with d2:
            st.pyplot(draw_board(st.session_state.player1_position, st.session_state.player2_position))
        


