from clients.survey import ApiSurveys
from checkers.checkers_helper import Checkers
from helpers.survey import Helpers
from config import Config


class Application:
    def __init__(self):
        self.api_surveys = ApiSurveys()
        self.checkers = Checkers()
        self.helpers = Helpers()
        self.token = self.try_login(Config.login, Config.password)

    def try_login(self, login, password):
        try:
            response = self.api_surveys.authenticate(login, password)
            print(response)
            return response.json()["token"]
        except:
            return Config.token

