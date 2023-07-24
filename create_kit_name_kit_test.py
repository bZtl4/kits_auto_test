import sender_stand_request
import data

# Создание и присвоение имени набора пользователя (позитивная проверка)


def positive_assert(name):
    # подготовка данных
    kit_headers = data.headers.copy()                             # копирование словарь для передачи headers
    kit_headers["Authorization"] = sender_stand_request.token     # помещаем в headers токен
    name_kit = data.name_kit_body.copy()                          # копирование словарь для передачи headers
    name_kit["name"] = name                                       # добавляет параметр name в тело запроса

    # Формирование ответа на запрос
    response = sender_stand_request.create_kit(name_kit, kit_headers)

    # Проверка
    assert response.status_code == 201, f'Ошибка, ОР "201" отличается от ФР "{response.status_code}"'
    assert response.json()["name"] == name, f'Ошибка, ОР "{name}" отличается от ФР "{response.json()["name"]}"'


# Создание и присвоение имени набора пользователя (негативная проверка)
def negative_assert_code_400(name=None):
    # подготовка данных
    kit_headers = data.headers.copy()                                 # копирование словарь для передачи headers
    kit_headers["Authorization"] = sender_stand_request.token         # помещаем в headers токен
    new_kit_body = data.name_kit_body.copy()                          # копирование словарь для передачи headers
    if name is not None:
        new_kit_body["name"] = name

    # Формирование ответа на запрос
    response = sender_stand_request.create_kit(new_kit_body, kit_headers)

    # Проверка
    assert response.status_code == 400, f'Ошибка, ОР "400" отличается от ФР "{response.status_code}"'


def test_create_kit_1_letter_in_name():             # п. 1 чек-листа - Допустимое количество символов (1)
    positive_assert("a")


def test_create_kit_511_letters_in_name():          # п. 2 чек-листа - Допустимое количество символов (511)
    positive_assert("A" * 511)


def test_create_kit_0_letter_in_name():             # п. 3 чек-листа - Количество символов меньше допустимого (0)
    negative_assert_code_400("")


def test_create_kit_512_letters_in_name():          # п. 4 чек-листа - Количество символов больше допустимого (512)
    negative_assert_code_400("A" * 512)


def test_create_kit_english_letters_in_name():      # п. 5 чек-листа - Разрешены английские буквы
    positive_assert("QWErty")


def test_create_kit_russian_letters_in_name():      # п. 6 чек-листа - Разрешены русские буквы
    positive_assert("Мария")


def test_create_kit_special_symbols_in_name():      # п. 7 чек-листа - Разрешены спецсимволы
    positive_assert("№%@,")


def test_create_kit_space_in_name():                # п. 8 чек-листа - Разрешены пробелы
    positive_assert(" Человек и КО ")


def test_create_kit_numbers_in_name():              # п. 9 чек-листа - Разрешены цифры
    positive_assert("123")


def test_create_kit_none_letter_in_name():          # п. 10 чек-листа - Параметр не передан в запросе
    negative_assert_code_400()


def test_create_kit_another_type_in_name():         # п. 11 чек-листа - Передан другой тип параметра
    negative_assert_code_400(123)
