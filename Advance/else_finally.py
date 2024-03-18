try:
    l = [1,2,3,4]
    a = int(input("Enter the index here :"))
    print(l[a])
except:
    print("Invalid input so please enter the valid input for run this program!")

else:
    print("This is  else statement with try except!")
finally:
    print("This is always excute")

# We can use  of print statement on the space of finaly but if we use this statement inside the function then it will be not run : 

def func1():
    try:
        l = [1,2,3,4]
        a = int(input("Enter the index here :"))
        print(l[a])
        return 1
    except:
        print("Invalid input so please enter the valid input for run this program!")
        return 0
    print("May be this will be executed!") # finally definately work here:
x = func1()
print(x)
