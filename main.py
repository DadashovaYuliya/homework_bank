from src.external_api import get_transaction_amount_rub
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.utils import get_bank_transaction_data
from src.widget import get_date, mask_account_card

print(get_mask_card_number(7000792289606361))

print(get_mask_account(73654108430135874305))

print(mask_account_card("Maestro 1596837868705199"))

print(mask_account_card("Счет 64686473678894779589"))

print(mask_account_card("MasterCard 7158300734726758"))

print(mask_account_card("Счет 35383033474447895560"))

print(mask_account_card("Visa Classic 6831982476737658"))

print(mask_account_card("Visa Platinum 8990922113665229"))

print(mask_account_card("Visa Gold 5999414228426353"))

print(mask_account_card("Счет 73654108430135874305"))

print(get_date("2024-03-11T02:26:18.671407"))

print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        state="EXECUTED",
    )
)

print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)

print(get_bank_transaction_data("data/operations.json"))
print(get_bank_transaction_data("data/operation.json"))

print(
    get_transaction_amount_rub(
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        }
    )
)
