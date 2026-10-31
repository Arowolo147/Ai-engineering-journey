import sys
import random 
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagain = True

while playagain:

    playerchoice = input("Enter...\n1 for rock\n,\n2 for paper,\n3 for scissors:\n\n")

    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("you must enter 1,2,or 3")

    computer = random.randint(1, 3)

    print(f"you chose {playerchoice}.")
    print(f"python chose{computer}.")
    print("")

    if player == 1 and computer == 3:
        print("you win!🎉")
    elif player == 2 and computer == 3:
        print("you win!🎉")
    elif player == 3 and computer == 1:
        print("you win!🎉")
    elif player == computer:
        print("Tie game")
    else: 
        print("python wins!😲")

    playagain = input("\nplay again? \nY for Yes or \nQ to quit \n\n")

    if playagain.lower() =="y":
        continue
    else:
        print("\n🎉🎉🎉🎉")
        print("Thanks for playing\n")
        playagain = False 
sys.exit("Bye!")