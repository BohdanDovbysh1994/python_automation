class Human:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def __clean(self, item: str):
        pass

    def __str__(self):
        result = ""
        for key, value in self.__dict__.items():
            result += f"{self.__clean(key)}: {value}\n\t"
        return f"{{\n\t{result}}}"
