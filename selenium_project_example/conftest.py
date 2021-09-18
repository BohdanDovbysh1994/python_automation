import pytest

from selenium.webdriver import Chrome

from .core.enums.test_type import TestType
from .core.test_result import TestResult
from .pages.dashboard_page.dashboard_page import DashboardPage


results = list()


@pytest.fixture(scope="session")
def driver(request):
    driver = Chrome("./infrastructure/drivers/chromedriver")
    yield driver
    # TODO: implement persistence storage layer for storing reports in DB (PostgreSQL, MongoDB)
    reports = TestResult.from_test_reports(results, TestType.UI)
    driver.quit()


@pytest.fixture
def dashboard_page(driver) -> DashboardPage:
    yield DashboardPage(driver)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    results.append(result)
