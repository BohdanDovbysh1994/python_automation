from __future__ import annotations

from datetime import datetime
from typing import List

from _pytest.reports import TestReport

from .enums.test_type import TestType


class TestResult:
    def __init__(
        self,
        name: str,
        result: str,
        date_created: datetime,
        type: TestType,
        duration: float,
        log: str,
        std_error: str,
        std_out
    ):
        self.name = name
        self.result = result
        self.date_created = date_created
        self.type = type
        self.duration = duration
        self.log = log
        self.std_error = std_error
        self.std_out = std_out

    @classmethod
    def from_test_reports(cls, results: List[TestReport], test_type: TestType) -> List[TestResult]:
        test_reports = []
        for result in results:
            test_reports.append(cls.from_test_report(result, test_type))

        return test_reports

    @classmethod
    def from_test_report(cls, result: TestReport, test_type: TestType) -> TestResult:
        return cls(
            name=result.head_line,
            result=result.outcome,
            date_created=datetime.now(),
            type=test_type,
            duration=result.duration,
            log=result.caplog,
            std_error=result.capstderr,
            std_out=result.capstdout,
        )

    def to_dict(self):
        data = dict()

        for key, value in self.__dict__.items():
            if isinstance(value, TestType):
                value = value.name
            elif isinstance(value, datetime):
                value = str(value)
            data[key] = value

        return data
