from ..core.cookie import Cookie
from ..core.local_storage import LocalStorage
from ..core.singleton import singleton
from ..core.web_driver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self._cookie = Cookie(self.__driver)
        self._local_storage = LocalStorage(self.__driver)
