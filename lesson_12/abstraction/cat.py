from abc import ABC, abstractmethod


class Cat(ABC):
    def __init__(self):
        self.color = None
        self.tail = None
        self.legs = 4
        self.hungry = 5

    @abstractmethod
    def make_noise(self):
        pass

    def eat(self):
        if self.hungry > 0:
            self.hungry -= 1
