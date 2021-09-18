import pytest

from os.path import abspath

from selenium.webdriver import Chrome

from .pages.dashboard_page.dashboard_page import DashboardPage


@pytest.fixture(scope="session")
def driver():
    # driver = Chrome(abspath("/infrastructure/drivers/chromedriver"))
    driver = Chrome("/lesson_22/selenium/infrastructure/drivers/chromedriver")
    yield driver
    driver.quit()


@pytest.fixture
def dashboard_page(driver) -> DashboardPage:
    yield DashboardPage(driver)
