import json


def transaction_json_in_python(json_path:str="data/operations.json") -> list | list[dict]:
    """
    Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях
    Путь по умолчанию 'data/operations.json'
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список
    """
    try:
        with open(json_path, encoding='utf-8') as data_file:
            transaction_data = json.load(data_file)
            if not isinstance(transaction_data, list):
                transaction_data = []
    except:
        transaction_data = []
    return transaction_data