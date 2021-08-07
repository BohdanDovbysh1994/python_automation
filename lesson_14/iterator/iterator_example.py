class CustomIterator:
    def __init__(self, sequence: list):
        self.__sequence = sequence
        self.__current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current < len(self.__sequence):
            item = self.__sequence[self.__current]
            self.__current += 1
            return item
        else:
            raise StopIteration


if __name__ == '__main__':
    custom_iterator = CustomIterator([1, 2, 3, 4, 5, 6])
    iterator = iter(custom_iterator)
    for item in custom_iterator:
        print(item)
