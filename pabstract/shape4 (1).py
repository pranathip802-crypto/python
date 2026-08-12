from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    def display_shape(self):
        print("This is a geometric shape")


class Circle(Shape):

    def area(self):
        return 78.5


circle = Circle()

print("Area =", circle.area())
circle.display_shape()