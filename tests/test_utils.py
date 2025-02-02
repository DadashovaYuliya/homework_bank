import pytest

from src.utils import get_bank_transaction_data


@pytest.mark.parametrize(
    "path, result",
    [
        (
            "data/test_operation.json",
            [
                {
                    "id": 441945886,
                    "state": "EXECUTED",
                    "date": "2019-08-26T10:50:58.294041",
                    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Maestro 1596837868705199",
                    "to": "Счет 64686473678894779589",
                },
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                    "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "MasterCard 7158300734726758",
                    "to": "Счет 35383033474447895560",
                },
            ],
        ),
        ("data/test.json", []),
    ],
)
def test_get_bank_transaction_data(path: str, result: list) -> None:
    """Тест на получение списка транзакций из json-файла"""
    assert get_bank_transaction_data(path) == result
