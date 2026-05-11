def filter_by_state(transactions_list: list, state: str = "EXECUTED") -> list:
    """
    Принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Возвращает новый список словарей, содержащий только те словари, у которых state соответствует указанному значению
    """
    the_filtered_list = []

    for transactions in transactions_list:
        if transactions["state"] == state:
            the_filtered_list.append(transactions)

    return the_filtered_list


def sort_by_date(transactions_list: list, is_reverse: bool = True) -> list:
    """
    Принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате
    """
    the_sorted_list = sorted(transactions_list, key=lambda key_date: key_date["date"], reverse=is_reverse)

    return the_sorted_list
