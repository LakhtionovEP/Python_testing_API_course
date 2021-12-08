import pytest
import requests
import random


def post_user(id, username, firstname, lastname, email, password, phone, userStatus=0):
    api_method = "v2/user"
    url = "https://petstore.swagger.io/" + api_method

    # словарь header содержит в себе необходимые заголовки для POST
    header = {"Accept": "application/json"}
    header["content-type"] = "application/json"

    # формирование тело запроса
    req_dict = {
        "id": id,
        "username": username,
        "firstName": firstname,
        "lastName": lastname,
        "email": email,
        "password": password,
        "phone": phone,
        "userStatus": userStatus
    }

    response = requests.request("POST", url, headers=header, json=req_dict)
    return response

def test_main():
    id = random.randint(100, 999)
    username = "EL2"
    firstName = "EL"
    lastName = "EL"
    email = "EL@mail.com"
    password = "admin"
    phone = "12345"
    userStatus = 0
    response = post_user(id, username, firstName, lastName, email, password, phone, userStatus)
    print('Создать пользователя')
    print(response.json())

    response = requests.get(f'https://petstore.swagger.io/v2/user/{username}')
    print('Запросить данные до обновления')
    print(response.json())
    old_phone = response.json()['phone']

    req_dict = {
        "id": id,
        "username": username,
        "firstName": firstName,
        "lastName": lastName,
        "email": email,
        "password": password,
        "phone": '666',
        "userStatus": userStatus
    }

    response = requests.put(f'https://petstore.swagger.io/v2/user/{username}', json=req_dict)
    print('Обновить данные')
    print(response.json())

    response = requests.get(f'https://petstore.swagger.io/v2/user/{username}')
    print('Запросить данные после обновления')
    print(response.json())
    new_phone = response.json()['phone']
    assert new_phone != old_phone, "Телефоны должны отличаться"


test_main()

#очень сильно глючит swagger для такого кейса :(