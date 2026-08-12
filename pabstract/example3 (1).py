
from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def area(self):
        radius = 5
        result = math.pi * radius * radius
        print("Area of Circle =", result)


class Rectangle(Shape):
    def area(self):
        length = 10
        width = 5
        result = length * width
        print("Area of Rectangle =", result)


circle = Circle()
rectangle = Rectangle()

circle.area()
rectangle.area()