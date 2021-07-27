class Donkey:
    def __init__(self):
        self.strength = 100
        

class Horse:
    def __init__(self):
        self.speed = 200


class Mul(Donkey, Horse):
    def __init__(self):
        Donkey.__init__(self)
        Horse.__init__(self)


if __name__ == '__main__':
    mul = Mul()

    print(mul.strength)
    print(mul.speed)
