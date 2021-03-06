import json
import jsonschema


class Checkers:
    @staticmethod
    def validate_json(item, path_to_schema):
        base_path = r'C:\Users\evgeniy.lakhtionov\Documents\GitHub\Python_testing_API_course\autotests_api_EL_new\schemas'
        path = base_path + '/' + path_to_schema

        with open(path) as file:
            schema = json.load(file)

        jsonschema.validate(item, schema)
        return True

    @staticmethod
    def validate_items(items, path_to_schema):
        base_path = r'C:\Users\evgeniy.lakhtionov\Documents\GitHub\Python_testing_API_course\autotests_api_EL_new\schemas'
        path = base_path + '/' + path_to_schema

        with open(path) as file:
            schema = json.load(file)

        stat = {}
        for i in range(len(items)):
            try:
                jsonschema.validate(items[i], schema)
                stat[items[i]['id']] = True
            except:
                stat[items[i]['id']] = False
        print(stat)
        #stat['1000'] = False
        stat = {key: val for key, val in stat.items() if val is False}
        #print(stat)
        if False in stat.values():
            return stat
        else:
            return True


    @staticmethod
    def check_get_survey_by_id(id, resp_dict):
        if resp_dict["id"] == id:
            return True
        else:
            return False

    @staticmethod
    def check_post_survey_status(resp_dict):
        if resp_dict["success"] == True:
            return True
        else:
            return False

    @staticmethod
    def check_post_survey(title, name, type, body):
        if body['title'] == title and body['businessTitle'] == name \
                and body['surveyPage'][0]['surveyQuestion'][0]['type'] == type:
            return True
        else:
            return False
