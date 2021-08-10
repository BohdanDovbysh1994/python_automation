from lesson_15.proxy_pattern.reader import Reader
from lesson_15.proxy_pattern.writer import Writer


class CsvReaderWriter(Reader, Writer):
    def __init__(self, file_name: str):
        self.__file_name = file_name

    def read(self) -> str:
        with open(self.__file_name) as file:
            text = file.read()
        return text

    def write(self, text: str):
        with open(self.__file_name, "w") as file:
            file.write(text)
