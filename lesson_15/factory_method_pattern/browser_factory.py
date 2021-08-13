from lesson_15.factory_method_pattern.drivers import ChromeBrowser, \
    FirefoxBrowser, EdgeBrowser
from lesson_15.factory_method_pattern.drivers.browser import Browser


class BrowserFactory:
    @staticmethod
    def get_browser(name: str):
        if name == "chrome":
            return ChromeBrowser()
        elif name == "firefox":
            return FirefoxBrowser()
        elif name == "edge":
            return EdgeBrowser()
        else:
            raise Exception("Incorrect name of browser(")


if __name__ == '__main__':
    print(id(BrowserFactory.get_browser("chrome")))
    print(id(BrowserFactory.get_browser("firefox")))
    print(id(BrowserFactory.get_browser("edge")))

    chrome = BrowserFactory.get_browser("chrome")
    firefox = BrowserFactory.get_browser("firefox")
    edge = BrowserFactory.get_browser("edge")
    print()
    print(id(chrome))
    print(id(firefox))
    print(id(edge))
