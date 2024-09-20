def get_mask_card_number(numbers: int) -> str:
    """Функция, создающая маску для номера карты в формате ХХХХ ХХ** **** ХХХХ"""
    numbers_str = str(numbers)

    return f"{numbers_str[:4]} {numbers_str[5:7]}** **** {numbers_str[-4:]}"


def get_mask_account(numbers: int) -> str:
    """Функция, создающая маску для номера счета в формате **ХХХХ"""
    numbers_str = str(numbers)

    return f"**{numbers_str[-4:]}"
