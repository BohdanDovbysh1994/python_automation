class Engine:
    def __init__(self):
        pass


class Car:
    def __init__(self):
        self.__engine = Engine()


if __name__ == '__main__':
    car = Car()
