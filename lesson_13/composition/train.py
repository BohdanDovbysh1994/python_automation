from typing import List

from lesson_13.train.train_car import TrainCar


class Train:
    def __init__(self):
        self.__train_cars: List[TrainCar] = list()

    def add_train_car(self):
        self.__train_cars.append(
            TrainCar(1)
        )

    def __str__(self):
        return f"{[train_car.number for train_car in self.__train_cars]}"


if __name__ == '__main__':
    train = Train()
    train.add_train_car()