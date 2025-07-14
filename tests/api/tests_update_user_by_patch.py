import pytest
from assertpy import assert_that
from api_requests.user_request_generator import UserRequestGenerator

user_request_generator = UserRequestGenerator()


@pytest.mark.api
def test_update_user_by_patch():

    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }

    response = user_request_generator.update_user_by_patch(2, payload)
    response_body = response.json()

    #Assertions
    #status code
    user_request_generator.validate_status_code(response, 200)

    # json structure
    assert_that(response_body['name']).is_equal_to(payload['name'])
    assert_that(response_body['job']).is_not_equal_to(payload['job'].upper())
    assert_that(response_body['createdAt']).contains(str(date.today()))
