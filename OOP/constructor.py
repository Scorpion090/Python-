# Constructor  - We use of constructor in python for taking the value on the run time.

class First:
    def __init__(self,name,city):   # This is parameterised constructor - 
        self.name = name
        self.city = city
    def info(self):
        print(f"Your name is {self.name} and your city is {self.city}")
a = First("Rohan Rathore","Indore")
b = First("Vishal Malviya","Dewas")
a.info()
b.info()


"""
There are two types of constructors - 
1. Parameterised constructor - (Pass the parameter)
2. Default constructor -     ( Default value which takes only self )

"""