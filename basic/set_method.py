s = {1,2,3,5,6}
s2 = {4,5,6,7}

# union of the set - 
print(s.union(s2))   # Return the union of the set - 
# s.update(s2) # Update the value of set 2 in set a .
# print(s)

# intersection of the set - 
print(s.intersection(s2)) # Return the intersection of the set.
s.intersection_update(s2) # intersection  update of the set values - 
print(s)

# Symmetric difference between two sets - Those values which is not common in two sets - 
print(s)
print(s2)
# print(s.symmetric_difference(s2)) # Symmetric difference - 
print(s.difference(s2)) 

