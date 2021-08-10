from lesson_15.proxy_pattern.ireader import IReader
from lesson_15.proxy_pattern.iwriter import IWriter


class CsvManager(IReader, IWriter):
    def __init__(self, file_name: str):
        self.__file_name = file_name

    def read(self) -> str:
        with open(self.__file_name) as file:
            text = file.read()
        return text

    def write(self, text: str):
        with open(self.__file_name, "a") as file:
            file.write(text)
