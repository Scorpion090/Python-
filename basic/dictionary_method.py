first = {
    11:112,2:113,3:144
}
second = {
    4:11    5,5:116,6:117,7:118
}

# Update the dictionary - 
first.update(second)
print(first)

# Clear of the dictionary - 
# first.clear()
# print(first)

# second.clear()
# print(second)

# Create an Empty dictionary - 
emp = {}
print(emp)

# difference between empty dictionary and empty set - 
s = set()
print(s)

# Remove the key and value pairs from the dictionary -
first.pop(3)
print(first)

# Direct remove the last key value pairs from the dictionary - 
print(second.popitem())

# Delete the whole dictionary with del keyword - 
# del first
print(first)

