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
    p1 = c1.text_input('Player 1 Name: ', placeholder='Type name here..')
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
