"""
Module: Python Scope Practice
Description: Exploring variable scope, nested functions, and the 
use of the 'global' and 'nonlocal' keywords to modify outer variables.
Author: Arowolo Abdullah
Learning Journey: Ai-engineering-journey
"""

name = "Dave"
count = 1


def another():
    color = "blue"

    # Use 'global' to modify the front-yard (global) variable 'count'
    global count
    count += 1
    print(count)

    # Nested function demonstrating 'nonlocal' scope
    def greeting(name):
        # Use 'nonlocal' to modify the parent function's 'color' variable
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("Dave")


another()