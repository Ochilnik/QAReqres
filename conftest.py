import pytest
from modules.api.clients.reqresin import Reqres


@pytest.fixture
def reqres_api():
    api = Reqres()
    yield api
