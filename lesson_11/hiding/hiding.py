from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, salary: int, position: str):
        self.salary = salary
        self.position = position

    @abstractmethod
    def do_work(self):
        pass


class Engineer(Employee):
    def __init__(self):
        super().__init__("Engineer", 2000)

    def _deploy_program(self):
        print("Deploying...")

    def __create_new_framework(self):
        print("Creating new framework...")

    def __create_infrastructure(self):
        print("Creating new infrastructure...")

    def deploy(self):
        """Deploy infrastructure after build app"""

        self.__create_new_framework()
        self.__create_infrastructure()


class Developer(Engineer):
    def __init__(self):
        super().__init__()

    def do_work(self):
        print("I am writing programs by means of framework")
        self._deploy_program()


if __name__ == '__main__':
    john = Developer()
    # john.do_work()
    john.deploy()
