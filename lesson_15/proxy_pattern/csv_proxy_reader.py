from lesson_15.proxy_pattern.csv_reader import CsvReaderWriter
from lesson_15.proxy_pattern.reader import Reader
from lesson_15.proxy_pattern.writer import Writer


class CsvProxyReaderWriter(Reader, Writer):
    def __init__(self, csv_reader_writer: CsvReaderWriter):
        self.__result = ""
        self.__is_actual = False
        self.__reader_writer = csv_reader_writer

    def read(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__reader_writer.read()
            self.__is_actual = True
            return self.__result

    def write(self, text: str):
        self.__reader_writer.write(text)
        self.__is_actual = False
