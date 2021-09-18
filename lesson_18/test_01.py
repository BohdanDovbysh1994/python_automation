from selenium.webdriver import Chrome


def test_01():
    driver = Chrome("./drivers/chromedriver")
    driver.get("https://google.com")
    driver.maximize_window()
    driver.quit()
