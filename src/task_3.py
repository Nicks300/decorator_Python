import json
from typing import Callable, Dict, Any

DICT_USERS: Dict[str, Dict[str, Any]] = {}
IS_AUTHORIZED: bool = False

def check_login_password(function: Callable[[], str]):
    def wrapper():
        global IS_AUTHORIZED
        global DICT_USERS
        if not IS_AUTHORIZED:
            with open("materials/users.json", "r", encoding="utf-8") as file:
                DICT_USERS = json.load(file)
            login: str = input()
            password: str = input()
            if login not in DICT_USERS.keys() or DICT_USERS.get(login).get("password") != password:
                raise PermissionError('Неверные логин или пароль!')
            else:
                IS_AUTHORIZED = True
        return function()
    return wrapper


@check_login_password
def stub_write_recipe():
    return """Пример рецепта.
Пум-пум-пум 2 раза в день 5 дней.
Там-там-там 3 раза в день перед едой 3 дня.
Дум-дум-дум 1 раз в день 10 дней."""

@check_login_password
def stub_add_to_schedule():
    return "Пациент записан на тот-то день, в такое-то время"


if __name__ == '__main__':
    print(stub_write_recipe())
    print(stub_add_to_schedule())
