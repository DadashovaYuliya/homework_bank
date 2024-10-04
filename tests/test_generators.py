import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def list_by_currency():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]


@pytest.mark.parametrize(
    "currency, expected",
    [
        (
            "USD",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {
                        "amount": "9824.07",
                        "currency": {
                            "name": "USD",
                            "code": "USD"
                        }
                    },
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702"
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {
                        "amount": "79114.93",
                        "currency": {
                            "name": "USD",
                            "code": "USD"
                        }
                    },
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188"
                },
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {
                        "amount": "56883.54",
                        "currency": {
                            "name": "USD",
                            "code": "USD"
                        }
                    },
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229"
                },
            ],
        ),
        (
            "руб.",
            [
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {
                        "amount": "43318.34",
                        "currency": {
                            "name": "руб.",
                            "code": "RUB"
                        }
                    },
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160"
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {
                        "amount": "67314.70",
                        "currency": {
                            "name": "руб.",
                            "code": "RUB"
                        }
                    },
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657"
                },
            ],
        ),
         ("EUR", []),
    ],
)

def test_filter_by_currency(list_by_currency, currency, expected):
    """Положительный тест на отбор банковских операций по заданной валюте, в том числе при отсутствии валюты в списке"""
    assert list(filter_by_currency(list_by_currency, currency)) == expected


def test_filter_by_currency_zero():
     with pytest.raises(StopIteration):
         x = filter_by_currency([], "")
         assert next(x) == 'Нет операций'


def test_transaction_descriptions():
    """Положительный тест на возврат описания операций"""
    assert next(transaction_descriptions ([{
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702"}])) == 'Перевод организации'
    assert next(transaction_descriptions ([{
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188"}])) == 'Перевод со счета на счет'
    assert next(transaction_descriptions ([{
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                     "to": "Visa Platinum 8990922113665229"}])) == 'Перевод с карты на карту'


def test_transaction_no_descriptions_():
    """Положительный тест на возврат описания операций, если операция не указана"""
    with pytest.raises(StopIteration):
        x = transaction_descriptions([])
        assert next(x) == 'Нет операций'


# @pytest.fixture
# def segment():
#     return [(0, 5), (5, 10), (7, 7)]

@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 5, ['0000 0000 0000 0001',
             '0000 0000 0000 0002',
             '0000 0000 0000 0003',
             '0000 0000 0000 0004']),
        (5, 10, ['0000 0000 0000 0005',
                 '0000 0000 0000 0006',
                 '0000 0000 0000 0007',
                 '0000 0000 0000 0008',
                 '0000 0000 0000 0009']),
        (7, 7, [])
    ])

def test_card_number_generator(start, stop, expected):
    '''Тест на корректность форматирования номеров карт'''
    assert list(card_number_generator(start, stop)) == expected