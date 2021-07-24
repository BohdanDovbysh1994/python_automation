class Human:
    __addresses = []

    def __init__(
        self,
        name: str = None,
        age: int = None,
        salary: int = None,
        # address: str = None,
        gender: bool = None,
    ):
        self.name = name
        self.age = age
        self.salary = salary
        # self.address = address
        self.gender = gender

    def get_name(self):
        return self.name

    def update_name(self, name):
        self.name = name

    @classmethod
    def from_name_and_age(cls, name, age):
        return cls(name, age)

    @classmethod
    def add_address(cls, address: str):
        cls.__addresses.append(address)

    @classmethod
    def get_addresses(cls):
        return cls.__addresses

    @staticmethod
    def calculate_bonus(salary, overtime):
        rate = salary / 160
        return rate * 2 * overtime


if __name__ == '__main__':
    # print(john.calculate_bonus(1500, 23))
    Human.add_address("Backer street")
    john = Human.from_name_and_age("John", 32)
    print(Human.get_addresses())
    print(john.get_addresses())
