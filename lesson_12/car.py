class Car:
    def __init__(self):
        self.__doors = 4
        self.__color = "Yellow"

    @property
    def doors(self):
        return self.__doors

    @doors.deleter
    def doors(self):
        del self.__doors

    def modify_doors(self, value):
        self.__doors = value


if __name__ == '__main__':
    car = Car()

