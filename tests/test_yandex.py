import allure


@allure.title("Выполнение запроса на поиск. Позитивный сценарий.")
def test_positive_search_scenario(yandex_fixture, headers):
    with allure.step("Присвоение адреса для поиска"):
        place = 'Санкт-Петербург,+Невский+проспект,+дом+1'
    with allure.step("Выполнение запроса поиска по городу, улице, дому"):
        yandex_fixture.get_request_positive(place, headers)
    with allure.step("Проверка статус кода"):
        yandex_fixture.check_status_code(200)
    with allure.step("Проверка заголовка ответа"):
        yandex_fixture.check_response_headers()
    with allure.step("Получение из тела ответа геокод"):
        request_field = yandex_fixture.get_request_field()
    with allure.step("Сравнение поискового запроса и геокода из тела ответа"):
        place = yandex_fixture.replace_plus_to_space(place)
        assert request_field == place
    with allure.step("Получение координат из тела ответа"):
        pos = yandex_fixture.get_pos_field()


@allure.title("Выполнение запроса на поиск, без API_KEY. Негативный сценарий")
def test_search_without_api_key_negative(yandex_fixture, headers):
    with allure.step("Присвоение адреса для поиска"):
        place = 'Санкт-Петербург,+Невский+проспект,+дом+1'
    with allure.step("Выполненеие запроса поиска по городу, улице, дому"):
        yandex_fixture.get_request_negative_without_api_key(place, headers)
    with allure.step("Проверка статус кода"):
        yandex_fixture.check_status_code(403)
    with allure.step("Проверка заголовка ответа"):
        yandex_fixture.check_response_headers()


@allure.title("Выполнение запроса на поиск. Пустой url. Негативный сценарий")
def test_search_empty_url_negative(yandex_fixture, headers):
    with allure.step("Выполненеие запроса поиска по городу, улице, дому"):
        yandex_fixture.get_bad_empty_request(headers)