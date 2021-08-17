import pytest


@pytest.mark.parametrize(
    "gender,expected", [("male", "male"), ("female", "female")], ids=["change_to_male", "change_to_female"]
)
def test_change_gender(human, gender, expected):
    human.change_gender(gender)

    assert human.gender == expected


def test_check_raise_of_exception_for_chenge_gender(human):
    with pytest.raises(Exception):
        human.change_gender("")
