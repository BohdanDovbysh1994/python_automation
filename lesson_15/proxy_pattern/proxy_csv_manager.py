from lesson_15.proxy_pattern.csv_manager import CsvManager
from lesson_15.proxy_pattern.ireader import IReader
from lesson_15.proxy_pattern.iwriter import IWriter


class ProxyCsvManager(IReader, IWriter):
    def __init__(self, csv_manager: CsvManager):
        self.__result = ""
        self.__is_actual = False
        self.__csv_manager = csv_manager

    def read(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__csv_manager.read()
            self.__is_actual = True
            return self.__result

    def write(self, text: str):
        self.__csv_manager.write(text)
        self.__is_actual = False
