from typing import Union


def get_mask_card_number(numbers: Union[str, int]) -> str:
    """Функция, создающая маску для номера карты в формате ХХХХ ХХ** **** ХХХХ"""
    numbers_str = str(numbers)
    if len(numbers_str) == 16:
        return f"{numbers_str[:4]} {numbers_str[4:6]}** **** {numbers_str[-4:]}"
    return "Проверьте длину номера карты"


def get_mask_account(numbers: Union[str, int]) -> str:
    """Функция, создающая маску для номера счета в формате **ХХХХ"""
    numbers_str = str(numbers)
    if len(numbers_str) == 20:
        return f"**{numbers_str[-4:]}"
    return "Проверьте длину номера счета"
