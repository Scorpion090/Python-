# If you want to change the elements of tuple then first you have to change tuple in list then you are able to some change in tuple.

t = (1,2,3,4)
t = list(t)
print(type(t))

# Change the element of list - 
t[0] = 88
print(t)
t = tuple(t)
print(type(t))

# Concatinating of two tuples  -
first = (1,2,3)
second = ("Rohan","Vishal","Kamal")
print(first + second)

# count method of tuple - 
print(second.count("Vishal"))
print(second.index("Rohan"))
print(second.index("Vishal"))
print(second.index("Kamal"))

# Note - 
print(t.index(3,1,3))

# We can also check the length of tuple - 
print(len(t))

# Note - You can apply all the method and function of the list if you have converted the tuple in the list - 
