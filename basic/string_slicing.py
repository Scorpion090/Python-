# This is all about the string slicing in the python programing language .
fruit = "Mango"
l = len(fruit)
print("Mango is a",l, "Character word")

# Access the characters of fruit Mango - 

# - We use of square brackets for slicing in string because square brackets means accesss the individual characters of string - 

# positive slicing - 

print(fruit[0:5])
print(fruit[0:])
print(fruit[:5])
print(fruit[:])

# Negative slicing - 
fruit = "Mango"
print(fruit[0:])
print(fruit[0:-3])
print(fruit[-5:])


# Here python automaticaly take the concept of len(fruit) - 
print(fruit[2:])
print(fruit[-3:])

nm = "Harry"
print(nm[-4:-2])


