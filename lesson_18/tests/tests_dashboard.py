import time


def test_check_choose_category_of_product(dashboard):
    dashboard.choose_category("Авто")
    product_list_page = dashboard.choose_subcategory("Легковые автомобили")
    time.sleep(1)
    product_page = product_list_page.choose_first_product()
    time.sleep(3)
