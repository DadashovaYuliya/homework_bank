from unittest.mock import mock_open, patch

import pandas as pd
import pytest

from src.read_file import read_csv, read_excel


@pytest.fixture
def test_df() -> pd.DataFrame:
    """Фикстура, создающая тестовый DataFrame"""

    test_dict = {
        "id": [650703.0, 3598919.0],
        "state": ["EXECUTED", "EXECUTED"],
        "date": ["2023-09-05T11:30:32Z", "2020-12-06T23:00:58Z"],
        "amount": [16210.0, 29740.0],
        "currency_name": ["Sol", "Peso"],
        "currency_code": ["PEN", "COP"],
        "from": ["Счет 58803664561298323391", "Discover 3172601889670065"],
        "to": ["Счет 39745660563456619397", "Discover 0720428384694643"],
        "description": ["Перевод организации", "Перевод с карты на карту"],
    }

    return pd.DataFrame(test_dict)


@patch("src.read_file.csv.DictReader")
def test_read_csv(mock_reader):
    m = mock_open()
    mock_reader.return_value = [
        {"id": "650703", "state": "EXECUTED", "date": "2023-09-05T11:30:32Z", "amount": "16210"}
    ]

    with patch("builtins.open", m) as mocked_open:
        assert read_csv("data/transactions.csv") == [
            {"id": "650703", "state": "EXECUTED", "date": "2023-09-05T11:30:32Z", "amount": "16210"}
        ]

        mocked_open.assert_called_with("data/transactions.csv", encoding="utf-8")


def test_read_csv_with_incorrect_path():
    """Тест с некорректным путем"""

    assert read_csv("") == [{}]


@patch("src.read_file.pd.read_excel")
def test_read_excel(mock_read, test_df):
    mock_read.return_value = test_df
    assert read_excel("G:/Downloads/transactions_excel.xlsx") == test_df.to_dict(orient="records")
    mock_read.assert_called_once_with("G:/Downloads/transactions_excel.xlsx")


def test_read_excel_with_incorrect_path():
    """Тест с некорректным путем"""

    assert read_excel("") == [{}]
