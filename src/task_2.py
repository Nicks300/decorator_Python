

with ...
    DICT_USERS = ...


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
