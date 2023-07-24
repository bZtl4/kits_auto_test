import requests
import configuration as c
import data

# Создание пользователя и получение авто токена
def post_new_user():
    response = requests.post(c.URL_SERVICE + c.CREATE_USER_PATH,
                             json=data.user_body,
                             headers=data.headers)
    if response.status_code == 201:
        return "Bearer " + response.json()["authToken"]  # Возвращаем в ответе авто токен

token = post_new_user()


# Создание набора
def create_kit(body, headers):
    return requests.post(c.URL_SERVICE + c.CREATE_KITS_PATH, json=body, headers=headers)
