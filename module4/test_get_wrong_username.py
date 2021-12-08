import pytest
import requests


@pytest.mark.parametrize("username", ["wrong", "error"])
def test_negative(username):
    response = requests.get(f'https://petstore.swagger.io/v2/user/{username}')
    assert response.status_code == 404, "Код не соответсвует"
    assert response.json()['type'] == 'error'
    assert response.json()['message'] == 'User not found'

