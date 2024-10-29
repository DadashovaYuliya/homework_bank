import unittest
from unittest.mock import patch

import pytest

from main import select_menu_item, select_operation_status, sorted_transaction_date, sorted_transaction_rub, \
    sorted_by_descriptions


@pytest.fixture
def list_transaction() -> list:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
]


@patch("main.read_excel")
@patch("main.input")
def test_select_menu_item(mock_input, mock_read_excel, list_transaction) -> None:
    mock_input.return_value = 3
    mock_read_excel.return_value = list_transaction()
    assert list_transaction() == select_menu_item()


@patch("main.input")
def test_select_operation_status(mock_input, list_transaction) -> None:
    mock_input.return_value = 'executed'
    assert select_operation_status(list_transaction) == list_transaction()


@patch("main.input")
def test_sorted_transaction_date(mock_input, list_transaction) -> None:
    mock_input.return_value = 'да'
    assert sorted_transaction_date(list_transaction) == list_transaction()


@patch("main.input")
def test_sorted_transaction_rub(mock_input, list_transaction) -> None:
    mock_input.return_value = 'да'
    assert sorted_transaction_rub(list_transaction) == list_transaction()


@patch("main.input")
def test_sorted_by_descriptions(mock_input, list_transaction) -> None:
    mock_input.return_value = 'да'
    assert sorted_by_descriptions(list_transaction) == list_transaction()
