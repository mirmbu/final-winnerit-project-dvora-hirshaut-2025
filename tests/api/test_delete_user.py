import pytest
from assertpy import assert_that
from api_requests.user_request_generator import UserRequestGenerator


user_request_generator = UserRequestGenerator()

@pytest.mark.api
def test_delete_user():

    response = user_request_generator.delete_user(2)

    #Assertions
    #status code
    user_request_generator.validate_status_code(response, 204)

    # json structure
    assert 'id' not in response
