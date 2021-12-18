import requests
from config import Config


class ApiSurveys:
    def __init__(self):
        self.url = Config.url
        self.default_headers = {"accept": "application/json"}
        self.default_headers = {"surveys-token": Config.token}

    def get_survey_by_id(self, id=580):
        api_method = f'api/survey/{id}'
        url = self.url + api_method
        headers = self.default_headers

        response = requests.get(url, headers=headers)

        print(response.text)
        print(response.url)
        return response


    def post_survey_status(self, id, status):
        api_method = f'api/survey/status/{id}/{status}'
        url = f'{self.url}{api_method}'
        headers = self.default_headers

        response = requests.post(url, headers=headers)
        print(response.text)
        print(response.url)
        return response

    def post_survey(self, body):
        api_method = 'api/survey/'
        url = f'{self.url}{api_method}'
        headers = self.default_headers

        response = requests.post(url, headers=headers, json=body)
        print(response.text)
        print(response.url)
        return response