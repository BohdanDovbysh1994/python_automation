from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self):
        self.weels = 4
        self.dors = 4
        self.engine = True
        self.engine_type = None

    def move_forward(self):
        print("Moving forward")

    def stop(self):
        print("Stopping...")

    def turn_right(self):
        print("Turn right")

    def turn_left(self):
        print("Turn left")

    @abstractmethod
    def refuel(self):
        pass


class Hammer(Car):
    def __init__(self):
        super().__init__()
        self.engine_type = "Gas"

    def refuel(self):
        print("Gasoline flows...")


class Tesla(Car):
    def __init__(self):
        super().__init__()
        self.engine_type = "Electro"

    def refuel(self):
        print("Charging...")


if __name__ == '__main__':
    tesla_car = Tesla()
    hammer_car = Hammer()
    tesla_car.refuel()
    hammer_car.refuel()
