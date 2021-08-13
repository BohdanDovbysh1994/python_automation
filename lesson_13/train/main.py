from lesson_13.train.passenger import Passenger
from lesson_13.train.train import Train
from lesson_13.train.train_car import TrainCar

# passenger_1 = Passenger("John Dow", 5, "Kharkov", "Moscow")
# train_car_1 = TrainCar(1)
# train_car_1.add_passenger(passenger_1)
train = Train()
train_cars = TrainCar(1), TrainCar(2), TrainCar(4), TrainCar(3), TrainCar(5),
[train.add_train_car(train_car) for train_car in train_cars]
del train
# print(train)
print(train_cars)

# print(train_car_1)