'''
2. Intermediate

Create a class Student with:

    Attributes: name, grade
    A method get_grade that returns "Pass" if the grade is
    greater than or equal to 40; otherwise, it returns "Fail".
    Create an object of Student with any name and grade and print
     whether the student passed or failed using the method
'''
class Car:
    def __init__(self,brand,model):
        self.brand= brand
        self.model=model
    def display(self):
        print(f"car name is {self.brand} and model is{self.model}")

c1 = Car("tesla","g15")
c1.display()
