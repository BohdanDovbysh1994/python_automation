import pytest

from entities.person import Person
from infrastructure.people_service import PeopleService


@pytest.fixture(scope="session")
def people_service() -> PeopleService:
    yield PeopleService()


@pytest.fixture
def first_person():
    yield Person(
        name="Luke Skywalker",
        height="172",
        mass="77",
        hair_color="blond",
        skin_color="fair",
        eye_color="blue",
        birth_year="19BBY",
        gender="female",
    )
