from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account: str) -> str:
    """Функция, которая обрабатывает информацию о картах и счетах и возвращает соответствующую маску"""
    account_list = account.split()
    mask = ""

    for i in account_list:
        if i.isalpha():
            mask += i + " "
        elif i.isdigit() and len(i) == 16:
            mask += get_mask_card_number (i)
        elif i.isdigit() and len(i) == 20:
            mask += get_mask_account (i)

    return mask


def get_date (str_data: str) -> str:
    """Функция, форматирующая строку даты"""
    return f"{str_data[8:10]}.{str_data[5:7]}.{str_data[:4]}"