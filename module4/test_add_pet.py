import requests
import random


def post_pet(id, category_id, category, name, photoUrls, tags_id, tags, status='available'):
    api_method = "v2/pet"
    url = "https://petstore.swagger.io/" + api_method

    # словарь header содержит в себе необходимые заголовки для POST
    header = {"Accept": "application/json"}
    header["content-type"] = "application/json"

    # формирование тело запроса
    req_dict = {
        "id": id,
        "category": {
            "id": category_id,
            'name': category
        },
        "name": name,
        "photoUrls": [
            photoUrls
            ],
        "tags": [
            {
            "id": tags_id,
            "name": tags
            }
            ],
        "status": status
    }

    response = requests.request("POST", url, headers=header, json=req_dict)
    return response


def delete_pet(petId):
    api_method = "v2/pet"
    url = "https://petstore.swagger.io/" + api_method

    # словарь header содержит в себе необходимые заголовки для POST
    header = {"Accept": "application/json"}
    header["content-type"] = "application/json"
    param = f'/{petId}'

    response = requests.request("DELETE", url+param, headers=header)
    return response


def test_positive():
    id = random.randint(1,100)
    category_id = random.randint(1,100)
    category = "test"
    name = "test"
    photoUrls = "test"
    tags_id = random.randint(1,100)
    tags = "test"
    status = "available"
    
    response = post_pet(id, category_id, category, name, photoUrls, tags_id, tags, status)
    print(response.status_code)
    assert response.status_code == 200, "Код ответа не соответствует ожидаемому"
    print(response.json())
    assert response.json()['name'] == name, "Созданное имя не соответствует запрашиваемому"
    
    response = delete_pet(id)
    print(response.url)
    print(response.status_code)


test_positive()
