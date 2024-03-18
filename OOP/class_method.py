class Person:
    company = "Apple"
    def __init__(self,name):
        self.name = name
        
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")
    
    @classmethod
    def changeCompany(self,Rohan):
        self.company = Rohan
    
a = Person("Rohan")
a.show()
a.changeCompany("Tesla")
a.show()
print(Person.company)
