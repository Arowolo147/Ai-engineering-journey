# ======================
# WHILE LOOPS
# ======================

# Simple while loop with break
value = 1
while value <= 10:
    print(value)
    if value == 5:
        break
    value += 1

print("----------")

# While loop with continue and else
value = 0
while value < 10:
    value += 1
    if value == 5:
        continue   # Skip the number 5
    print(value)
else:
    print("Value is now equal to " + str(value))

print("----------")

# ======================
# FOR LOOPS
# ======================

names = ["Emir", "Arowolo", "Abdullahi"]

# Loop through a list
for name in names:
    print(name)

print("----------")

# Loop through a string
for letter in "Nigeria":
    print(letter)

print("----------")

# For loop with break
for name in names:
    if name == "Abdullahi":
        break
    print(name)

print("----------")

# For loop with continue
for name in names:
    if name == "Arowolo":
        continue
    print(name)

print("----------")

# ======================
# RANGE FUNCTION
# ======================

# range(stop)
for y in range(5):
    print(y)

print("----------")

# range(start, stop)
for x in range(2, 5):
    print(x)

print("----------")

# range(start, stop, step)
for x in range(5, 100, 5):
    print(x)
else:
    print("Glad that's over!")

print("----------")

# ======================
# NESTED LOOPS
# ======================

names = ["Emir", "Arowolo", "Abdullahi"]
actions = ["codes", "sleeps", "eats"]

# Nested loop - Name first
for name in names:             #outer loop
    for action in actions:     #inner loop
        print(name + " " + action + ".")

print("----------")

# Nested loop - Action first
for action in actions:
    for name in names:
        print(name + " " + action + ".")