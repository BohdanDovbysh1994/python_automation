from .cat import Cat


class Tiger(Cat):
    def __init__(self):
        self.__color = "Tricolor"
        self.__tail = "Long"
        self.__legs = 4

    def make_noise(self):
        print("rhrhrhrhrh")
