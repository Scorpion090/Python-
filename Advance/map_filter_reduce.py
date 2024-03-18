# This is all about the map,filter and reduce of the python programing language .

# 1. Map
num = int(input("Enter the number here :"))
def square(item):
    return item * item
print(square(num))

# Print square of all elements of the list - 
l = [1,2,3,4,5]
newl = []
for i in l:
    newl.append(square(i))
print(newl)

# We can also do this with the help of lambda function -
newl = list(map(square,l))
print(newl)

# We can also use of map function with lambda function - 
l = [1,2,3,4,5]
new = list(map(lambda x : x*x,l))
print(new)


# 2.Filter - 
l = [1,2,3,4,5]
filter_func = lambda x : x>4
newone = list(filter(filter_func,l))
print(newone)


# 3. Reduce - 
from functools import reduce
l = [1,2,3,4,5]
sum = reduce(lambda x ,y: x + y,l)
print(sum)
