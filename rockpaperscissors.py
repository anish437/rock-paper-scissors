



import streamlit as st
import random

Rock="rock"
Paper="paper"
Scissors="scissors"
game_images=[Rock,Paper,Scissors]
st.write("Welcome to Rock Paper Scissors Game")
st.write("1. Rock")
st.write("2. Paper")
st.write("3. Scissors")
user_choice = st.text_input("Enter your choice (Rock, Paper, Scissors): ").lower()

# initialize counters in session state
if 'count' not in st.session_state:
    st.session_state.count = 0
if 'rounds' not in st.session_state:
    st.session_state.rounds = 0

play = st.button("Play")
if play:
    computer_choice = random.choice([Rock, Paper, Scissors])
    st.write("Computer chose:", computer_choice)
    if user_choice == computer_choice:
        st.write("It's a tie!")
    elif (user_choice == Rock and computer_choice == Scissors) or \
         (user_choice == Paper and computer_choice == Rock) or \
         (user_choice == Scissors and computer_choice == Paper):
        st.write("You win!")
        st.session_state.count += 1
    else:
        st.write("Computer wins!")

    
    st.session_state.rounds += 1

score = st.session_state.get('count', 0)
st.write("Your score:", score)
st.write("Rounds played:", st.session_state.get('rounds', 0))
if st.button("Reset score"):
    st.session_state.count = 0
    st.write("Score reset to 0")

if st.button("Reset rounds"):
    st.session_state.rounds = 0
    st.write("Rounds reset to 0")
