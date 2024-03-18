for i in range(6):
    print(i)
else:
    print("Thanks for using this program!")

# If i break my program then else will be not executw - 
for i in range(6):
    print(i)
    if i==4:
        break
else:
    print("Thanks for using this program!")

# Do this with the help of while loop - 
i = 0
while(i<6):
    print(i)
    i = i+1
else:
    print("Thanks for using this program!")

i = 0
while(i<6):
    print(i)
    if i==4:
        break
    i = i + 1
else:
    print("Thanks for using this program!")

