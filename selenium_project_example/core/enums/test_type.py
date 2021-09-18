from enum import Enum, unique


@unique
class TestType(Enum):
    UI = 0
    API = 1
