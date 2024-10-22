import logging
from typing import Union

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(numbers: Union[str, int]) -> str:
    """Функция, создающая маску для номера карты в формате ХХХХ ХХ** **** ХХХХ"""
    try:
        logger.info("Создаем маску для номера карты")
        numbers_str = str(numbers)
        if len(numbers_str) == 16:
            return f"{numbers_str[:4]} {numbers_str[4:6]}** **** {numbers_str[-4:]}"
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")
    return "Проверьте корректность ввода номера карты"


def get_mask_account(numbers: Union[str, int]) -> str:
    """Функция, создающая маску для номера счета в формате **ХХХХ"""
    try:
        logger.info("Создаем маску для номера счета")
        numbers_str = str(numbers)
        if len(numbers_str) == 20:
            return f"**{numbers_str[-4:]}"
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")
    return "Проверьте корректность ввода номера счета"
