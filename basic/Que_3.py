# Que - 3. Write a python program to ask a number from user and check this is a perfect integer or not.

num = input("Enter the number over here: ")
if int(num) == float(num):
    print("This is a perfect integer!")
else:
    print("This is not a perfect integer!")
