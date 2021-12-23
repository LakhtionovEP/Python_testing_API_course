import requests
from config import Config


class ApiSurveys:
    def __init__(self):
        self.url = Config.url
        self.default_headers = {"accept": "application/json"}
        #self.default_headers = {"surveys-token": Application.token}

    def authenticate(self, login, password):
        api_method = 'api/auth/login'
        url = self.url + api_method
        headers = self.default_headers
        body = {
            "login": login,
            "password": password
        }

        response = requests.post(url, headers=headers, json=body)
        print(response)
        return response


    def get_survey_by_id(self, token, id=580):
        api_method = f'api/survey/{id}'
        url = self.url + api_method
        headers = self.default_headers
        headers["surveys-token"] = token

        response = requests.get(url, headers=headers)

        print(response.text)
        print(response.url)
        return response


    def post_survey_status(self, token, id, status):
        api_method = f'api/survey/status/{id}/{status}'
        url = f'{self.url}{api_method}'
        headers = self.default_headers
        headers["surveys-token"] = token

        response = requests.post(url, headers=headers)
        print(response.text)
        print(response.url)
        return response

    def post_survey(self, token, body):
        api_method = 'api/survey/'
        url = f'{self.url}{api_method}'
        headers = self.default_headers
        headers["surveys-token"] = token

        response = requests.post(url, headers=headers, json=body)
        print(response.text)
        print(response.url)
        return response

    def put_survey(self, token, id, body):
        api_method = f'api/survey/{id}'
        url = self.url + api_method
        headers = self.default_headers
        headers["surveys-token"] = token

        response = requests.put(url, headers=headers, json=body)

        print(response.text)
        print(response.url)
        return response

    def get_survey_by_subs(self, token, subs):
        api_method = f'api/survey/title/{subs}'
        url = self.url + api_method
        headers = self.default_headers
        headers["surveys-token"] = token

        response = requests.get(url, headers=headers)

        print(response.text)
        print(response.url)
        return response

    def delete_survey_by_id(self, token, id):
        api_method = f'api/survey/{id}'
        url = self.url + api_method
        headers = self.default_headers
        headers["surveys-token"] = token

        response = requests.delete(url, headers=headers)

        print(response.text)
        print(response.url)
        return response