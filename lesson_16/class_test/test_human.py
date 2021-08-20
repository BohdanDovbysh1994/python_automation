import pytest

from lesson_16.human import Human


class TestHuman:
    def setup_class(self):
        self.human = Human("John", 32, "male")

    def setup(self):
        print("Setup for each test")

    def test_check_grow_method(self):
        self.human.grow()

        assert self.human.age == 33

    def test_change_gender_method(self):
        self.human.change_gender("female")

        assert self.human.gender == "female"

    def test_check_gender_after_initialization(self):
        assert self.human.gender == "male"

    def teardown(self):
        print("Teardown for each test")

    def teardown_class(self):
        pass
