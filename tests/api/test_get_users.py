import pytest
from assertpy import assert_that
from api_requests.users_request_generator import UsersRequestGenerator


users_request_generator = UsersRequestGenerator()


@pytest.mark.api
def test_get_users():

    response = users_request_generator.get_users(2)
    response_body = response.json()

    #Assertions
    #status code
    users_request_generator.validate_status_code(response, 200)

    # json structure
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

