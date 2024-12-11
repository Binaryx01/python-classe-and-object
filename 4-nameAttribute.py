'''
Define a class Person with a name attribute.
Set the name of a person object to "Ishwor".
'''

class Person:
    def __init__(self, name):
        self.name = name
    def display(self):
        print(f"The name is {self.name}")

p1 = Person("Ishwor")
p1.display()

