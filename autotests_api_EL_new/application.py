from clients.survey import ApiSurveys
from checkers.checkers_helper import Checkers
from helpers.survey import Helpers

class Application:
    def __init__(self):
        self.api_surveys = ApiSurveys()
        self.checkers = Checkers()
        self.helpers = Helpers()
