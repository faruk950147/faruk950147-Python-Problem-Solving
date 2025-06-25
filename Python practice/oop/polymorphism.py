
class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def sound(self):
        print(f"{self.name} says Meow!")

class Cow(Animal):
    def sound(self):
        print(f"{self.name} says Moo!")

def animal_sound(animal):
    animal.sound()

if __name__ == "__main__":
    dog = Dog("Tommy")
    cat = Cat("Kitty")
    cow = Cow("Bessie")

    animals = [dog, cat, cow]

    for animal in animals:
        animal_sound(animal)


# class Shape:
#     def __init__(self, name):
#         self.name = name

# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__("Circle")
#         self.radius = radius
    
#     def area(self):
#         return 3.14 * self.radius * self.radius

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         super().__init__("Rectangle")
#         self.length = length
#         self.width = width
    
#     def area(self):
#         return self.length * self.width

# def shape_area(shape):
#     return shape.area()

# if __name__ == "__main__":
#     circle = Circle(5)
#     rectangle = Rectangle(4, 6)

#     shapes = [circle, rectangle]

#     for shape in shapes:
#         print(f"Area of {shape.name}:", shape_area(shape))
