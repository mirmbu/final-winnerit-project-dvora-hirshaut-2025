import pytest

data = {
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
    ("visual_user", "secret_sauce")
}

#successful login
@pytest.mark.parametrize("username, password", data)
@pytest.mark.login
@pytest.mark.ui
def test_successful_login(login, username: str, password: str):
    login.expect_credentials()

    login.type_username(username)
    login.type_password(password)
    login.click_login_button()

    login.expect_products_page()
