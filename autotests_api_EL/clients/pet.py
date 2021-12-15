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
