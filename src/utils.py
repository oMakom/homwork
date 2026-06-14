import json
import logging

import src.external_api as external_api

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def transaction_json_in_python(json_path: str = "data/operations.json") -> list | list[dict]:
    """
    Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях
    Путь по умолчанию 'data/operations.json'
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список
    """
    logger.info(f"Вызов transaction_json_in_python с путем до JSON-файла({json_path})")
    try:
        logger.info("transaction_json_in_python попытка открытия файла транзакций")
        with open(json_path, encoding="utf-8") as data_file:
            transaction_data = json.load(data_file)
            if not isinstance(transaction_data, list):
                logger.error("transaction_json_in_python данные не список, отдаем пустой список")
                transaction_data = []
    except (FileNotFoundError, PermissionError, UnicodeDecodeError, json.JSONDecodeError) as e:
        logger.error(f"transaction_json_in_python ошибка {e} ; отдаем пустой список")
        transaction_data = []
    logger.info("transaction_json_in_python чтение файла транзакций завершено")
    return transaction_data


def transaction_amount(transaction: dict) -> float:
    """
    принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float
    Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения
    текущего курса валют и конвертации суммы операции в рубли
    """
    logger.info("Вызов функции transaction_amount")
    if transaction.get("operationAmount").get("currency").get("code") and transaction.get("operationAmount").get(
        "amount"
    ):
        operation_code = transaction.get("operationAmount").get("currency").get("code")
        operation_amount = transaction.get("operationAmount").get("amount")
        result_value = round(float(operation_amount) * float(external_api.exchange_rate(operation_code)), 2)
        logger.info("transaction_amount успешное выполнение функции")
        return result_value
    else:
        logger.error("transaction_amount ошибка выполнения, сумма транзакций будет равна 0")
        return 0
