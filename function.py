# A simple function that prints a greeting to the console
def hello_world():
    print("Hello world")

# Calling the hello_world function
hello_world()


# A function to add two numbers with default values of 0
def sum(num1=0, num2=0):
    # Ensure both inputs are integers; return early (None) if not
    if type(num1) is not int or type(num2) is not int:
        return
    return num1 + num2

# Calling the sum function with two integers and storing the result
total = sum(1, 2)
print(total)


# A function using *args to accept a variable number of positional arguments
def multiple_items(*args):
    print(args)           # Prints the arguments as a tuple
    print(type(args))     # Prints the data type (<class 'tuple'>)

# Calling the function with multiple string arguments
multiple_items("Dave", "John", "Sara")


# A function using **kwargs to accept a variable number of keyword arguments
def mult_named_items(**kwargs):
    print(kwargs)         # Prints the arguments as a dictionary
    print(type(kwargs))   # Prints the data type (<class 'dict'>)

# Calling the function with named keyword arguments
mult_named_items(first="Dave", last="Gray")