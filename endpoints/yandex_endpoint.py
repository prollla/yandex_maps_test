import allure
import requests

from endpoints.base_endpoint import BaseEndpoint


class YandexEndpoint(BaseEndpoint):
    def __init__(self):
        super().__init__()

    def get_request_positive(self, place, headers):
        url = f'{self.BASE_URL_GEOCODE}?apikey={self.API_KEY}&geocode={place}&format=json'
        response = self.get_request(url, headers)

    def get_request_negative_without_api_key(self, place, headers):
        url = f'{self.BASE_URL_GEOCODE}?apikey=API_KEY&geocode={place}&format=json'
        response = self.get_request(url, headers)

    def get_bad_empty_request(self, headers):
        url = f'{self.BASE_URL_GEOCODE}'
        with allure.step("Выполнение запроса"):
            response = requests.get(url, headers=headers, verify=False)
        with allure.step("Проверка статус кода"):
            assert response.status_code == 400
        with allure.step("Проверка заголовков"):
            assert response.headers['Content-Type'] == 'text/xml; charset=utf-8'

    def get_request_field(self):
        request_field = \
            self.response_json["response"]["GeoObjectCollection"]["metaDataProperty"]["GeocoderResponseMetaData"][
                "request"]
        return request_field

    def get_pos_field(self):
        pos_field = \
            self.response_json["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
        return pos_field
