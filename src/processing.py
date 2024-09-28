def filter_by_state(new_dict: list, state: str = "EXECUTED") -> list:
    """'Функция, фильтрующая список банковских операций по заданному статусу"""
    filter_dict = []
    for i in new_dict:
        if i.get("state") == state:
            filter_dict.append(i)
    return filter_dict


def sort_by_date(new_dict: list, sort_order: bool = True) -> list:
    """'Функция, сортирующая список банковских операций по дате возрастания или убывания"""
    return sorted(new_dict, key=lambda x: x["date"], reverse=sort_order)
