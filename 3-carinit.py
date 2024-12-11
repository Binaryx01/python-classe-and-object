'''

Create a class Car with attributes brand and model.
 Initialize them using the _*init*_ method.
Create an object of Car class and print its attributes.
Create an object of Car class and print its attributes.

'''

class Car:
    def __init__(self,brand,model):
        self.brand= brand
        self.model=model
    def display(self):
        print(f"the model of the car is {self.model} the brand of the car is {self.brand}")


c1 = Car("Toyota","Z5")
c1.display()

