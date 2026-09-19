import streamlit as st
from connector import GameFactory
import uuid
#Hello i am writing this code
if "game" not in st.session_state:
    st.session_state.game=None

if "message" not in st.session_state:
    st.session_state.message=""

if "game_id" not in st.session_state:
    st.session_state.game_id=str(uuid.uuid4())


#Game setup
if st.session_state.game is None:
    
    st.markdown(

        """
       <style>
       div.stButton > button{

       background-color:#8DB600;
       color: white;
       font-size: 22px;
       
       }
""",unsafe_allow_html=True
    )
    st.title("**Welcome To HangMan Game**")
    user_name=st.text_input("  **Enter your name**")
    word_bank = [
        "Programming & Architecture",
        "Databases & Networking",
        "Marketing & E-commerce",
        "Logic & Science",
        "Anime & Animation"
    ]
    category=st.selectbox("Select the category of words you want to guess",word_bank)

    left_spacer, center_col, right_spacer = st.columns([1, 1, 1])
    with center_col:
        if st.button(' Start Game'):
            factory=GameFactory(user_name,category)
            st.session_state.game=factory.create_game()
            st.rerun()

else:
    
    game=st.session_state.game
    st.markdown("""<h1 style='text-align:center; font-family: "Courier New" ,Courier, monospace; font-size:45px'>👋 Game Started</h1>""",unsafe_allow_html=True)
    if st.session_state.message:
        if "Correct" in st.session_state.message:
            st.toast(st.session_state.message,icon="✅")
        elif "Wrong" in st.session_state.message:
            st.toast(st.session_state.message, icon="❌")
        elif "Won" in st.session_state.message:
            st.toast(st.session_state.message,icon="🏆")
        elif "lost" in st.session_state.message:
            st.toast(st.session_state.message, icon="💀")
        elif "already" in st.session_state.message:
            st.toast(st.session_state.message)
        else:
            st.toast(st.session_state.message, icon="⚠️")
        st.session_state.message = ""
    col1,col2=st.columns(2)
    with col1:

        st.markdown(f"<p style='font-size: 22px'>Player: {game.player.player_name}</p>",unsafe_allow_html=True)
        st.markdown(
            """
            <style>
            [data-testid="stMetricLabel"] p {
        font-size: 22px !important;
         !important;
     
    }
    </style>
    """,
    unsafe_allow_html=True
            
        )

        st.metric(label="Score",value=game.score.get_score)
        #st.write("Attempts: ",game.attempts_remaining)
        # st.write(" Guessed_letters: ",game.word.get_display(game.player.guessed_letters))
       
        
    with col2:
         st.markdown("<p style='font-size: 22px; margin-bottom:2px; ' >Health Remaining</p>",unsafe_allow_html=True)
         st.progress(game.attempts_remaining/6)
         st.markdown(f"<p style='font-size: 22px; margin-bottom: 2px;'>Wrong Guesses: {'  ' .join(game.wrong_guesses)}</p>",unsafe_allow_html=True)
    raw_word=game.word.get_display(game.player.guessed_letters).upper()
    spaced_word=" ".join(raw_word)

    st.markdown(f"""<h1 style='text-align: center; font-size: 50px;  font-family: "Courier New" ,Courier, monospace;'> {spaced_word}</h1>""",unsafe_allow_html=True)   
        
   
  
    if not game.game_over:
        st.markdown("<h2 style='font-size:30 px; text-align:center;'>Control Deck</h2>",unsafe_allow_html=True)
        letters = list("abcdefghijklmnopqrstuvwxyz")
        cols=st.columns(7)
        
        for i,letter in enumerate(letters):
            with cols[i%7]:
                is_guessed=game.player.has_guessed(letter)
                if st.button(letter.upper(),key=f"{st.session_state.game_id}_{letter}",disabled=is_guessed,use_container_width=True):
                    result=game.process_guess(letter)
                    if result=="correct":
                        st.session_state.message="Correct Guess!!"
                    elif result=="wrong":
                        st.session_state.message="Your Guess is wrong"
                    elif result=="repeated":
                        st.session_state.message="You already guess the letter"
        
                    if game.check_win():
                        st.session_state.message="Congratulations You Won!"
                    elif game.check_lose():
                        st.session_state.message="Game Over You lost"
                    st.rerun()
   
    if game.game_over:
        left_spacer, center_col, right_spacer = st.columns([1, 1, 1])
        st.markdown(

        """
       <style>
       div.stButton > button{

       background-color:#8DB600;
       color: white;
       font-size: 22px;
       
       }
""",unsafe_allow_html=True
    )
        with center_col:
            if st.button("New Game"):
                st.session_state.game=None
                st.session_state.message=""
                st.session_state.game_id=str(uuid.uuid4())
                st.rerun()
        


