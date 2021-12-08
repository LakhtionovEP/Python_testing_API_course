import requests
baseurl = 'https://petstore.swagger.io/v2'
api1 = '/pet/findByStatus'
params1 = {'status': 'available'}
r1 = requests.get(baseurl+api1, params=params1)
print(r1.status_code)
print(r1.json())
api2 = '/user'
params2 = '/string'
r2 = requests.get(baseurl+api2+params2)
print(r2.status_code)
print(r2.json())
