# Enumerate function -

l = [1,2,3,4,5,6,7,8,9,10]
for i in range(1,len(l)+1):
    print(i)

# i also want to print the index of this list then we can use of enumerate function  - 
for index,item in enumerate(l):
    print(index,item)
    