from unittest.mock import patch

import pytest

from src.external_api import get_transaction_amount_rub


@pytest.mark.parametrize(
    "transaction, amount",
    [
        (
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {"amount": "8221.37", "currency": {"name": "RUB", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560",
            },
            8221.37,
        ),
        (
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {"amount": "158221.37", "currency": {"name": "RUB", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560",
            },
            158221.37,
        ),
    ],
)
def test_get_transaction_amount_rub_positive(transaction: dict, amount: float) -> None:
    """Положительный тест работы функции без подключения по API"""
    assert get_transaction_amount_rub(transaction) == amount


@patch("src.external_api.requests.request")
def test_get_transaction_amount_rub(mock_get):
    """Тест на работу конвертации валюты с API"""
    mock_get.return_value.json.return_value = {
        "date": "2018-02-22",
        "historical": "",
        "info": {"rate": 5, "timestamp": 1519328414},
        "query": {"amount": 10, "from": "USD", "to": "RUB"},
        "result": 50.00,
        "success": True,
    }
    assert (
        get_transaction_amount_rub(
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {"amount": "10", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560",
            }
        )
        == 50.00
    )
