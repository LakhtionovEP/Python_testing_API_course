import json
import jsonschema


class Checker:
    @staticmethod
    def validate_json(item, path_to_schema):
       path = base_path + "/" + path_to_schema
       with open(path) as file:
          schema = json.load(file)

       jsonschema.validate(item, schema)
       return True
