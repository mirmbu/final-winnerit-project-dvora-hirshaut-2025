import pytest
from assertpy import assert_that
from datetime import date
from api_requests.user_request_generator import UserRequestGenerator


user_request_generator = UserRequestGenerator()

@pytest.mark.api
def test_create_user():

    payload = {
    "name": "morpheus",
    "job": "leader"
    }

    response = user_request_generator.create_user(payload)
    response_body = response.json()

    #Assertions
    #status code
    user_request_generator.validate_status_code(response, 201)

    #json structure
    assert_that(response_body['id']).is_not_empty()
    assert_that(response_body['name']).is_equal_to(payload["name"])
    assert_that(response_body['job']).contains(payload["job"])
    assert_that(response_body['createdAt']).contains(str(date.today()))

