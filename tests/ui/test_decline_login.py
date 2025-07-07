import pytest

data = {
    ("","secret_sauce", "Epic sadface: Username is required"),
    ("standard_user","", "Epic sadface: Password is required"),
    ("abcd","secret_sauce", "Epic sadface: Username and password do not match any user in this service"),
    ("standard_user","1234", "Epic sadface: Username and password do not match any user in this service"),
    ("locked_out_user","secret_sauce", "Epic sadface: Sorry, this user has been locked out.")
}

@pytest.mark.parametrize("username, password, expected", data)
@pytest.mark.login
@pytest.mark.ui
def test_declined_login(login, username: str, password: str, expected: str):
    login.expect_credentials()

    login.type_username(username)
    login.type_password(password)
    login.click_login_button()

    login.expect_error_message(expected)