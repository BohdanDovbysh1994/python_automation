from datetime import datetime
from typing import List

from .employee import Employee


class Company:
    def __init__(
        self, name: str, address: str, date: datetime, industry: str
    ):
        self.__name = name
        self.__addresses: List[str] = self.__initiate_addresses(address)
        self.__registration_date = date
        self.__industry = industry
        self.__employees: List[Employee] = list()

    def __initiate_addresses(self, address: str) -> List[str]:
        return [address]

    def hire(self, employee: Employee):
        self.__employees.append(employee)

    @property
    def employees(self):
        return self.__employees
