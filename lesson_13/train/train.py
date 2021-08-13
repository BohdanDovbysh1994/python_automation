from typing import List

from lesson_13.train.train_car import TrainCar


class Train:
    def __init__(self):
        self.__train_cars: List[TrainCar] = list()

    def add_train_car(self, train_car: TrainCar):
        self.__train_cars.append(train_car)

    def __str__(self):
        result = "<=[HEAD]"

        for train_car in self.__train_cars:
            result += f"-[{train_car.number}]"

        return result
