

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
computer_choice = random.choice([Rock, Paper, Scissors])
st.write("Computer chose:", computer_choice)
if user_choice == computer_choice:
    st.write("It's a tie!")
elif (user_choice == Rock and computer_choice == Scissors) or \
     (user_choice == Paper and computer_choice == Rock) or \
     (user_choice == Scissors and computer_choice == Paper):
    st.write("You win!")
else:
    st.write("Computer wins!")