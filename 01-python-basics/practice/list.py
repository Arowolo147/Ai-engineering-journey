users = ["Arowolo", "Abdullahi", "Usman"]

data =["Emir", 42, True]

emptylist = []
print ("Arowolo" in emptylist )

print(users[1])
print(users[-2])

print(users.index("Usman"))
print(users[0:2])
print(users[1:2])
print(users[1:])
print(users[-3:-1])

users.append("Olajide")
print(users)

users += ["Olajide"]
print(users)

users.extend(data)
print(users)

users.insert(0, "Bob")
print(users)

users[2:2] = ["Eddie", "Alex"]
print(users)

users[1:3] = ["Laide","Ayomide"]
print(users)

users.remove('Usman')
print(users)

users.pop()
print(users)

users += ["EMir", "Amoo"]
print(users)

del users[2]
print(users)

data.clear()
print(data)

users[1:2] = ["Diane", "Tom"]
print(users)

users[1:3] = ["lao", "Bill"]

# Fix: Remove non-string items before sorting
users = [item for item in users if isinstance(item, str)]
users.sort(key=str.lower)
print(users)

nums = [2 ,4, 53,98,1,5]
nums.reverse()
print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]
print(numscopy)
print(mynums)
print(mycopy)

print(type(nums))

mylist = list([1, "omolayo", "Arike"])
print (mylist)

#Tuples
mytuple = tuple(("Dave", 45, 87, "emir"))
anothertuple = ('olajide', 'Amoo', 'Arike', 'Bolanle', 'Amoo', 'Amoo', 'Amoo',)
print(mytuple)
print(anothertuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
print(newlist)
newtuple = tuple(newlist)
print(newtuple)

(one, two, *hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count('Amoo'))