from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def area(self):
        return math.pi * 5 * 5


class Rectangle(Shape):
    def area(self):
        return 10 * 5


class Triangle(Shape):
    def area(self):
        return 0.5 * 10 * 6


shapes = [Circle(), Rectangle(), Triangle()]

for shape in shapes:
    print("Area =", shape.area())