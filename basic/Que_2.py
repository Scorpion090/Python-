# Que - 2. Write a program to ask the number from user and print the start of that number line by line.

num = int(input("Enter the number over here:"))
for i in range(1,num+1):
    print(i * "*")