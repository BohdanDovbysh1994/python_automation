class Cap:
    def __init__(self, level: float):
        self.level = level
        self.drink = None

    def fill(self, percent: float, drink: str) -> None:
        self.level = percent
        self.drink = drink


if __name__ == '__main__':
    my_cap = Cap(0.0)
    my_cap.fill(50.0, "Whisky")

    if my_cap.level == 50.0:
        my_cap.fill(20.0, "Ice")
