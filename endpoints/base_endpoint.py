import pytest
import requests\

class BaseEndpoint:
    def __init__(self):
        self.response_json = None
        self.response = None
        self.BASE_URL_GEOCODE = 'https://geocode-maps.yandex.ru/1.x'
        self.BASE_URL_SEARCH_MAPS = 'https://search-maps.yandex.ru/v1/'
        self.API_KEY = '008e5caa-76c5-48b4-b082-5df21148ba84'

    def get_request(self, url, headers):
        self.response = requests.get(url, headers=headers, verify=False)
        self.response_json = self.response.json()
        return self.response_json

    def post_request(self, url, headers, data):
        self.response = requests.post(url, headers=headers, data=data, verify=False)
        self.response_json = self.response.json()
        return self.response_json

    def check_status_code(self, code):
        if self.response.status_code == code:
            pass
        else:
            pytest.fail(f'Error: {self.response.status_code}')

    def check_response_headers(self):
        if self.response.headers['Content-Type'] == 'application/json; charset=utf-8':
            pass
        else:
            pytest.fail(f'Error: Headers != application/json')

    def replace_plus_to_space(self, place):
        return place.replace('+', ' ')