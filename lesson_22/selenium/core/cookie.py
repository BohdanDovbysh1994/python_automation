from .web_driver import WebDriver


class Cookie:
    def __init__(self, driver: WebDriver):
        self.__driver = driver
