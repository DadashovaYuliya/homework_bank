import json


def get_bank_transaction_data (path: str) -> list:
    try:
        with open(path, encoding='utf-8') as f:

            try:
                bank_file = json.load(f)
            except json.JSONDecodeError:
                return []

    except FileNotFoundError:
        return []

    return bank_file

