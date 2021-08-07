class Hobby:
    def __init__(self, name: str):
        self.__name = name

    def __call__(self, _class):
        _class._Human__hobby = self.__name
        return _class
