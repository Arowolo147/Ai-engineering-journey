questions = [
    ["What is a variable in programming?", "A variable is a named storage that holds data which can be changed during program execution."],
    ["What is a function in programming?", "A function is a block of reusable code that performs a specific task."]
]

count = 0

for question in questions:
    user_input = input(f"{question[0]}\nYour answer: ")

if user_input.strip().lower() == question[1].strip().lower():
    print("Correct!\n")
    count += 1
else:
    print("Incorrect.\n")
print(f"You answered {count} out of {len(questions)} questions correctly.")