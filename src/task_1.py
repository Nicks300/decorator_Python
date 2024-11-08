import json
from typing import Callable, Dict


def check_login_password(function: Callable[[], str], dict_data: Dict[str, Dict[str, str]])-> str:
    login: str = input()
    password: str = input()
    found: bool = False

    if login in dict_data.keys():
        if dict_data[login].get("password") == password:
            found = True
    if found:
        return function()
    else:
        raise PermissionError('Неверные логин или пароль!')

def stub_write_recipe():
    return """Пример рецепта.
Пум-пум-пум 2 раза в день 5 дней.
Там-там-там 3 раза в день перед едой 3 дня.
Дум-дум-дум 1 раз в день 10 дней."""


def stub_add_to_schedule():
    return "Пациент записан на тот-то день, в такое-то время"


if __name__ == '__main__':
    file_path = "materials/users.json"
    with open(file_path, 'r') as file:
        data = json.load(file)

    print(check_login_password(stub_write_recipe, data))
    print(check_login_password(stub_add_to_schedule, data))
