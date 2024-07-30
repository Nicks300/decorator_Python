

def stub_write_recipe(
    signature_name: str,
    signature_speciality: str = 'Врач-терапевт'
) -> str:
    return f"""Пример рецепта.
Пум-пум-пум 2 раза в день 5 дней.
Там-там-там 3 раза в день перед едой 3 дня.
Дум-дум-дум 1 раз в день 10 дней.

{signature_name}
{signature_speciality}"""


def stub_add_to_schedule(day: str, time_: str) -> str:
    return f"Пациент записан на {day}, в {time_}"


if __name__ == '__main__':
    print(stub_write_recipe(signature_name='Иванов Иван Иванович', signature_speciality='Врач-хирург'))
    print(stub_add_to_schedule('2024-02-13', '13:00'))
