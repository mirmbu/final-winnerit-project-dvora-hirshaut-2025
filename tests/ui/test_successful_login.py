import pytest

#successful login
@pytest.mark.login
def test_successful_login(login):
    login.expect_credentials()

    login.type_username("standard_user")
    login.type_password("secret_sauce")
    login.click_login_button()

    login.expect_products_page()

