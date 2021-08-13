from lesson_13.train.passenger import Passenger


class TrainCar:
    def __init__(self, number: int):
        self.__number = number
        self.__passengers = list()

    def __str__(self):
        result = "[\n"

        for passenger in self.__passengers:
            result += f"\t{passenger}"

        return result + "\n]"

    def add_passenger(self, passenger: Passenger):
        self.__passengers.append(passenger)

    @property
    def number(self):
        return self.__number
