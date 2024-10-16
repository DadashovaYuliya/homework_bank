import json
from typing import Any


def get_bank_transaction_data(path: str) -> Any:
    """Функция, возвращающая список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, encoding="utf-8") as f:

            try:
                bank_file = json.load(f)
            except json.JSONDecodeError:
                return []

    except FileNotFoundError:
        return []

    return bank_file
