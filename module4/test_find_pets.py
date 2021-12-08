import pytest
import requests


def get_pets_by_status(status):
    params = {'status' : status}
    response = requests.get('https://petstore.swagger.io/v2/pet/findByStatus', params=params)
    return response


@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_positive(status):
    response = get_pets_by_status(status)
    assert response.status_code == 200, "Код не соответсвует"


