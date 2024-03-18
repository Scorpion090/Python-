class Person:
    def __init__(self, name,std):
        self.name = name
        self.std = std
        
    def info(self):
        print(f"The name is {self.name} and the your class is {self.std}")
    
    @staticmethod
    def add(a,b):  # We can also access this with the help of static method without using of self keyword.
        return a + b
a = Person("Rohan Rathore","b-tech")
a.info()
Person.info(a)
result = a.add(2,3)
print(result)

