# This is all about the if and else statement - 
num = int(input("Enter the number her: "))
if(num == 0):
    print("This is the number one")
elif(num<8):
    print("This number is less than 8")
elif(num>8):
    print("This number is greater than 0")
else:
    print("This is a negative number")



# let's take the another example - 
age = int(input("Enter the your age here: "))
if(age==0):
    print("First you should to take birth")
elif(age>=1 and age<=17):
    print("You can not drive")
else:
    print("You can drive the car easily")
    
    
# This is the program of nested if and else statement - 
age = int(input("Enter the your age here:"))
if(age>=18):
    print("you are an Adult")
    
    # Nested if-else statement - 
    if(age>=21):
        print("You are also eligible to vote!")
    else:
        print("You can't vote  because you are still an adult!")
else:
    print("You are not an Adult!")

# This is the another example of if-else statement related to daily life - 
apple_price = int(input("Enter the apple price here: " ))
budget = int(int(input("Enter the your budget here :")))
if(budget - apple_price > 50):
    print("Hey! Alexa you can add one kg apple to the cart")
elif(budget - apple_price > 70):
    print("Okay! you can buy apples")
else:
    print("Hey! Alexa do not add apples to the cart!")

# There is a another example - 
num = int(input("Enter the value of number here :"))
if(num<0):
    print("Thisi is the first negative number")
elif(num>0):
    print("This is the positive number")
elif(num==-1):
    print("This is the second negative number :")

print("This code will be always run because this code is out of indentation!")
