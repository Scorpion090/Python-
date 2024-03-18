# With the help of list methods we can manupulate of list items -

l = [1,2,3,4,5,6,7,9,8,10]
print(l)

# Add the element in the list - 
l.append(11)
print(l)

# sort method of list - 
l.sort()
print(l)

# Again convert the list in the same format - 
l.sort(reverse = True)
print(l)

l.reverse()
print(l)

# index method of the list - 
print(l.index(1))
print(l.index(2))
print(l.index(3))

# count method of the list -
print(l.count(1))

# This  is the concept of copy and view - 
print(l)
m = l.copy()
m[0] = 0
print(m)
print(l)

# Insert method of the list - 
l.insert(0,1333)
print(l)

# This is the extend method of the list which is used to combine of two list - 
ll = [900,1000,1100]
l.extend(ll)
print(l)


