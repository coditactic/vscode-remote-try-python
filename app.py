#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# build a console mini game in python , the game is called "rock, paper or scissors"
# the game should be played between the user and the computer
# the game should be played for 5 rounds
# the game should be played in the console
# end of the game the winner should be announced
# the game should be played in the console
# end of the game the winner should be announced

import random

user_score = 0
computer_score = 0

print("Welcome to the game of Rock, Paper, Scissors!")

for i in range(5):
    user_choice = input("Enter your choice (rock/paper/scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_actions)
    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
            user_score += 1
        else:
            print("Paper covers rock! You lose.")
            computer_score += 1
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
            user_score += 1
        else:
            print("Scissors cuts paper! You lose.")
            computer_score += 1
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
            user_score += 1
        else:
            print("Rock smashes scissors! You lose.")
            computer_score += 1

print(f"\nFinal Scores:\nUser: {user_score}\nComputer: {computer_score}")
