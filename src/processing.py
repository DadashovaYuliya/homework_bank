def filter_by_state (new_data: list, state = 'EXECUTED') -> list:
    ''''Функция, фильтрующая список словарей по ключу и значениею state = "EXECUTED"'''
    filter_dict = []
    for i in new_data:
        if i['state'] =='EXECUTED':
            filter_dict.append(i)
    return filter_dict
