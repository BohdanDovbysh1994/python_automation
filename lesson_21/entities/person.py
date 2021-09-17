from __future__ import annotations


class Person:
    def __init__(
        self,
        name,
        height,
        mass,
        hair_color,
        skin_color,
        eye_color,
        birth_year,
        gender,
    ):
        self.name = name
        self.height = height
        self.mass = mass
        self.hair_color = hair_color
        self.skin_color = skin_color
        self.eye_color = eye_color
        self.birth_year = birth_year
        self.gender = gender

    def __eq__(self, other: Person):
        return self.__dict__ == other.__dict__
