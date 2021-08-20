import pytest

from lesson_16.human import Human, Action


@pytest.fixture
def action() -> Action:
    yield Action("dancing")


@pytest.fixture
def human(action) -> Human:
    yield Human("John", 32, "male", action)
