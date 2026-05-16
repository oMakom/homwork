def filter_by_state(transactions_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Возвращает новый список словарей, содержащий только те словари, у которых state соответствует указанному значению
    """
    the_filtered_list = []

    for transactions in transactions_list:
        if transactions["state"] == state:
            the_filtered_list.append(transactions)

    return the_filtered_list


def sort_by_date(transactions_list: list[dict], is_reverse: bool = True) -> list[dict] | str:
    """
    Принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате
    Выдает строку с ошибкой,если указана некорректная дата в транзакции с указанием ее ID
    """
    try:
        from datetime import datetime

        for transactions in transactions_list:
            id_transactions = transactions["id"]
            datetime.fromisoformat(transactions["date"])
    except ValueError:
        return (f"Ошибка ввода: Введите кооректные данные по дате в ISO виде (например: 2024-03-11T02:26:18.671407) в "
                f"транзакции ID {id_transactions}")

    the_sorted_list = sorted(transactions_list, key=lambda key_date: key_date["date"], reverse=is_reverse)

    return the_sorted_list
