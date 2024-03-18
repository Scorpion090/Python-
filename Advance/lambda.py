# This is all about the lambda function - 
# Lambda is a one line function - 

num = int(input("Enter the any number here:"))
sum = lambda num: num*num
print(f"The square of {num} is = {sum(num)}")

# Creating the lambda function which is calculating the sum of two numbers - 
a = int(input("Enter the first number here:"))
b = int(input("Enter the second number here:"))
add = lambda a,b: a + b
print(add(a,b))

# Here lambda is a keyword .
# write a average function - 
number1 = int(input("Enter the number here:"))
number2 = int(input("Enter the number here:"))
avg = lambda a,b: (a+b)//2
print(avg(number1,number2))


# Mostly we use of lambda function when we will use function as a function
def appl(cube, nm):
    return 6 + cube(nm)
nm = int(input("Enter the number here: "))
cube = lambda nm : nm * nm * nm
print(appl(cube,nm))

# We can also do this with the help of lambda functions  -
nm = int(input("Enter the number here: "))
appl = lambda nm : nm * nm * nm  + 6
print(appl(nm))
