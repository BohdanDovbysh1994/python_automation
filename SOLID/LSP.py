from abc import ABC, abstractmethod


class Dog(ABC):
    def __init__(self):
        self._legs = 4

    @property
    @abstractmethod
    def tail_length(self):
        pass


class Mops(Dog):
    def __init__(self):
        super().__init__()
        self._size = "Small"
        self._drooling = 5
        self._tail_length = 2
        self._breed_name = "Mops"

    @property
    def tail_length(self):
        return self._tail_length

    @property
    def breed(self):
        return self._breed_name


class Shepard(Dog):
    def __init__(self):
        super().__init__()
        self._size = "Big"
        self._drooling = 3
        self._tail_length = 5
        self._breed_name = "Shepard"

    @property
    def tail_length(self):
        return self._tail_length

    @property
    def breed(self):
        return self._breed_name


if __name__ == '__main__':
    def get_dog_info(dog: Dog):
        return dog.tail_length

    for dog in Mops(), Shepard():
        print(get_dog_info(dog))