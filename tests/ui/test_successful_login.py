#successful login
def test_successful_login(login_page):
    login_page.expect_credentials()

    login_page.type_username("standard_user")
    login_page.type_password("secret_sauce")
    login_page.click_login_button()

    login_page.expect_products_page()

