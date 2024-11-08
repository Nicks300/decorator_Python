import json
from typing import Callable, Dict

DICT_USERS: Dict = {}

def check_login_password(function: Callable[[], str]):
    global DICT_USERS
    with open("materials/users.json", "r", encoding="utf-8") as file:
        DICT_USERS = json.load(file)
    login: str = input()
    password: str = input()

    if login not in DICT_USERS.keys() or DICT_USERS.get(login).get("password") != password:
        raise PermissionError('Неверные логин или пароль!')
    else:
        print("Сигнал из функции")
        return function

def stub_write_recipe():
    return """Пример рецепта.
Пум-пум-пум 2 раза в день 5 дней.
Там-там-там 3 раза в день перед едой 3 дня.
Дум-дум-дум 1 раз в день 10 дней."""


def stub_add_to_schedule():
    return "Пациент записан на тот-то день, в такое-то время"


if __name__ == '__main__':
    stub_write_recipe = check_login_password(stub_write_recipe)
    stub_add_to_schedule = check_login_password(stub_add_to_schedule)

    print('-' * 50)
    print('Сигнал перед главным вызовом')
    print('-' * 50)
    print(stub_write_recipe())
    print(stub_add_to_schedule())

    print(type(stub_write_recipe))
    print(type(stub_add_to_schedule))


