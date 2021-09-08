from selenium.webdriver.common.by import By

from lesson_18.pages.base_page import BasePage
from lesson_18.pages.product_page import ProductPage


class ProductListPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__first_product_locator = (By.XPATH, "//tbody/tr[@class='wrap'][1]")

    def choose_first_product(self) -> ProductPage:
        self._click(self.__first_product_locator)
        return ProductPage(self._driver)
