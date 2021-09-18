from typing import Tuple


class Locator:
    def __init__(self, method: str, path: str):
        self.__method = method
        self.__path = path

    @property
    def method(self):
        return self.__method

    @property
    def path(self):
        return self.__path

    def to_tuple(self) -> Tuple[str, str]:
        return self.__method, self.__path
