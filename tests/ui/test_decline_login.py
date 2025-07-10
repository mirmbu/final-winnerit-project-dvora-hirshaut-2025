import pytest
import pandas as pd
import os


#load the csv file and convert it to tuple.
def load_login_data():
    file_path = os.path.join(os.path.dirname(__file__), "login_test_cases.csv")
    df = pd.read_csv(file_path).fillna("")
    return [tuple(row) for row in df.to_numpy()]



@pytest.mark.parametrize("username,password,expected_result", load_login_data())
@pytest.mark.login
@pytest.mark.ui
def test_declined_login(login, username: str, password: str, expected_result: str):
    login.expect_credentials()

    login.type_username(username)
    login.type_password(password)
    login.click_login_button()

    login.expect_error_message(expected_result)