import pytest
from assertpy import assert_that
from api_requests.user_request_generator import UserRequestGenerator

user_request_generator = UserRequestGenerator()

@pytest.mark.api
def test_login_successful():

    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = user_request_generator.login(payload)
    response_body = response.json()

    # Assertions
    # status code
    user_request_generator.validate_status_code(response, 200)

    # json structure
    assert_that(response_body['token']).is_not_empty()