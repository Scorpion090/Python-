# This is all about the for loop - 

n = int(input("Enter the number here :"))
for i in range(n):
    print(i)
    
# We can iterate the value of inside the list with the for loop  - 
names = ["Rohan","Rohit","Vishal","Kamal","Anil","Satish"]
for name in names:
    print(name)
    for item in name:
        print(item)
l = [1,2,3]
l2 = [1,2,3]
print(l is l2)
print(l==l2)

# Note - In simple terms, Python internally caches small integers and some other objects for efficiency. When you create a list like `l = [1, 2, 3]`, a new object is created each time. However, for small integers like `a = 9`, Python often uses the same object for efficiency. So, when you use `is` to compare lists, it checks if they are the exact same object in memory, but for integers, it may return `True` because Python sometimes reuses the same object for small integers. Use `==` for content comparison to ensure consistent results.

AA = 9
BB = 9
print(AA==BB)
print(AA is BB)

# print the multiplication table with the help of for loop - 
number = int(input("Enter the number here :"))
for i in range(1,11):
    print(number,"X ",i,"= " ,i*number)
    
    