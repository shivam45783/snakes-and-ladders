import streamlit as st
import matplotlib.pyplot as plt
import random
import time
from PIL import Image


def run():
    st.write("""    
    # Player vs Computer Snakes and Ladder Game🐍🪜🎲
    """)
    
    # taking input of names and colours from user
    c1, c2 = st.columns(2)
    p1 = c1.text_input('Player 1 Name: ', placeholder='Type name here..')
    clr1 = c1.selectbox("Select Player 1's color", ['blue', 'green', 'orange','grey','violet'])
    clr2 = 'red'
    if p1:
        
        # d1, d2 = st.columns(2)
        if "player1__position" not in st.session_state:
            st.session_state.player1__position = 0
        if "computer_position" not in st.session_state:
            st.session_state.computer_position = 0
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
        a = 0   
        b = 0
    
        #Drawing board
        def draw_board(player1__position, computer_position):
            fig, ax = plt.subplots(figsize=(14,14))
            for row in range(10):
                for col in range(10):
                    cell_num = (9 - row) * 10 + col + 1 if row % 2 == 0 else (9 - row) * 10 + (9 - col) + 1
                    if cell_num == player1__position and cell_num == computer_position:
                        color = 'purple'  
                    elif cell_num == player1__position:
                        color = clr1
                    elif cell_num == computer_position:
                        color = 'red'
                    else:
                        color = 'white'
                    ax.text(col + 0.5, 9 - row + 0.5, str(cell_num), va='center', ha='center',
                            bbox=dict(facecolor=color, edgecolor='black', boxstyle='round,pad=1'), fontsize=15)
                    
                    for i in range(11):
                        ax.axhline(i,color='black')
                        ax.axvline(i,color='black')
        
            #Drawing snakes(REFERED FROM INTERNET/AI)
            for start, end in snakes.items():
                start_x, start_y = (start - 1) % 10, 9 - (start - 1) // 10
                end_x, end_y = (end - 1) % 10, 9 - (end - 1) // 10
                ax.plot([start_x + 0.5, end_x + 0.5], [start_y + 0.5, end_y + 0.5], 'r', linewidth=20, alpha=0.4)
            
            #Drawing ladders(REFERED FROM INTERNET/AI)
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
        
        #inside c1
        with c1:
             #splitting c1 into four columns
            col1, col2, col3, col4 = st.columns(4)
            
            #inside col2
            with col2:
                st.write(f"#### :{clr1}[{p1}]")
                button1 = st.button(f"{p1}'s Move")
                
                #creating button for player1's move
                if button1 and st.session_state.turn == 1:
                    roll = random.randint(1, 6)
                    a = roll
                    
                    #Creating a list containing the path of images of different faces of dice
                    image=["face_1.jpg","face_2.jpg","face_3.jpg","face_4.jpg","face_5.jpg","face_6.jpg"]
                    lst=[]
                    for i in range(random.randint(1,4)):
                        
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
                    
                    #Assigning new position to player after the roll of dice
                    st.session_state.player1__position = move_player(st.session_state.player1__position, roll)
                    
                    #Changing the turn to computer
                    st.session_state.turn = 2
                    
                    # Winning condition for player
                    if st.session_state.player1__position == 100:
                        st.balloons()
                        st.write(f"🎉 Congratulations! {p1} wins!")
                        st.session_state.turn = None
                        time.sleep(3)
                    elif move_player(st.session_state.player1__position,roll) == st.session_state.player1__position:
                        st.write("Roll Exceeded 🙂!! Try Again")
                

                
            #inside col3
            with col3:
                #Same logic as above
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
                
        
        # To play again if any player wins 
        if st.session_state.player1__position==100 or st.session_state.computer_position==100:
            st.markdown("""
            ### :blue[Play Again..]""")
            
            #creating reload button to play again
            reload_button = st.button("Play Again")
            
            if reload_button:
                st.session_state.player1__position = 0
                st.session_state.computer_position = 0
        
        #Marking players move and their current position
        st.markdown(f""" 
        # :{clr1}[{p1}'s Move ->] {a}""")
        st.markdown(f"""
        # :{clr1}[{p1}'s Position ->]  {st.session_state.player1__position}""")
        st.markdown(f"""
        # :red[Computer's  Move ->] {b}""")
        st.markdown(f"""
        # :red[Computer's Position ->] {st.session_state.computer_position}""")

        #Plotting bar graph representing their current position
        fig, ax = plt.subplots()
        positions = [st.session_state.player1__position, st.session_state.computer_position]
        ax.bar([f'{p1}', f'computer'], positions, color=[clr1, "red"])
        ax.set_title("Current Positions")
        st.pyplot(fig)

        
        #Showing player's turn 
        if st.session_state.turn == 1:
            with col1:
                st.markdown(f"""
            #### :{clr1}[{p1}'s Move]""")
        else:
            with col4:
                st.markdown(f"""
            ####:red [Computer's Move]""")
        
        #plotting board in column c2
        with c2:
            st.pyplot(draw_board(st.session_state.player1__position, st.session_state.computer_position))
