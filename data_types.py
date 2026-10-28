#Build a menu
import math 
title = "menu".upper()
print(title.center(20, "=")) 
print ("cofee".ljust(16, ".") + "$1".rjust(4))
print ("nescafe".ljust(16, ".") + "$2".rjust(4))
print ("topcafe".ljust(16, ".") + "$3".rjust(4))
total = "total".title()
print (total.rjust(34) + "=" +"$6".rjust(10, "."))
remarks = ("thanks for your patronage".title())
print(remarks.center(50, "."))

#string index values 
first = "Abdullah"
last = "Arowolo"
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[:1])
print(first[1:])

# #Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

#numeric data types
#integer type 
price = 200
best_price = int(90)
print (type(price))
print(isinstance(best_price, int))

#float data types
gpa = 4.2
print(type(gpa))

#complex type
com_value = 5+7j
print(type(com_value))
print(isinstance(com_value,complex))

#built in functions for numbers 
print(abs(gpa))
print(round(gpa * -1))
 

print(math.pi)
print(math.sqrt(78))



