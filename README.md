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
