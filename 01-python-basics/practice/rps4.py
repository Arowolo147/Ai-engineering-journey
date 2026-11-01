"""
Module: Rock, Paper, Scissors Game (Version 4)
Description: An interactive command-line Rock, Paper, Scissors game 
implementing global state tracking (game counter), nested helper functions 
for winner evaluation, and clean recursive replay loops.
Author: Arowolo Abdullahi
Learning Journey: Ai-engineering-journey
"""

import random
import sys
from enum import Enum

# Global state tracker to remember total games played across recursive rounds
game_count = 0


def play_rps():
    # Define game choices using Enum for cleaner code structure
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    # Prompt user for choice and validate input
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

    # Nested helper function to encapsulate game logic and evaluate the outcome
    def decide_winner(player, computer):
        if player == 1 and computer == 3:
            return "You win! 🎉"
        elif player == 2 and computer == 3:
            return "You win! 🎉"
        elif player == 3 and computer == 1:
            return "You win! 🎉"
        elif player == computer:
            return "Tie game!"
        else:
            return "Python wins! 😲"

    # Evaluate game result
    game_result = decide_winner(player, computer)
    print(game_result)

    # Modify the global game counter using the 'global' keyword
    global game_count
    game_count += 1

    print(f"\nGame count: {game_count}")
    print("\nPlay again?")

    # Replay input validation loop
    while True:
        playagain = input("\nPlay again? \nY for Yes or \nQ to quit \n\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    # Handle replay decision via recursion or clean exit
    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n🎉🎉🎉🎉")
        print("Thanks for playing!\n")
        sys.exit("Bye!")


# Start the game
play_rps()