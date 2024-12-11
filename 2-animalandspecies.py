'''

Create a class Animal with an attribute species.
 Create an object and set species to "Dog" and make it woof sound as well
'''

class Animal:
    def __init__(self,species):
        self.species = species

    def speak(self):
        print(f"The given animal make sound as {self.species}")

    def display(self):
        if self.species.lower == "dog":
            print(f"The given animal produces woof sound")
        else:
            print(f"The given animal makes sound as woof {self.species} sound")


a1 = Animal("Dog")

a1.display()
a1.speak()