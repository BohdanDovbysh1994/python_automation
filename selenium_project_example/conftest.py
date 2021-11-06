import pytest

from selenium.webdriver import Chrome

from .core.infrastructure.repositories.test_result_repository import \
    TestResultRepository
from .core.test_result import TestResult
from .pages.dashboard_page.dashboard_page import DashboardPage


results = list()


@pytest.fixture(scope="session")
def test_result_repository():
    yield TestResultRepository()


@pytest.fixture(scope="session")
def driver(request, test_result_repository):
    driver = Chrome("core/infrastructure/drivers/chromedriver")
    yield driver
    reports = TestResult.from_test_reports(results, "UI")
    test_result_repository.save(reports)
    driver.quit()


@pytest.fixture
def dashboard_page(driver) -> DashboardPage:
    yield DashboardPage(driver)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    results.append(result)