# Set - Set is collection of well define objects.Sets items are unchangable and do not allow duplicate values and set is a unordered collection of items . Order doesen't maintan.

s = {2,4,2,6}
print(s)
print(type(s))  

# We can't change the vlaue of set  - 
# s[0] = 9
# print(s)

# We can store multiple data types value inside the set - 
t = {"Rohan Rathore",True,33,44,2,7}
print(t)
print(type(t))

Rohan = {}
print(type(Rohan))   # Return the type is <class dict>

Rohit = set()
print(type(Rohit))   # Return the type is <class set>

# We can access of the set items with the help of for loop - 
for items in t:
    print(items)


