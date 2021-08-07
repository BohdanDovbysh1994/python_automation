class File:
    def __init__(self, file_name: str, mode: str):
        self.__file_name = file_name
        self.__mode = mode
        self.__io_wrapper = None

    def read(self) -> str:
        return self.__io_wrapper.read()

    def __enter__(self):
        self.__io_wrapper = open(self.__file_name, self.__mode)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__io_wrapper.close()


if __name__ == '__main__':
    with File("text", "r") as file:
        print(file.read())
