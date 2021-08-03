class Mul:
    def __init__(self, strength: int, speed: int):
        self.strength = strength
        self.speed = speed

    def __str__(self):
        return (
            f"{self.__class__.__name__}:\n{{\n\tspeed: {self.speed}\n\tstrength: {self.strength}\n}}"
        )
