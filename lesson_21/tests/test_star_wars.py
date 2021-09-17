from entities.person import Person


def test_check_person_01(people_service):
    response = people_service.get_person(1)

    assert response.json()["name"] == "Luke Skywalker"


def test_check_person_02(people_service):
    response = people_service.get_person(1)
    keys = ["name", "height"]

    assert all(key in response.json() for key in keys)


def test_check_person_03(people_service, first_person):
    response = people_service.get_person(1)
    actual_person = Person(
        response.json()["name"],
        response.json()["height"],
        response.json()["mass"],
        response.json()["hair_color"],
        response.json()["skin_color"],
        response.json()["eye_color"],
        response.json()["birth_year"],
        response.json()["gender"],
    )
    assert actual_person == first_person
