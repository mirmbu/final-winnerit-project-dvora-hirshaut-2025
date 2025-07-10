import pytest
from assertpy import assert_that
from api_requests.user_request_generator import UserRequestGenerator


user_request_generator = UserRequestGenerator()


@pytest.mark.api
def test_get_user():
    response = user_request_generator.get_user(2)
    response_body = response.json()

    #Assertions
    #status code = 200
    user_request_generator.validate_status_code(response, 200)

    ##json structure
    assert response_body['data']['id'] == 2
    assert response_body['data']['email'] == 'janet.weaver@reqres.in'

    assert_that(response_body['data']['first_name']).does_not_match('janet')
    assert_that(response_body['data']['last_name']).is_not_empty()
    assert_that(response_body['data']).contains('avatar')
    assert_that(response_body['data']).does_not_contain_key('support')

    #Raise an error
    with pytest.raises(AssertionError) as err:
        assert_that(response_body['data']['first_name']).does_not_match('Janet')
    assert "to not match pattern" in str(err.value)
    assert_that(f'{err.value}').is_equal_to('Expected <Janet> to not match pattern <Janet>, but did.')
