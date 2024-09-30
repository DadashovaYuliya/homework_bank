import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "account_id, masks",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(account_id: str, masks: str):
    """Положительный тест на маскировку карты или счета"""
    assert mask_account_card(account_id) == masks


def test_mask_account_card_number_len():
    """Тест на некорректную длину или отсутствие ввода"""
    assert mask_account_card("Maestro 700079228960636125") == "Некорректный ввод данных"
    assert mask_account_card("") == "Введите данные счета или карты"


@pytest.mark.parametrize(
    "str_date, masks",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2022-05-15T06:15:39.574852", "15.05.2022"),
        ("2023-12-02T23:18:45", "02.12.2023"),
        ("2024-11-15", "15.11.2024"),
    ],
)
def test_get_date(str_date: str, masks: str):
    """Положительный тест на форматирование даты"""
    assert get_date(str_date) == masks


def test_get_date_no_data():
    """Тест на отсутствие ввода"""
    assert get_date("") == "Некорректный ввод данных"
