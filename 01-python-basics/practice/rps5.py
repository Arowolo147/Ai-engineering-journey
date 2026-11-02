"""
Module: Rock, Paper, Scissors Game (Version 5)
Description: An advanced implementation of Rock, Paper, Scissors utilizing 
closures and the 'nonlocal' keyword to track game state, player wins, 
and python wins across multiple recursive rounds without global variables.
Author: Arowolo Abdullah
Learning Journey: Ai-engineering-journey
"""

import random
import sys
from enum import Enum


def rps():
    """Factory function that encapsulates state (game counts and wins)

    and returns the play_rps closure function.
    """
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

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

        # Nested helper function to evaluate outcome and update win counts
        def decide_winner(player, computer):
            nonlocal python_wins
            nonlocal player_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return "You win! 🎉"
            elif player == 2 and computer == 3:
                player_wins += 1
                return "You win! 🎉"
            elif player == 3 and computer == 1:
                player_wins += 1
                return "You win! 🎉"
            elif player == computer:
                return "Tie game!"
            else:
                python_wins += 1
                return "Python wins! 😲"

        # Evaluate game result
        game_result = decide_winner(player, computer)
        print(game_result)

        # Update and display total game count using nonlocal scope
        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"Player wins: {player_wins}")
        print(f"Python wins: {python_wins}")

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

    return play_rps


# Initialize the closure and start the game
play = rps()
play()