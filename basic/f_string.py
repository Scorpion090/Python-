# We use of f-string for use integer,float and many more data type in our string . f-string inclode in python 3.6 version.

# Note - Before python 3.6 we had useed format method.

num = int(input("Enter the number here :"))
num2 = int(input("Enter the second number here :"))
print("The first number is {0} and the second number is {1}".format(num,num2))

# But we can do this with the help of f-string method - 
print(f"The first number is{num} and the second number is {num2} and the sum of both is {num+num2}")

# There is an Another example  - 
letter = ("My name is {} and i'm from {}")
name = input("Enter the your name here: ")
country = input("Enter the your country name here:")
print(letter.format(name,country))

# We can also do this  with this - 👇🏼
letter = ("My name is {1} and i'm from {0}")
name = input("Enter the your name here: ")
country = input("Enter the your country name here:")
print(letter.format(country,name))

# There is a another example - 
num = int(input("Enter the value of number here :"))
print("The value of your number is = {:.2f}".format(num))

sst = int(input("Enter the any number value here :"))
print(f"The value of your number is {sst:.3f}")

# If i want to use f-string something like this - 
n = input("Enter the your name here:")
s_n = input("Enter the your surname here:")
print(f"name is {{n}} and surname is {{s_n}}")
