# Dictionaries

band = {
    "kwara": "ilorin",
    "lagos": "ikeja"
}

band2 = dict(kwara = "ilorin", lagos = "ikeja")

print(band)
print(band2)
print(type(band))
print(len(band2))

#Accesing dict items
print(band["kwara"])
print(band2["lagos"])

print(band.get("kwara"))
print(band2.get("lagos"))

#listing all keys 
print(band.keys())

#listing of values
print(band.values())

#listing of key/value pairs as tuples
print(band.items())

#verifying a key exist
print("lagos" in band)
print("offa" in band2)

#change values
band["lagos"] = "oshodi"
band.update({"kwara" : "offa"})

print(band)

#remove items
print(band.pop("lagos"))
print(band)

band["lagos"] = "ikeja"
print(band)

print(band.popitem())  #tuple

#delete and clear
band.update({"adamawa": "yola"})
print(band)
del band["adamawa"]
print(band)

band2.clear()
print(band2)

# copying dictionaries 

# band2 = band # create a reference 
# print("bad copying method!")
# print(band2)
# print(band)

# band2["kwara"] = "Molete"
# print(band)

band2 = band.copy()
band2["kwara"] = "Molete"
print("good copy")
print(band)
print(band2)

# or use the dict() construction function 
band3 = dict(band)
print("Good copy!")
print(band3)

#nested dictionaries 

state1 = {
    "state" : "capital",
    "Abia" : "umuhaia"
}
state2 = {
    "state" : "capital",
    "Adamawa" : "Yola"
}
band = {
    "state1" :state1,
    "state2" :state2
}
print(band)
print(band["state1"]["state"])

#sets

nums = {1,2,3,4,5}
nums2 = set((1,2,3,4,5))

print(nums)
print(nums2)
print(type(nums))
print(len(nums2))

# N0 duplicated is allowed
nums3 ={1,2,3,3,2,4,5}
print(nums3)

#True is a dup of 1, false is a dup of zero 
nums4 = {1,2,False,3 ,3,0,True}
print(nums4)

#check if a values is in a set 
print(2 in nums4)

#but you cannot refer to an element in the set with an index position or a key 

# Adding a  new element to a set
nums4.add((5,6,7))
print(nums4)

#Adding element from one set to another
morenums = {7,8,9}
nums.update(morenums)
print(nums)

#you can use update with lists,tuples and dictionaries, too. 

#Merging two sets to create a new set 
set1 = {1,2,3}
set2 = {4,5,6}

newset = set1.union(set2)
print(newset)

#keeping only the duplicates 

set1 = {1,2,3}
set2 = {4,5,6,2,1}
set1.intersection_update(set2)
print(set1)

#keeping everything except the duplicate 

set1 = {1,2,3}
set2 = {4,5,6,2,1}

set1.symmetric_difference_update(set2)
print(set1)