import requests
import pytest
from assertpy import assert_that

@pytest.mark.api
def test_get_user_by_id(base_reqres_url, headers):
    response = requests.get(f'{base_reqres_url}api/users/2', headers=headers, verify=False)
    response_body = response.json()

    #Assertions
    assert_that(response.status_code).is_equal_to(200)

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
