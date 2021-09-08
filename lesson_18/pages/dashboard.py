import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from .product_list_page import ProductListPage
from ..core.page_singleton import singleton
from .base_page import BasePage


@singleton
class Dashboard(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.__galery_locator = (By.XPATH, "//*[@id='gallerywide']")
        self.__auto_subcategory_locator = (By.XPATH, "//div[@id='bottom1532']")

    def choose_category(self, name: str) -> None:
        time.sleep((2))
        self._click((By.XPATH, f"//span[text()='{name}']/ancestor::div[1]"))

    def choose_subcategory(self, name: str) -> ProductListPage:
        self._click((By.XPATH, f"//span[text()='{name}']"))
        return ProductListPage(self._driver)

    def wait_for_galery(self):
        return self._wait_until_element_appears(self.__galery_locator)

    def is_subcategories_displayed(self):
        element = self._wait_until_element_appears(self.__auto_subcategory_locator)
        return element.get_attribute("style") == ""
