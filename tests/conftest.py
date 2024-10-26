import pytest
import sys
import os
from endpoints.yandex_endpoint import YandexEndpoint

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture()
def yandex_fixture():
    return YandexEndpoint()


@pytest.fixture
def headers():
    return {
        'Content-Type': 'application/json'
    }
