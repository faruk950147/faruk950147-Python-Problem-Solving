# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         raise NotImplementedError("Subclass must implement 'area' method")
#     @abstractmethod
#     def perimeter(self):
#         raise NotImplementedError("Subclass must implement 'perimeter' method")

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement 'area' method")

    def perimeter(self):
        raise NotImplementedError("Subclass must implement 'perimeter' method")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


r = Rectangle(10, 5)
print("Rectangle Area:", r.area())
print("Rectangle Perimeter:", r.perimeter())

c = Circle(7)
print("Circle Area:", c.area())
print("Circle Perimeter:", c.perimeter())

