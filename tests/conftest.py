import pytest

from endpoints.yandex_endpoint import YandexEndpoint


@pytest.fixture()
def yandex_fixture():
    return YandexEndpoint()


@pytest.fixture
def headers():
    return {
        'Content-Type': 'application/json'
    }
