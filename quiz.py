questions = [
    ["What is a variable in programming?", "A variable is a named storage that holds data which can be changed during program execution."],
    ["What is a function in programming?", "A function is a block of reusable code that performs a specific task."]
]
for question in questions:
    user_input = input(f"{question[0]}\nYour answer: ")

if user_input == question[1]:
    print("Correct!\n")
else:
    print("Incorrect.\n")