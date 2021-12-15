import json

a = "schema"
b = "get_by_pet_id_response.json"
c = a + '/' + b
print(c)
with open(c) as file:
    schema = json.load(file)