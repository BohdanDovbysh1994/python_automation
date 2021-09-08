from selenium.webdriver.common.by import By

from lesson_19.core.locator import Locator


class DashboardLocatorsCollection:
    def __init__(self):
        # self.__gallery = Locator(By.XPATH, "//*[@id='gallerywide']")
        self.__upload_file_input_field_locator = Locator(
            By.XPATH, "//input[@type='file'][@style='visibility: hidden;']"
        )

    # @property
    # def gallery(self):
    #     return self.__gallery

    @property
    def upaload_file_input_field(self):
        return self.__upload_file_input_field_locator
