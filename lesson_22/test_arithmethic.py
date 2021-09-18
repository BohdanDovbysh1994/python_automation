import pytest


def test_check_2_plus_2():
    assert 2 + 2 == 4


def test_check_2_multiply_2():
    assert 2 * 2 == 6


@pytest.mark.skip()
def test_skip():
    pass
