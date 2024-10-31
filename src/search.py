import re
from collections import Counter
from typing import Any


def get_transactions_by_row(list_bank: list, row: str) -> list[dict[Any, Any]]:
    """Функция, фильтрующая список транзакций по строке поиска"""
    filter_transaction = []
    for i in list_bank:
        if re.findall(row.lower(), str(i.get("description").lower())):
            filter_transaction.append(i)
    return filter_transaction


def get_category_counter(list_bank: list, list_categ: list) -> dict:
    '''Функция, возвращающая словарь с данными {категория:количество}'''
    filter_transaction = []
    list_categ_low = [i.lower() for i in list_categ]
    for i in list_bank:
        if i.get("description").lower() in list_categ_low:
            filter_transaction.append(i["description"])
    counted = Counter(filter_transaction)
    return counted
