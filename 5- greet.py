'''
Add a method greet() in Person class to print "Hello, [name]!".
'''
class Person:
    def __init__(self,name):
        self.name = name
    def greet(self):
        print(f"Hello{self.name}")

p1 = Person("Ishwor")
p1.greet()

