import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains


def test_send_keys():
    driver = Chrome("./drivers/chromedriver")
    search_input_field_locator = "//input[@title='Поиск']"

    driver.get("https://google.com")

    search_input_field = driver.find_element_by_xpath(search_input_field_locator)
    search_input_field.send_keys("Harley Davidson")
    time.sleep(3)

    driver.quit()


def test_key_combination_with_action_chaines():
    driver = Chrome("./drivers/chromedriver")
    search_input_field_locator = "//input[@title='Поиск']"
    first_search_result_locator = "//ul[@role='listbox']//li[1]"
    first_link_in_search_result_locator = "//a[3]"

    driver.get("https://google.com")

    search_input_field = driver.find_element_by_xpath(
        search_input_field_locator
    )
    actions = ActionChains(driver)
    # Cntrl + a
    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    driver.quit()

def test_scroll_with_action_chaines():
    driver = Chrome("./drivers/chromedriver")
    search_input_field_locator = "//input[@title='Поиск']"
    first_search_result_locator = "//ul[@role='listbox']//li[1]"
    first_link_in_search_result_locator = "//a[3]"

    driver.get("https://google.com")

    search_input_field = driver.find_element_by_xpath(
        search_input_field_locator
    )
    actions = ActionChains(driver)
    # move to element
    # actions.move_to_element(target_element)

    driver.quit()

def test_other_examples():
    driver = Chrome("./drivers/chromedriver")
    search_input_field_locator = "//input[@title='Поиск']"
    first_search_result_locator = "//ul[@role='listbox']//li[1]"
    first_link_in_search_result_locator = "//a[3]"

    driver.get("https://google.com")

    search_input_field = driver.find_element_by_xpath(
        search_input_field_locator
    )
    # search_input_field.clear()
    # search_input_field.screenshot("element.jpg")
    # search_input_field.get_attribute("role")
    # assert search_input_field.text == "some"

    # first_search_result_element: WebElement = driver.find_element_by_xpath(first_search_result_locator)
    # first_search_result_element.click()
    # driver.back()
    # driver.save_screenshot("name.jpg")
    # time.sleep(3)

    # first_link_in_search_result: WebElement = driver.find_element_by_xpath(first_link_in_search_result_locator)
    # first_link_in_search_result.click()
    # time.sleep(3)

    # actions.key_down(Keys.CONTROL).send_keys("r").key_up(Keys.CONTROL).perform()
    # driver.refresh()
    # time.sleep(5)

    driver.quit()
