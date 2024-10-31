from typing import Any

from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.read_file import read_csv, read_excel
from src.search import get_transactions_by_row
from src.utils import get_bank_transaction_data
from src.widget import get_date, mask_account_card


def select_menu_item() -> list:
    """Функция, получающая список транзакций из формата файла, выбранного пользователем"""
    user_input = int(
        input(
            """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла\n"""
        )
    )
    try:
        list_bank = []
        if user_input == 1:
            print("Для обработки выбран JSON-файл")
            list_bank = get_bank_transaction_data("data/operations.json")
        elif user_input == 2:
            print("Для обработки выбран CSV-файл")
            list_bank = read_csv("data/transactions.csv")
        elif user_input == 3:
            print("Для обработки выбран XLSX-файл")
            list_bank = read_excel("G:/Downloads/transactions_excel.xlsx")

        return list_bank

    except Exception as ex:
        print(f"Произошла ошибка {ex}.")
        return []


def select_operation_status(list_bank: list) -> list:
    """Функция, получающая список транзакций по статусу, выбранному пользователем"""
    list_status = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        user_input = str(
            input(
                """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"""
            ).upper()
        )
        if user_input in list_status:
            print(f"Операции отфильтрованы по статусу {user_input}.")
            list_bank = filter_by_state(list_bank, user_input)
            break
        else:
            print(f"По статусу {user_input} операции не найдены.")
    return list_bank


def sorted_transaction_date(list_bank: list) -> list:
    """Функция, сортирующая транзакции по дате в соответствии с запросом пользователя"""
    user_input = input("Отсортировать операции по дате? Да/Нет.\n").lower()
    if user_input == "да":
        user_input = input("Отсортировать по возрастанию или по убыванию?? По возрастанию/По убыванию.\n").lower()

        if user_input == "по возрастанию":
            sort_order = False
        else:
            sort_order = True

        list_bank = sort_by_date(list_bank, sort_order)
    return list_bank


def sorted_transaction_rub(list_bank: list) -> list:
    """Функция, сортирующая транзакции по валюте в соответствии с запросом пользователя"""
    user_input = input("Выводить только рублевые тразакции? Да/Нет.\n").lower()
    if user_input == "да":
        list_bank = filter_by_currency(list_bank, "RUB")
        return list(list_bank)
    else:
        return list_bank


def sorted_by_descriptions(list_bank: list) -> list:
    """Функция, сортирующая транзакции по слову в описании в соответствии с запросом пользователя"""
    user_input = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет.\n").lower()
    if user_input == "да":
        input_search = input("Введите слово:\n")
        list_bank = get_transactions_by_row(list_bank, input_search)
    return list_bank


def get_final_list(list_bank: list) -> Any:
    """Функция, выводящая транзакции в соответствии с запросом пользователя"""
    if len(list_bank) == 0:
        print("Не найдено транзакций с заданными условиями.")
    else:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке {len(list_bank)}.")

    for transaction in list_bank:
        date = get_date(transaction.get("date"))
        print(f"{date} {transaction.get('description')}")

        try:
            mask_from = mask_account_card(transaction["from"])
            print(f"{mask_from} -> ", end="")
        except KeyError:
            print('', end='')
        except AttributeError:
            print('', end='')
        except IndexError:
            print('', end='')
        mask_to = mask_account_card(transaction["to"])

        try:
            amount = transaction["amount"]
        except KeyError:
            amount = transaction["operationAmount"]["amount"]
        try:
            currency = transaction["currency_name"]
        except KeyError:
            currency = transaction["operationAmount"]["currency"]["name"]
        print(f"{mask_to} \nСумма: {amount} {currency}")


def main():
    """Запуск программы"""
    list_bank = select_menu_item()
    list_bank = select_operation_status(list_bank)
    list_bank = sorted_transaction_date(list_bank)
    list_bank = sorted_transaction_rub(list_bank)
    list_bank = sorted_by_descriptions(list_bank)
    get_final_list(list_bank)


print(main())
