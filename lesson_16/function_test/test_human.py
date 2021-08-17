import os

import pytest


@pytest.mark.smoke
@pytest.mark.slow
def test_check_gender_after_change_from_male(human):
    human.change_gender("female")

    assert human.gender == "female"


@pytest.mark.smoke
@pytest.mark.fast
def test_check_gender_after_change_from_male_01(human):
    human.change_gender("female")

    assert human.gender == "female"


@pytest.mark.xfail(reason="Failes due to existing bug", condition=True)
def test_check_gender_after_change_from_female(human, monkeypatch):
    monkeypatch.setattr(
        human, "_Human__gender", "female"
    )
    human.change_gender("male")

    assert human.gender == "female"


@pytest.mark.skip("this test will be skipped")
def test_check_gender_after_change_from_female_1(human, monkeypatch):
    monkeypatch.setattr(
        human, "_Human__gender", "female"
    )
    human.change_gender("male")

    assert human.gender == "female"
