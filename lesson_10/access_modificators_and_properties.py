class Human:
    def __init__(self, name: str, age: 32):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        self.__name = new_name


if __name__ == '__main__':
    john = Human("John", 32)
    print(john.name)
    john.name = "Marta"
    print(john.name)
