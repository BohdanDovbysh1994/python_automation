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


dogs = Shepard(), Mops()


class DogFactory:
    def get_dog(self, breed_name: str) -> Dog:
        for dog in dogs:
            if breed_name == dog.breed:
                return dog
