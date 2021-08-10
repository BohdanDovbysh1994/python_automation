from lesson_15.factory_method_pattern.drivers import ChromeBrowser, \
    FirefoxBrowser, EdgeBrowser
from lesson_15.factory_method_pattern.drivers.browser import Browser


class BrowserFactory:
    @staticmethod
    def get_browser(name: str) -> Browser:
        if name == "chrome":
            return ChromeBrowser()
        elif name == "firefox":
            return FirefoxBrowser()
        elif name == "edge":
            return EdgeBrowser()
        else:
            raise Exception("Incorrect name of browser(")


if __name__ == '__main__':
    browser = BrowserFactory.get_browser(name)
