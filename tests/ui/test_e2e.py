from pages.cart_page import CartPage
from pages.items_page import ItemsPage

# successful e2e
def test_e2e(login, items, cart, checkout_information, checkout_overview, checkout_complete):
    login.expect_credentials()

    login.type_username("standard_user")
    login.type_password("secret_sauce")
    login.click_login_button()

    login.expect_products_page()

    items.add_product_by_name("sauce-labs-backpack")
    items.add_product_by_name("sauce-labs-fleece-jacket")
    items.add_product_by_name("sauce-labs-bolt-t-shirt")

    items.expect_remove_button("sauce-labs-backpack")

    items.click_details(5)

    items.click_shopping_cart()

    cart.expect_your_cart()
    cart.expect_url()
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
    checkout_overview.click_finish_button()

    checkout_complete.expect_url()
    checkout_complete.expect_thank_you()
    checkout_complete.click_back_home()

    items.expect_url()
