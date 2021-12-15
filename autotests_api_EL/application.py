from clients.pet import ApiPetStore
from helpers.message import MessageHelper
from checkers.general import Checker


class Application:
    def __init__(self):
        self.api = ApiPetStore()
        self.helper = MessageHelper()
        self.checker = Checker()
