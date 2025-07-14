import pytest
from assertpy import assert_that
from api_requests.user_request_generator import UserRequestGenerator

user_request_generator = UserRequestGenerator()

@pytest.mark.api
def test_register_successful():

    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    response = user_request_generator.register(payload)
    response_body = response.json()

    #Assertions
    #status code
    user_request_generator.validate_status_code(response, 200)

    #json structure
    assert_that(response_body['id']).is_equal_to(4)
    assert_that(response_body['token']).is_not_empty()