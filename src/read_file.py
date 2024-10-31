import csv
import logging
from typing import Any

import pandas as pd

logger = logging.getLogger("read_file")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/read_file.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_csv(path: str) -> list[dict[Any, Any]]:
    """Функция, возвращающая данные о транзакциях с файла формата csv"""
    try:
        logger.info("Попытка открытия файла")
        with open(path, encoding="utf-8") as file:
            logger.info("Чтение транзакций из файла")
            reader = csv.DictReader(file, delimiter=";")
            result = [row for row in reader]
            return result
    except Exception as ex:
        logger.error(f"Произошла ошибка чтения файла: {ex}")
        return [{}]


def read_excel(path: str) -> list[dict[Any, Any]]:
    """Функция, возвращающая данные о транзакциях с файла формата excel"""
    try:
        logger.info("Чтение транзакций из файла")
        reader = pd.read_excel(path, engine="openpyxl")
        result = reader.to_dict(orient="records")
        return result
    except Exception as ex:
        logger.error(f"Произошла ошибка чтения файла: {ex}")
        return [{}]
