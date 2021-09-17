from requests import Response, get

from app import config


class PeopleService:
    def __init__(self):
        self.__people_url = f"{config['host']}/people"

    def get_person(self, id: int) -> Response:
        return get(f"{self.__people_url}/{id}")
