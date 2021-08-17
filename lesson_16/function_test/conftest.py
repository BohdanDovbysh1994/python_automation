import pytest

from lesson_16.code_for_testing import Human, Action


@pytest.fixture
def action() -> Action:
    yield Action("dancing")


@pytest.fixture
def human(action) -> Human:
    yield Human("John", 32, "male", action)
