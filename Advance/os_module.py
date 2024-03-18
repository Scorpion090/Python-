# This is operating system (O.S.) module - 
import os

if(not os.path.exists("Main")):
    os.mkdir("Main")

# Create a file inside the main folder - 
file_path = os.path.join("Main","Hello.py")
print(file_path)

with open("Hello.py", "w") as f:
    f.write("print('This is the content of main file')")

# Read of the file which you have created - 
with open("Hello.py", "r") as f:
    print(f.read())

