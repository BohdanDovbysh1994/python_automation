from .mul import Mul


class Horse:
    def __init__(self):
        self.speed = 5
        self.age = 5

    def __add__(self, other) -> Mul:
        return Mul(other.strength, self.speed)

    def __str__(self):
        return (
            f"{self.__class__.__name__}:"
            f"\n{{\n\tspeed: {self.speed}\n\t"
            f"age: {self.age}\n}}"
        )

    def __radd__(self, other) -> Mul:
        return Mul(other.strength, self.speed)

    def __iadd__(self, other):
        self.age += other.age
        return self

    def __bool__(self):
        return False

    def __float__(self):
        return 1.5

    def __eq__(self, other):
        return self.age == other.age
