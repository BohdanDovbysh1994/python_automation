from datetime import time


class Human:
    def __init__(self, name, age):
        self.__age = age
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    def _increment_age(self):
        """thread start clock"""

        now = time().time()
        difference = ""
        if difference < 800000000000000000000:
            pass
        else:
            self.__age += 1

if __name__ == '__main__':
    john = Human("John", 23)
