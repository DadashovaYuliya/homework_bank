# ПРОЕКТ БАНК

## Описание:

Проект банк - это виджет, который показывает несколько последних успешных банковских операций клиента.

## Установка:

1. Клонируйте репозиторий:
```
git@github.com:DadashovaYuliya/homework_bank.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Использование функций:

mask_account_card - принимает наименование карты или счета с номером в формате строки 
и возвращает соответствующую маску в формате "Наименование ХХХХ ХХ** **** ХХХХ" - для карты
и "Счет **ХХХХ" - для счета

get_date - принимает дату в формате "2024-03-11T02:26:18.671407" и возвращает дату в формате "11.03.2024"

filter_by_state - принимает список словарей с данными о банковских операциях 
и возвращает отсортированный список по заданному статусу

sort_by_date - принимает список словарей с данными о банковских операциях 
и возвращает отсортированный список по возрастанию или убыванию даты

filter_by_currency - принимает список словарей с данными о банковских операциях 
и возвращает отсортированный список по заданной валюте операции

transaction_descriptions - принимает список словарей с данными о банковских операциях 
и возвращает описание операции

card_number_generator - функция генерации номера карт заданного количества в формате 
ХХХХ ХХХХ ХХХХ

## Тестирование:
Для модулей masks.py, processing.py, widget.py, generators.py реализованы тесты:
```
Name                       Stmts   Miss  Cover
----------------------------------------------
src\__init__.py                0      0   100%
src\generators.py             26      0   100%
src\masks.py                  11      0   100%
src\processing.py              8      0   100%
src\widget.py                 18      0   100%
tests\__init__.py              0      0   100%
tests\test_generators.py      23      0   100%
tests\test_masks.py           15      0   100%
tests\test_processing.py      16      1    94%
tests\test_widget.py          13      0   100%
----------------------------------------------
TOTAL                        130      1    99%

```
