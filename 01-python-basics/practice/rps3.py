"""
Module: Rock, Paper, Scissors Game (Version 3)
Description: An interactive command-line Rock, Paper, Scissors game 
implementing Python Enums, input validation, recursion for replay loops, 
and randomized computer choices.
Author: Arowolo Abdullah
Learning Journey: Ai-engineering-journey
"""

import random
import sys
from enum import Enum


def play_rps():
    # Define game choices using Enum for cleaner, structured constants
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    # Prompt user for input and validate selection
    playerchoice = input(
        "Enter...\n1 for rock\n,\n2 for paper,\n3 for scissors:\n\n"
    )

    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3.")
        return play_rps()

    player = int(playerchoice)
    computer = random.randint(1, 3)

    print(f"You chose {playerchoice}.")
    print(f"Python chose {computer}.")
    print("")

    # Core game logic: determine win, loss, or tie
    if player == 1 and computer == 3:
        print("You win! 🎉")
    elif player == 2 and computer == 3:
        print("You win! 🎉")
    elif player == 3 and computer == 1:
        print("You win! 🎉")
    elif player == computer:
        print("Tie game!")
    else:
        print("Python wins! 😲")

    print("\nPlay again?")

    # Validation loop for replay prompt
    while True:
        playagain = input("\nY for Yes or \nQ to quit \n\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    # Handle replay decision using recursion or exit
    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n🎉🎉🎉🎉")
        print("Thanks for playing!\n")
        sys.exit("Bye!")


# Start the game
play_rps()