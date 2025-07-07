import pytest

from pages.cart_page import CartPage
from pages.items_page import ItemsPage

# successful e2e
@pytest.mark.e2e
def test_e2e_successful_order(login, items, cart, checkout_information, checkout_overview, checkout_complete):
    login.expect_credentials()
    login.type_username("standard_user")
    login.type_password("secret_sauce")
    login.click_login_button()
    login.expect_products_page()

    items.add_product_by_name("Sauce Labs Backpack")
    items.add_product_by_name("Sauce Labs Fleece Jacket")
    items.add_product_by_name("Sauce Labs Bolt T-Shirt")
    items.expect_remove_button("Sauce Labs Backpack")
    items.click_details(5)
    items.click_shopping_cart()

    cart.expect_your_cart()
    cart.expect_url()
    cart.remove_product_by_name("Sauce Labs Fleece Jacket")
    cart.click_checkout()

    checkout_information.expect_checkout_information_url()
    checkout_information.expect_checkout_your_information()
    checkout_information.type_first_name("Dvora")
    checkout_information.type_last_name("Hirshaut")
    checkout_information.type_zip_code("1234")
    checkout_information.click_continue_button()

    checkout_overview.expect_url()
    checkout_overview.expect_title()
    checkout_overview.expect_price()
    # checkout_overview.click_details(1)
    #
    # #all the way back, because it go back to items page.
    # items.click_shopping_cart()
    # cart.click_checkout()
    # checkout_information.click_continue_button()
    # checkout_information.expect_error_message("Error: First Name is required")
    # checkout_information.type_first_name("Dvora")
    # checkout_information.type_last_name("Hirhsuat")
    # checkout_information.click_continue_button()
    # checkout_information.expect_error_message("Error: Postal Code is required")
    # checkout_information.type_zip_code("1234")
    # checkout_information.click_continue_button()
    checkout_overview.click_finish_button()

    checkout_complete.expect_url()
    checkout_complete.expect_thank_you()
    checkout_complete.click_back_home()

    items.expect_url()

def test_e2e(login, items, cart, checkout_information, checkout_overview, checkout_complete):
    pass