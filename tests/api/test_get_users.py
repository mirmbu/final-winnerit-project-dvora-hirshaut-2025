import requests
import pytest
from assertpy import assert_that


def test_get_users(base_reqres_url, headers):
    response = requests.get(f'{base_reqres_url}/api/users?page=2', headers=headers, verify=False)
    response_body = response.json()

    #Assertions
    assert_that(response.status_code).is_equal_to(200)

    assert response_body['data'][0]['id'] == 7
    assert response_body['data'][1]['email'] == 'lindsay.ferguson@reqres.in'
    assert response_body['data'][2]['first_name'] == 'Tobias'
    assert response_body['data'][3]['last_name'] == 'Fields'
    assert response_body['data'][4]['avatar'] == 'https://reqres.in/img/faces/11-image.jpg'
    assert response_body['data'][5]['email'] == 'rachel.howell@reqres.in'

    assert_that(response_body).contains_key('page')
    assert_that(response_body).contains_key('support')
    assert_that(response_body['support']).contains_key('url')
    assert_that(response_body['support']['text']).is_equal_to('Tired of writing endless social media content? Let Content Caddy generate it for you.')

    assert_that(len(list(response_body))).is_equal_to(6)