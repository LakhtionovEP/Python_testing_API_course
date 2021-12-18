import json
import jsonschema


class Checker:
    @staticmethod
    def validate_json(item, path_to_schema):
        base_path = 'schemas'
        path = base_path + '/' + path_to_schema
        #path = base_path + path_to_schema
        with open(path) as file:
            schema = json.load(file)

        jsonschema.validate(item, schema)
        return True

    @staticmethod
    def check_find_pets_by_id(resp_dict, exp_status):
        for item in resp_dict:
            if item['status'] != exp_status:
                return False
        return True


    @staticmethod
    def check_post_pet(resp_dict, exp_status):
        for item in resp_dict:
            if item['status'] != exp_status:
                return False
        return True