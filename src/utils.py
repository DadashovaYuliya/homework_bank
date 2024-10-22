import json
import logging
from typing import Any

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_bank_transaction_data(path: str) -> Any:
    """Функция, возвращающая список словарей с данными о финансовых транзакциях"""
    try:
        logger.info("Попытка открытия файла")
        with open(path, encoding="utf-8") as f:

            try:
                logger.info("Получение транзакций из файла")
                bank_file = json.load(f)
            except json.JSONDecodeError as ex:
                logger.error(f"Произошла ошибка получения транзакций: {ex}")
                return []

    except FileNotFoundError as ex:
        logger.error(f"Произошла ошибка открытия файла: {ex}")
        return []

    return bank_file
