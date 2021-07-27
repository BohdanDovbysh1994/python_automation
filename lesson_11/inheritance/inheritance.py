class Human:
    def __init__(self, name: str, age: int, gender: bool):
        self.name = name
        self.age = age
        self.gender = gender

    def think(self):
        print("I think like a simple Human")


class Employee(Human):
    def __init__(self, name: str, age: int, gender: bool, salary: int, position: str):
        super().__init__(name, age, gender)
        self.salary = salary
        self.position = position

    def think(self):
        """
            Provide basic logic from Human and additional logic
        """

        super().think()
        print("Also I additionally think like engineer=)")


if __name__ == '__main__':
    john = Employee("John", 23, True, 1500, "Manager")
    john.think()
