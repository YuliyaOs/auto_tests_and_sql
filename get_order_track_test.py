# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data

# эта функция создает заказ и возвращает его трек номер


def get_track():
    order_response = sender_stand_request.post_new_order(data.order_body)
    track = order_response.json()["track"]
    return track

# эта функция присваивает параметру "t" значение полученного после создания заказа трек номера


def track_in_params():
    track = get_track()
    params = data.params.copy()
    params["t"] = track
    return params

# функция для позитивной проверки


def positive_assert():
    params = track_in_params()
    get_order_response = sender_stand_request.get_order(params)
    assert get_order_response.status_code == 200
    assert get_order_response.json()["order"] != ""

# функция для негативной проверки


def negative_assert(track):
    params = data.params.copy()
    params["t"] = track
    get_order_response = sender_stand_request.get_order(params)
    assert get_order_response.status_code == 404
    assert get_order_response.json()["code"] == 404
    assert get_order_response.json()["message"] == "Заказ не найден"

# функция для негативной проверки


def negative_assert_no_track(params):
    get_order_response = sender_stand_request.get_order(params)
    assert get_order_response.status_code == 400
    assert get_order_response.json()["code"] == 400
    assert get_order_response.json(
    )["message"] == "Недостаточно данных для поиска"

    
# Ославская Юлия, 35-я когорта - Финальный проект. Инженер по тестированию плюс

# Тест 1. Успешное получение заказа по треку заказа
def test_get_order_with_track_success_response():
    positive_assert()

# Тест 2. Ошибка
# Передача несуществующего трека заказа


def test_get_order_no_exist_track_error_response():
    negative_assert("666666")

# Тест 3. Ошибка
# Отправка запроса без трека заказа


def test_get_order_without_track_error_response():
    params = data.params.copy()
    params.pop("t")
    negative_assert_no_track(params)
