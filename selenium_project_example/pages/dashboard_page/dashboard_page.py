from ..base_page import BasePage
from ...core.singleton import singleton
from ...core.web_driver import WebDriver
from .dashboard_locators import DashboardLocators


@singleton
class DashboardPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.__locators = DashboardLocators()
