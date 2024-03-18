'''String - 
        String is a data type in python inclosed in single quotes or double quotes
'''
name = input("Enter the your name here: ")
print("My name is " + name)

apple = "He want\'s to eat an apple"
print(apple)

# you can also use of double code in your string - 
print("Here\"s you  can see this is a double code in your string " )

# You can also use of \n in your string - 
print("Hey!\nGood Morning\nWhat's up!\n")

# Other method to do this - 
story = '''Hey!
Good Morning
What's up!
'''
print(story)

# We can access the index value of the string - 
n = "Rohan"
print(n[0])
print(n[1])
print(n[2])
print(n[3])
print(n[4])
# print(n[5])  You will get an Error because string indexcing our or range.

# you can also get the string individual value like this - 
print(n[:3])     # here first is including and last is excluding.

# for loop with strings - 
print("Let's use a for loop!")
for i in story:
    print(i)
    
# We can also use of this with other - 
n = "Rohan"
for item in n:
    print(item)
    

