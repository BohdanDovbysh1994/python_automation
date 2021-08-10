from abc import ABC


class Browser(ABC):
    _name: str = ""

    def __init__(self):
        self.__history = []

    @property
    def history(self):
        return self.__history
