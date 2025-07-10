import pytest
from assertpy import assert_that
from api_requests.users_request_generator import UsersRequestGenerator

users_request_generator = UsersRequestGenerator()

@pytest.mark.api
def test_get_resource_users():

    response = users_request_generator.get_resource_users()
    response_body = response.json()

    #Assertions
    #status code
    users_request_generator.validate_status_code(response, 200)

    # json structure
    assert_that(response_body['page']).is_equal_to(1)
    assert_that(response_body['per_page']).is_equal_to(6)

    assert response_body['data'][0]['id'] == 1
    assert response_body['data'][1]['pantone_value'] == '17-2031'
    assert_that(response_body['data'][2]['name']).is_not_equal_to('True Red')