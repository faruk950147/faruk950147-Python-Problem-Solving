class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(self.name, self.age)

p1 = Person("Faruk", 22)
p1.display()