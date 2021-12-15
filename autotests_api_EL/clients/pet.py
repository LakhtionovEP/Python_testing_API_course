import requests


class ApiPetStore:
    def __init__(self):
        self.url = "https://petstore.swagger.io"
        self.default_headers = {"Accept": "application/json"}