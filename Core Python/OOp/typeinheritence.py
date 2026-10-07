class Animal:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def display(self):
        print("Name :", self.name)
        print("Color :", self.color)
        print("Age :" , self.age) 

class Dog(Animal):
    pass    

d1 = Dog("Rani", "Black", 10)
d1.display()
        