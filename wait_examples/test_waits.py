from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_send_keys():
    driver = Chrome("../lesson_18/drivers/chromedriver")
    # driver.implicitly_wait(10)
    web_driver_wait = WebDriverWait(driver, 10)

    search_input_field_locator = "//input[@title='Поиск']"
    first_search_result_locator = "//ul[@role='listbox']//li[1]"
    first_link_in_search_result_locator = "//a[3]"

    driver.get("https://google.com")

    search_input_field = web_driver_wait.until(
        EC.presence_of_element_located(
            (By.XPATH, search_input_field_locator)
        )
    )

    # search_input_field = web_driver_wait.until(
    #     lambda driver: driver.find_element_by_xpath(search_input_field_locator)
    # )
    # search_input_field = driver.find_element_by_xpath(search_input_field_locator)

    search_input_field.send_keys("Harley Davidson")
    search_input_field = driver.find_element_by_xpath(
        search_input_field_locator
    )
    driver.quit()
