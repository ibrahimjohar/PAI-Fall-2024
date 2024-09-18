from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

rectangle = Rectangle(4, 5)
triangle = Triangle(3, 6)
square = Square(4)

print("Rectangle area:", rectangle.area())
print("Triangle area:", triangle.area())
print("Square area:", square.area())