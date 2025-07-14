import pytest
from assertpy import assert_that
from api_requests.user_request_generator import UserRequestGenerator

user_request_generator = UserRequestGenerator()

@pytest.mark.api
def test_register_unsuccessful():

    payload = {
        "email": "sydney@fife"
    }

    response = user_request_generator.register(payload)
    response_body = response.json()

    # Assertions
    # status code
    user_request_generator.validate_status_code(response, 400)

    # json structure
    assert_that(response_body['error']).is_equal_to('Missing password')