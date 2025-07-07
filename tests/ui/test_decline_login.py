import pytest


#username is missing
@pytest.mark.login
def test_username_missing(login):
    login.expect_credentials()

    login.type_username("")
    login.type_password("secret_sauce")
    login.click_login_button()

    login.expect_error_message("Epic sadface: Username is required")

#password is missing
@pytest.mark.login
def test_password_missing(login):
    login.expect_credentials()

    login.type_username("standard_user")
    login.type_password("")
    login.click_login_button()

    login.expect_error_message("Epic sadface: Password is required")

#username is invalid
@pytest.mark.login
def test_username_invalid(login):
    login.expect_credentials()

    login.type_username("abcd")
    login.type_password("secret_sauce")
    login.click_login_button()

    login.expect_error_message("Epic sadface: Username and password do not match any user in this service")

#password is invalid
@pytest.mark.login
def test_password_invalid(login):
    login.expect_credentials()

    login.type_username("standard_user")
    login.type_password("1234")
    login.click_login_button()

    login.expect_error_message("Epic sadface: Username and password do not match any user in this service")

#locked out user
@pytest.mark.login
def test_locked_out_user(login):
    login.expect_credentials()

    login.type_username("locked_out_user")
    login.type_password("secret_sauce")
    login.click_login_button()

    login.expect_error_message("Epic sadface: Sorry, this user has been locked out.")
