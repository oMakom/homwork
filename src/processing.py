import re
from collections import defaultdict

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


def process_bank_search(data:list[dict], search:str) -> list[dict]:
    """
    Принимать список словарей с данными о банковских операциях и строку поиска, а возвращать список словарей,
    у которых в описании есть данная строка
    """
    result = []
    for transaction in data:
        if transaction.get("description") and re.search(search.lower(), transaction["description"].lower()):
            result.append(transaction)
    return result


def process_bank_operations(data:list[dict], categories:list) -> dict:
    """
    Принимает список словарей с данными о банковских операциях и список категорий операций, а возвращает словарь,
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
    Категории операций хранятся в поле description
    """
    result_dict = defaultdict(int)
    for transaction in data:
        for category in categories:
            if transaction.get("description") and (category.lower() == transaction["description"].lower()):
                result_dict[transaction["description"]] += 1
    return dict(result_dict)