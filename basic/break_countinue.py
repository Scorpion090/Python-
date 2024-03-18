# We use of break and countinue break exit the loop and continue skip the interation.

# break - 
num = int(input("Enter the nubmer here: "))
for i in range(num):
    if(i==4):
        print("Break the loop for i = 2")
        break
    print(i)
print("Thanks for using this loop!")

# continue - 
num2 = int(input("Enter the number here :"))
for i in range(num2):
    if(i==4):
        print("Skip the iteration for i = 2")
        continue
    print(i)
print("Also thanks for using this loop!")

# We can also use this with while loop - 
# break - 
n = int(input("Enter the number here :"))
i = 0
while(i < n):
    if(i == 2):
        print("Break the loop for i = 2")
        break
    print(i)
    i = i+1
print("Thanks for using this loop!")

# continue - 
n2 = int(input("Enter the number here: "))
i = 0
while(i < n2):
    if(i == 2):
        print("Skip the loop for i = 2")
        i = i + 1
        continue
    print(i)
    i = i + 1
print("Thanks for using this loop!")




