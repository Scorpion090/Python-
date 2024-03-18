# Tuple - Tuple is an Immutable data type in python. We can't change the value of tuple. Tuple items separated by commas and inclosed with round brackets.Tuple can store multiplel data type values.

tup = (1,2,3,"Rohan")
print(tup.index(2))
print(type(tup),tup)
# tup[0] = 90     Throw an Error we can't change the value of the tuple.

# If you are creating one element tuple then you have to take comma,otherwise it will show different data type.
t = (1,)
print(type(t))
print(t)

# printing the elements of tuple -
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
# print(tup[4])   Throw an Error baecause tuple index out of range .


# indexing of tuple - 
print(tup[1])
print(tup[2])
print(tup[3])

# Negative indexing of tuple - 
print(tup[-1])
print(tup[-2])
print(tup[-3])


# Check the items is contaning the tupe or not .
if "Rohan" in tup:
    print("Yes!")
else:
    print("No!")

# We can slicing of tuple but origional tuple will not be change a new tuple will return .
print(tup[0:4])

