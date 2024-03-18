# This is all about the function - 

a = int(input("Enter the number here : "))
b = int(input("Enter the number here : "))
def Gmean(a, b):
    result = (a + b)//2
    return ("The Geometric mean of this function is = ", result)
ans = Gmean(a, b)
print(ans)

# There is a another function here: 
num = int(input("Enter the number here :"))
def squere(num):
    return num * num
output = squere(num)
print(output)

# Create a function to add of two numbers - 
first = int(input("Enter the number  here :"))
second = int(input("Enter the number  here :"))
def add(first, second):
    return first + second
m = add(first, second)
print(f"The sum of {first} and {second} is  = {m}")

# There is an Another function for adding the numbers - 
def sum(m,n):
    print(m + n)
sum(2,3)
sum(4,3)


# Find the factorial of user entered number with the help of functions - 
number = int(input("Enter the number here :"))
def factorial(number):
    fact = 1
    for i in range(1,number+1):
        fact = fact * i 
    return fact
result = factorial(number)
print(f"The factorial of {number} is  = {result}")

# Find the factorial without functions - 
n = int(input("Enter the number here :"))
f = 1
for i in range(1,n+1):
    f = f * i
print(f"The factorial of {n} is  = {f}")

# Find the factorial with the help of math module - 
import math
n2 = int(input("Enter the number here : "))
ff = math.factorial(n2)
print(f"The factorial of {n2} is  = {ff}")


