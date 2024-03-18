# This is all about the decorator.
# Creating the decorators function from here:

def dec(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this function")
    return mfx

# @dec
def rohan():
    print("What is this here")

rohan()

# Apply the decorator without extra parentheses
dec(rohan)()



# Here this is the other example:
def ow(name):
    def mfx(*args, **kwargs):    
        print("Good Morning bruh!")
        name(*args, **kwargs)
        print("Thanks for using this code:")
    return mfx
@ow
def name(Rani,city):
    print(f"The name is = {Rani} and the city is  = {city}")
name("Rohan","Indore")
# *args` allows a function to accept any number of positional arguments:
# **kwargs` allows it to accept any number of keyword arguments in Python.