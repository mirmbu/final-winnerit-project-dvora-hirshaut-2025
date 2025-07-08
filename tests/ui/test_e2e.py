import pytest

# successful e2e
@pytest.mark.e2e
@pytest.mark.ui
def test_e2e_successful_order(login, products, cart, checkout_information, checkout_overview, checkout_complete):
    #login
    login.expect_credentials()
    login.type_username("standard_user")
    login.type_password("secret_sauce")
    login.click_login_button()
    login.expect_products_page()

    #add products to cart
    products.add_product_by_name("Sauce Labs Backpack")
    products.add_product_by_name("Sauce Labs Fleece Jacket")
    products.add_product_by_name("Sauce Labs Bolt T-Shirt")
    #expect remove button is visible
    products.expect_remove_button("Sauce Labs Backpack")
    #click to see details of product with id=5
    products.click_details(5)
    #click on the shopping cart button
    products.click_shopping_cart()

    #cart page
    cart.expect_your_cart()
    cart.expect_url()
    #click checkout
    cart.click_checkout()

    #checkout information page
    checkout_information.expect_checkout_information_url()
    checkout_information.expect_checkout_your_information()
    #type information
    checkout_information.type_first_name("Dvora")
    checkout_information.type_last_name("Hirshaut")
    checkout_information.type_zip_code("1234")
    #click continue button
    checkout_information.click_continue_button()

    #checkou overview
    checkout_overview.expect_url()
    checkout_overview.expect_title()
    #check the price
    checkout_overview.expect_price()
    #click to finish
    checkout_overview.click_finish_button()

    #checkout complete page
    checkout_complete.expect_url()
    checkout_complete.expect_thank_you()
    #click to back to products
    checkout_complete.click_back_home()

    #check that navigate back to products.
    products.expect_url()

@pytest.mark.e2e
@pytest.mark.ui
def test_e2e_click_details(login, products, cart, checkout_information, checkout_overview, checkout_complete):
    #login
    login.expect_credentials()
    login.type_username("standard_user")
    login.type_password("secret_sauce")
    login.click_login_button()
    login.expect_products_page()

    #add products
    products.add_product_by_name("Sauce Labs Backpack")
    products.add_product_by_name("Sauce Labs Fleece Jacket")
    products.add_product_by_name("Sauce Labs Bolt T-Shirt")
    products.add_product_by_name("Sauce Labs Bike Light")
    products.add_product_by_name("Sauce Labs Onesie")
    products.add_product_by_name("Test.allTheThings() T-Shirt (Red)")

    #click to see details of the product.
    products.click_details(2)
    #click shopping cart
    products.click_shopping_cart()

    #click the checkout button
    cart.click_checkout()

    #type checkout information
    checkout_information.type_first_name("Dvora")
    checkout_information.type_last_name("Hirshaut")
    checkout_information.type_zip_code("1234")
    # click continue button
    checkout_information.click_continue_button()

    #click to see details of id=1
    checkout_overview.click_details(1)
    #back to the product page, so need to do again.
    products.click_shopping_cart()
    cart.click_checkout()
    checkout_information.type_first_name("Dvora")
    checkout_information.type_last_name("Hirshaut")
    checkout_information.type_zip_code("1234")
    checkout_information.click_continue_button()
    checkout_overview.click_finish_button()
    checkout_complete.expect_thank_you()

@pytest.mark.e2e
@pytest.mark.ui
def test_e2e_remove_from_cart(login, products, cart, checkout_information, checkout_overview, checkout_complete):
    #login
    login.expect_credentials()
    login.type_username("standard_user")
    login.type_password("secret_sauce")
    login.click_login_button()
    login.expect_products_page()
    #add products
    products.add_product_by_name("Sauce Labs Backpack")
    products.add_product_by_name("Sauce Labs Fleece Jacket")
    products.add_product_by_name("Sauce Labs Bolt T-Shirt")
    products.add_product_by_name("Sauce Labs Bike Light")
    products.add_product_by_name("Sauce Labs Onesie")
    products.add_product_by_name("Test.allTheThings() T-Shirt (Red)")
    #click shopping cart
    products.click_shopping_cart()
    cart.expect_your_cart()
    cart.expect_url()
    #remove product from cart
    cart.remove_product_by_name("Sauce Labs Fleece Jacket")
    cart.remove_product_by_name("Sauce Labs Bolt T-Shirt")
    cart.remove_product_by_name("Test.allTheThings() T-Shirt (Red)")
    cart.click_checkout()
    #type checkout information
    checkout_information.type_first_name("Dvora")
    checkout_information.type_last_name("Hirshaut")
    checkout_information.type_zip_code("1234")
    # click continue button
    checkout_information.click_continue_button()
    checkout_overview.click_finish_button()
    checkout_complete.expect_thank_you()

@pytest.mark.e2e
@pytest.mark.ui
def test_e2e_checkout_information(login, products, cart, checkout_information, checkout_overview, checkout_complete):
    #login
    login.expect_credentials()
    login.type_username("standard_user")
    login.type_password("secret_sauce")
    login.click_login_button()
    login.expect_products_page()
    #add products
    products.add_product_by_name("Sauce Labs Backpack")
    products.add_product_by_name("Sauce Labs Fleece Jacket")
    products.add_product_by_name("Sauce Labs Bolt T-Shirt")
    products.add_product_by_name("Sauce Labs Bike Light")
    products.add_product_by_name("Sauce Labs Onesie")
    products.add_product_by_name("Test.allTheThings() T-Shirt (Red)")
    #click shopping cart
    products.click_shopping_cart()
    cart.click_checkout()

    #validation of checkout information
    checkout_information.click_continue_button()
    checkout_information.expect_error_message("Error: First Name is required")
    checkout_information.type_first_name("Dvora")
    checkout_information.type_last_name("Hirhsuat")
    checkout_information.click_continue_button()
    checkout_information.expect_error_message("Error: Postal Code is required")
    checkout_information.type_zip_code("1234")
    checkout_information.click_continue_button()

    checkout_overview.click_finish_button()
    checkout_complete.expect_thank_you()
