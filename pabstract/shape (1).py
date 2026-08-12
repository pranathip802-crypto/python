from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):

    def area(self):
        length = 10
        width = 5
        print("Rectangle Area =", length * width)

    def perimeter(self):
        length = 10
        width = 5
        print("Rectangle Perimeter =", 2 * (length + width))


class Circle(Shape):

    def area(self):
        radius = 5
        print("Circle Area =", math.pi * radius * radius)

    def perimeter(self):
        radius = 5
        print("Circle Perimeter =", 2 * math.pi * radius)


rectangle = Rectangle()
circle = Circle()

rectangle.area()
rectangle.perimeter()

circle.area()
circle.perimeter()