import pytest
from assertpy import assert_that
from api_requests.user_request_generator import UserRequestGenerator


user_request_generator = UserRequestGenerator()


@pytest.mark.api
def test_get_resource_user():
    response = user_request_generator.get_resource_user(2)
    response_body = response.json()

    #Assertions
    #status code = 200
    user_request_generator.validate_status_code(response, 200)

    #more assertions
    assert response_body['data']['id'] == 2
    assert response_body['data']['name'] != 'Fuchsia rose'

    # json structure
    assert_that(response_body['data']['year']).is_equal_to(2001)
    assert_that(response_body['data']).contains('color')
    assert_that(response_body['data']).does_not_contain_key('support')
    assert_that(response_body['support']['text']).is_not_empty()


    #Raise an error
    with pytest.raises(AssertionError) as err:
        assert_that(response_body['data']['color']).is_false()
    assert "Expected <False>, but was not." in str(err.value)
    assert_that(f'{err.value}').is_equal_to('Expected <False>, but was not.')
