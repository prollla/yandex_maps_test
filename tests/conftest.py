import pytest


@pytest.fixture()
def yandex_fixture():
    return YandexEndpoint()


@pytest.fixture
def headers():
    return {
        'Content-Type': 'application/json'
    }
