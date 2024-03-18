l = [1,2,3,4,5]
l2 = [1,2,3,4,5]

print(l is l2)
print(l == l2)

name = ("Rohan Rathore")
name2 = ("Rohan Rathore")
print(name is name2)
print(name == name2)

# Here name and name2 is pointing to the same objects because python knows then name is the constant and it will be not change that's why it will not create other memory.

# We can do this all the immutable data types because immutable data type can not change.

a = None
b = None
print(a is b)
print(a == b)

# Note - There is a biggest difference between is and equals is equal to compare  values and is compare the exact memory location.


# This is the also another program of is and == of the python programing language.
l = [1,2,3]
l2 = [1,2,3]
print(l == l2)
print(l is l2)
