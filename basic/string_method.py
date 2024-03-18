# This is all about the string methods- 
# Strings are immutable data type in python we can't change the origional strings we can only create a copy of origional string.

a = "Rohan Rathore !!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))  # only end exclamation marked remove not starting.
print(a.replace("R","S"))
print(a.split(" "))   # Convert the strings into the list.
print(a.capitalize())

str1 = "Welcome to the AI Wallah"
print(len(str1))
print(str1.center(50))
print(len(str1.center(50)))
print(str1.count("Welcome"))
print(a.endswith("!!"))
print(a.endswith("n",2,5))
print(a.find("Rathore")) # It will throw an error if string is not find.
print(a.index("Rathore")) # it will direct throw an Erro if string is not find.

str2 = "welcome\n  Rohan Rathore"
print(str2.isalnum())
print(str2.isalpha())
print(str2.islower())
print(str2.isupper())
print(str2.isprintable())
print(str2.isspace())
print(str2.istitle()) # it will return true if the your string is capital letter othewise it will return false.
print(str1.startswith("Welcome"))

Story = "Chandana used to get up early in the morning complite her house hold in the two work for long"
print(Story.swapcase())
print(Story.title()) 









