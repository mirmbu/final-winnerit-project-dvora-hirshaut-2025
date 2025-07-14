import pytest
from assertpy import assert_that
from api_requests.users_request_generator import UsersRequestGenerator

users_request_generator = UsersRequestGenerator()

@pytest.mark.api
def test_delayed_response():

    response = users_request_generator.delayed_response(3)
    response_body = response.json()

    # Assertions
    # status code
    users_request_generator.validate_status_code(response, 200)

    # json structure
    assert_that(response_body['page']).is_equal_to(1)
    assert_that(response_body['per_page']).is_equal_to(6)
    assert_that(response_body['total']).is_equal_to(12)
    assert_that(response_body['total_pages']).is_equal_to(2)
    assert_that(response_body['data'][0]).contains_key('id')
    assert_that(response_body['support']).contains_key('text')
    assert_that(response_body['support']['url']).is_not_empty()


    #Raise an error
    with pytest.raises(AssertionError) as err:
        assert_that(response_body['data'][4]['id']).is_equal_to(6)
    assert "to be equal to" in str(err.value)