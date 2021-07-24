class Human:
    addresses = []
    salary = None
    # --------------------
    TYPE = "Employee"

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name


john: Human = Human("John", 32)
marta: Human = Human("Marta", 24)
john.addresses.append("Backer str.")

print(john.addresses)
print(marta.addresses)
marta.addresses.append("Some")

print(john.addresses)
print(marta.addresses)

Human.addresses.append("Some2")

print(john.addresses)
print(marta.addresses)

john.salary = 1500
print(john.salary)
print(marta.salary)

Human.salary = 2000

print(john.salary)
print(marta.salary)
