import requests
from config import Config

subs = 'EL'
api_method = f'api/survey/title/{subs}'
#api_method = 'api/auth/login'
url = f'{Config.url}{api_method}'
#url = 'http://survey-back-admin-bff-eco-services-stage.apps.okd.stage.digital.rt.ru/api/auth/login'
headers = {"accept": "application/json"}
headers["surveys-token"] = Config.token
body = {
    "login": Config.login,
    "password": Config.password
}

response = requests.get(url, headers=headers)
print(url)
print(response.json())
#print(response.json()['token'])
