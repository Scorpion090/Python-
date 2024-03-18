# Error handling in python programing language -
try:
    num = input("Enter the number here :")
    print(f"The multiplication table of {num} is ")

    for i in range(1,11):
        print(f"{int(num)} X {i} = {int(num)*i}")
    
except:
    print("please enter the correct value here:")
print("Thanks for using this program")


# We can handle multiple errors here:

try:
    num2 = int(input("Enter the number here:"))
    a = [3,4]
    print(a[num2])
except ValueError as e:
    print("Invalid input!")
except IndexError as e:
    print("Index Error")


