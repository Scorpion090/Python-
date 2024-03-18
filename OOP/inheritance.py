# Inheritance - Consume the one class properties and methods into the other class is called inheritance.

class first:
    def father(self):
        print("This is the first class")
class second(first):
    def brother(self):
        print("This is the second class")
class third(second):
    def myself(self):
        print("This is the third class")

a = third()
a.myself ()
a.brother()

