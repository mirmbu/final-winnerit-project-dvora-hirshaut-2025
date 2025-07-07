import requests
import pytest
from assertpy import assert_that

def test_user_not_found(base_reqres_url, headers):
    response = requests.get(f'{base_reqres_url}/api/users/23', headers=headers, verify=False)
    response_body = response.json()

    #Assertions
    assert response.status_code == 401
    # assert len(list(response_body)) == 0
    assert_that(response_body).is_empty()

    #Raise an error
    with pytest.raises(AssertionError) as err:
        assert_that(response_body).contains_key('id')
    assert "" in str(err.value)
