import requests
import pytest
from assertpy import assert_that
from api_requests.user_request_generator import UserRequestGenerator

user_request_generator = UserRequestGenerator()

@pytest.mark.api
def test_resource_user_not_found():

    response = user_request_generator.get_resource_user(23)
    response_body = response.json()


    #Assertions
    #statuc doe
    user_request_generator.validate_status_code(response, 404)

    # json structure
    assert_that(response_body).is_empty()

    #Raise an error
    with pytest.raises(AssertionError) as err:
        assert_that(response_body).contains_key('name')
    assert "" in str(err.value)
