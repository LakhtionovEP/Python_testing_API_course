import pytest

from application import Application
from helpers.message import MessageHelper

fixture = Application()


@pytest.fixture(scope="session")
def base_fixture():
    return fixture
