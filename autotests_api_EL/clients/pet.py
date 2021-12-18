import requests


class ApiPetStore:
    def __init__(self):
        self.url = "https://petstore.swagger.io"
        self.default_headers = {"Accept": "application/json"}

    def get_pet_by_id(self, pet_id):
        api_method = f"/v2/pet/{pet_id}"
        url = f"{self.url}{api_method}"
        headers = self.default_headers

        print("REQUEST: GET", url, sep="\n")
        response = requests.request("GET", url, headers=headers)
        print("RESPONSE: ", response.status_code, response.text, sep="\n")
        return response

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


        print("REQUEST: POST", url, sep="\n")
        response = requests.request("POST", url, headers=header, json=req_dict)
        print("RESPONSE: ", response.status_code, response.text, sep="\n")
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