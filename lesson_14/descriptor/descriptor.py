from typing import Type


class Column:
    def __init__(self, name: str, column_type: Type):
        self.__name = name
        self.__column_type = column_type
        self.__value = None

    def __set__(self, instance, value):
        self.__value = value

    def __get__(self, instance, owner):
        return self.__value


class Table:
    id = Column("id", str)
    name = Column("name", str)


table = Table()
table.id = "1"
table.name = "John Dow"
print(table.id)
print(table.name)
