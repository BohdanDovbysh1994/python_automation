from __future__ import annotations

from lesson_15.singleton_pattern.scooter_singleton import singleton


@singleton
class Scooter:
    def __init__(self, color: str, wheel_size: int):
        self.__color = color
        self.__wheel_size = wheel_size
        self.__electro = False


if __name__ == '__main__':
    scooter_1 = Scooter("Yellow", 23)
    scooter_2 = Scooter("Red", 50)
    print()
