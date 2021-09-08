def test_check_choose_category_of_product(dashboard):
    dashboard.choose_category("Авто")
    assert dashboard.is_subcategories_displayed() == False
