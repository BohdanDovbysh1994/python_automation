import time

import pytest
from selenium.webdriver import Chrome

from .pages.dashboard_page import Dashboard


@pytest.fixture(scope="session")
def driver() -> Chrome:
    driver = Chrome("../drivers/chromedriver")
    driver.maximize_window()
    driver.get("http://olx.ua")
    # time.sleep(2)

    # print("COOKIE: ", driver.get_cookies())
    # driver.add_cookie({"name": "auto", "value": "Hammer"})
    # print("COOKIE: ", driver.get_cookies())
    # print(driver.get_cookie("auto"))

    # driver.execute_script("window.localStorage['some_some'] = 'Hammer'")
    # print(driver.execute_script("return window.localStorage['some_some'];"))
    # print()
    yield driver

    driver.quit()


@pytest.fixture
def dashboard(driver) -> Dashboard:
    yield Dashboard(driver)
