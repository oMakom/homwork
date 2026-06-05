import json
import src.external_api as external_api


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


def transaction_amount(transaction:dict) -> float:
    """
    принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float
    Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения
    текущего курса валют и конвертации суммы операции в рубли
    """
    if transaction.get("operationAmount").get("currency").get("code") and transaction.get("operationAmount").get("amount"):
        operation_code = transaction.get("operationAmount").get("currency").get("code")
        operation_amount = transaction.get("operationAmount").get("amount")
        result_value = round(float(operation_amount) * float(external_api.exchange_rate(operation_code)), 2)
        return result_value
    else:
        return 0
