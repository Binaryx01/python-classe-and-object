'''
Create a class Circle with an attribute
radius and initialize it using the constructor. and
Add a method area() in Circle to calculate and return the area (πr²).
Add a method area() in Circle to calculate and return the area (πr²).

'''
import  math

class Circle:
    def __init__(self,radius):
        self.radius= radius

    def display(self):
        print(f"the radius is{self.radius}")

    def calculate(self):
        return math.pi * (self.radius*self.radius)


c1 = Circle(25)
c1.display()
print(f"The area is {c1.calculate()}")

