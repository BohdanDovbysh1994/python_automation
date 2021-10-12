from typing import List

from ..session import session
from ..models.test_result import TestResultModel
from ...test_result import TestResult


class TestResultRepository:
    def __init__(self):
        self.__session = session

    def save(self, test_results: List[TestResult]):
        results = []

        for result in test_results:
            results.append(
                TestResultModel(**result.to_dict())
            )

        self.__session.add_all(results)
        self.__session.commit()
