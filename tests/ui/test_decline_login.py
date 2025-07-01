#username is missing
def test_username_missing(login_page):
    login_page.expect_credentials()

    login_page.type_username("")
    login_page.type_password("secret_sauce")
    login_page.click_login_button()

    login_page.expect_error_message("Epic sadface: Username is required")

#password is missing
def test_password_missing(login_page):
    login_page.expect_credentials()

    login_page.type_username("standard_user")
    login_page.type_password("")
    login_page.click_login_button()

    login_page.expect_error_message("Epic sadface: Password is required")

#username is invalid
def test_username_invalid(login_page):
    login_page.expect_credentials()

    login_page.type_username("abcd")
    login_page.type_password("secret_sauce")
    login_page.click_login_button()

    login_page.expect_error_message("Epic sadface: Username and password do not match any user in this service")

#password is invalid
def test_password_invalid(login_page):
    login_page.expect_credentials()

    login_page.type_username("standard_user")
    login_page.type_password("1234")
    login_page.click_login_button()

    login_page.expect_error_message("Epic sadface: Username and password do not match any user in this service")

#locked out user
def test_locked_out_user(login_page):
    login_page.expect_credentials()

    login_page.type_username("locked_out_user")
    login_page.type_password("secret_sauce")
    login_page.click_login_button()

    login_page.expect_error_message("Epic sadface: Sorry, this user has been locked out.")
