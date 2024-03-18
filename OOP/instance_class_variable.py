# This is all about the istance vs class/ global variable - 

class Employee:
    company = "Apple"   # This is a class variable .
    def __init__(self,name):
        self.name = name             # Here self.name and self.raise_amount is a instance Variable. 
        self.raise_amount = 0.2
    def showDetails(self):
        print(f"The name is {self.name} and the raise_amount is {self.raise_amount} and the company name is {self.company}")

a = Employee("Rohan")
a.company = "Apple India"   # We can make change this - 
a.raise_amount = 9.5
a.showDetails()
b = Employee("Harry")   #We can make change this - 
b.company = "Apple USA"
Employee.showDetails(b)



