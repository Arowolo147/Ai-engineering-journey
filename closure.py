"""
Module: Python Closures Practice
Description: Demonstrates closures in Python, where a nested function 
retains access to variables in its outer function's scope even after 
the outer function has finished execution.
Author: Arowolo Abdullah
Learning Journey: Ai-engineering-journey
"""

# A closure is a nested function that remembers and has access to variables
# in its outer function, even after the outer function has finished running
# and is completely gone.


def parent_function(person, coins):
    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print(f"\n {person} has {coins} coins left.")
        elif coins == 1:
            print(f"\n {person} has {coins} coins left.")
        else:
            print(f"\n {person} is out of coins.")

    return play_game


# Create closures with customized initial states for each player
tommy = parent_function("Tommy", 5)
jenny = parent_function("jenny", 3)

# Play game rounds
tommy()
tommy()
tommy()

jenny()