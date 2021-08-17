class Action:
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        return self.__name


class Human:
    def __init__(self, name: str, age: int, gender: str, action: Action):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__action = action

    def grow(self):
        self.__age += 1

    def change_gender(self, gender: str):
        if gender not in ["male", "female"]:
            raise Exception("Not correct name of gender")
        self.__gender = gender

    @property
    def age(self) -> int:
        return self.__age

    @property
    def gender(self):
        return self.__gender

    @property
    def action(self):
        return self.__action
