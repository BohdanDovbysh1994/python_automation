from .cat import Cat


class Lion(Cat):
    def __init__(self):
        super().__init__()

    def make_noise(self):
        super().make_noise()
        print("Rrrrrrrrrr")
