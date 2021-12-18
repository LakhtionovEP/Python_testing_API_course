import requests

url = 'http://survey-back-admin-bff-eco-services-stage.apps.okd.stage.digital.rt.ru/api/survey/580'
token = '8987-5qowpaqtr6r4np5347yd6jft13'
header = {"Accept": "application/json", "surveys-token": "8987-5qowpaqtr6r4np5347yd6jft13"}
response = requests.get(url, token, headers=header)
print(response.text)