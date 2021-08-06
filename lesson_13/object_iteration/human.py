class Human:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__gender = gender
        self.__age = age

    def __iterate(self) -> dict:
        data = dict()
        for key, value in self.__dict__.items():
            if not key.startswith("_") and not callable(value):
                data[key] = value
        return data
