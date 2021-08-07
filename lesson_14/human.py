class Human:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def __clean(self, item: str):
        pass

    def __str__(self):
        result = ""
        print(self.__class__.__dict__)
        for key, value in self.__dict__.items():
            result += f"{key}: {value}\n\t"
        return f"{{\n\t{result}}}"


if __name__ == '__main__':
    print(Human("john", 32))
