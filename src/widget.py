from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account: str) -> str:
    """Функция, которая обрабатывает информацию о картах и счетах и возвращает соответствующую маску"""
    # if len(account) == 0:
    #     return "Введите данные счета или карты"

    account_list = account.split()

    if len(account_list[-1]) == 16:
        mask_card_number = get_mask_card_number(account_list[-1])
        account_list[-1] = mask_card_number
        return " ".join(account_list)

    elif len(account_list[-1]) == 20:
        mask_account = get_mask_account(account_list[-1])
        account_list[-1] = mask_account
        return " ".join(account_list)

    return "Некорректный ввод данных"


def get_date(str_data: str) -> str:
    """Функция, форматирующая строку даты"""
    if len(str_data) > 0:
        return f"{str_data[8:10]}.{str_data[5:7]}.{str_data[:4]}"

    return "Некорректный ввод данных"
