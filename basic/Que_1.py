# Que - 1. Write a python program to ask a number from user and print all the factor of the number:

num = int(input("Enter the number over here:"))
factors = []
for i in range(1,num + 1):
    if(num % i == 0):
        factors.append(i)

print(f"The factors of {num} is = {factors}")

