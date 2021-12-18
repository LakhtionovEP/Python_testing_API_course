from clients.pet import ApiPetStore
#from helpers.message import MessageHelper
from helpers.petgen import PetgenHelper
from checkers.general import Checker


class Application:
    def __init__(self):
        self.api = ApiPetStore()
        self.helper = PetgenHelper()
        self.checker = Checker()
