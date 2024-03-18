"""TypeCasting-
                TypeCasting is a way of converting one data type into another if possible.

There are two types of type casting in string - 
                                                1. Explicit type casting.(We need to do.)
                                                2. Emplicit type casting.(Python automaticaly do this.) """

# 1.Explicit type casting - 

a = '1'
print(a)

print(int(a))

b = "Rohan"
# print(int(b))   # It is not possible.

one = "1"
two = 2
print(one)
print(int(one) + two)  

# Let's take another example.
first = "1"
second = "2"
print(first + second)

# After typecasting to this - 
print(int(first) + int(second))


# Another example - 

name = "Mahesh "
surname = "Rathore"
print(name + surname)

# 2. Emplicit type casting -

s = 9
t = 1.9
print(s + t)   # python has automaticaly convert this data into floating point numbers.

