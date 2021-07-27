class Human:
    def __init__(self):
        self.name = "John"
        self.age = 32
        self.beet_counter = 0

    def __hurt_beet(self):
        print("Hurt is betting...")
        self.beet_counter += 1

    def death(self):
        if self.beet_counter == 1000:
            del self

    def live(self):
        self.__hurt_beet()

    def eat(self):
        print("I am eating")


if __name__ == '__main__':
    john = Human()
    john.eat()
