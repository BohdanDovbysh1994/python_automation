from lesson_12.interfaces.Itransport import ITransport
from lesson_12.interfaces.iflyable import IFlyable


class Helicopter(IFlyable, ITransport):
    def __init__(self):
        self.__number_of_doors = 4
        self.__number_of_rotors = 2
        self.__number_of_blades = 3
        self.__engine_status = False
        self.__x = 0
        self.__y = 0
        self.__z = 0
        self.__health = 100
        self.__is_on_land = True

    def fly(self):
        pass

    def nosedive(self):
        pass

    def take_off(self):
        pass

    def land(self):
        pass

    def start_engine(self):
        self.__engine_status = True

    def move(self, direction: str, distance: int):
        if direction == "up":
            self.__z += distance
            if self.__is_on_land:
                self.__is_on_land = False
        elif direction == "down":
            if self.__z > 0:
                self.__z -= distance
        elif direction == "right":
            self.__x += distance
        elif direction == "left":
            self.__x -= distance
        elif direction == "forward":
            self.__y += distance
        elif direction == "back":
            self.__y -= distance
        else:
            pass

    def stop_engine(self):
        self.__engine_status = False
        if not self.__is_on_land:
            self.nosedive()

    @property
    def engine_status(self):
        return self.__engine_status

    def get_coordinates(self) -> tuple:
        return self.__x, self.__y, self.__z
