import pytest

from lesson_16.human import Human


@pytest.fixture
def human() -> Human:
    yield Human("John", 32, "male")
