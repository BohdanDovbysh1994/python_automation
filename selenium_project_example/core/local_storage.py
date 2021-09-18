from .web_driver import WebDriver


class LocalStorage:
    def __init__(self, driver: WebDriver):
        self.__driver = driver
