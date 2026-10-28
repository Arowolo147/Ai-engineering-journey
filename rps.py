import sys
import random 
from enum import Enum

class RPS(Enum):
    APPLE = 1
    BALL = 2
    CAT = 3

print("")
playerchoice = input("Enter...\n1 for apple,\n2 for ball,\n3 for cat:\n\n")

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("you must enter 1,2,or 3")

computerchoice = random.choice("123")
computer = int(computerchoice)

print("")
print("you chose" + playerchoice + ".")
print("python chose" + computerchoice + ".")
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