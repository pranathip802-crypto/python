
from abc import ABC, abstractmethod

class Food(ABC):

    @abstractmethod
    def prepare(self):
        pass


class Pizza(Food):
    def prepare(self):
        print("Preparing Pizza")


class Burger(Food):
    def prepare(self):
        print("Preparing Burger")


pizza = Pizza()
burger = Burger()

pizza.prepare()
burger.prepare()