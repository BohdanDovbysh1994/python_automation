from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, salary: int, position: str):
        self.salary = salary
        self.position = position

    @abstractmethod
    def do_work(self):
        pass


class Pragrammer(Employee):
    def __init__(self):
        super().__init__("Programmer", 2000)

    def do_work(self):
        print("I am writing programs")


if __name__ == '__main__':
    john = Pragrammer()
    # john.do_work() # error not implemented method
    # john = Employee("manager", 2000) # Error
