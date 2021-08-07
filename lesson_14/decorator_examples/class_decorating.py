from lesson_14.decorator_examples.hobbi_decorator import Hobby


@Hobby("Dancing")
class Human:
    def __init__(self):
        self.__name = "John"
        self.__age = 32

    @property
    def name(self):
        return self.__name


if __name__ == '__main__':
    john = Human()
    print(john)
    [str(item) for item in range(5)]
    print()
