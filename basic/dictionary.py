# dictionary  is a combination of key and value pairs.Dictionary is a orederd collection of data items then can store multiple data types of values .

dict = {
    "name":"Rohan Rathore",
    "From":"Indore"
}
print(dict)
print(dict["name"])
print(dict["From"])

# We can use of dictionary in our real life -
d = {
    1 : "Rohan",
    2 : "Rohit",
    3 : "Sohan",
    4 : "Danish"
}
print(d[1])
print(d[2])
print(d[4])


# If you don't want to error in your program  then you can do this - 
info = {
    "Name":"Rohan Rathore",
    "College":"Sage university Indore",
    "Marks":80
}
# print(info["Name2"])    throug the error.
print(info.get("Name2"))   # Successfully will run this program.

# Access all the keys and values - 
print(info.keys()) 
print(info.values())

for key in info.keys():
    print(f"The value of dictionary corresponding of {key}  is {info[key]}")
    
for value in info.values():
    print(value)

    
print(info.items())
for key,value in info.items():
    print(f"The value of dictionary corresponding of {key}  is {value}")
    