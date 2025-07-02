from pages.cart_page import CartPage
from pages.items_page import ItemsPage

# successful e2e
def test_e2e(login, items, cart):
    login.expect_credentials()

    login.type_username("standard_user")
    login.type_password("secret_sauce")
    login.click_login_button()

    login.expect_products_page()

    items.add_jacket()
    items.add_t_shirt()
    #items.add_t_shirt()
    items.add_backpack()
    items.expect_remove_button("sauce-labs-backpack")

    items.click_details(5)

    items.click_shopping_cart()

    cart.expect_your_cart()
    cart.expect_url()
    cart.click_checkout()
