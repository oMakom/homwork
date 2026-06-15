import csv
import logging
from typing import Any, Dict, Hashable, List

import pandas as pd

logger = logging.getLogger("read_files")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/read_files.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_csv_file(file_path: str = "data/transactions.csv") -> List[Dict[Hashable, Any]]:
    """
    Функция читает cvs файл. Принимает на фход путь к файлу и выводит список словарей (при ошибках пустой список)
    Путь по умолчанию "data/transactions.csv"
    """
    logger.info(f"вызов read_csv_file с путем до файла: {file_path}")
    transactions: List[Dict[Hashable, Any]] = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            logger.info(f"read_csv_file чтение файла: {file_path}")
            read_cvs = csv.DictReader(f, delimiter=";")
            for row in read_cvs:
                if any(value for value in row.values() if value):
                    transactions.append(dict(row))
    except FileNotFoundError as er_file:
        logger.error(f"read_csv_file ошибка открытия файла: {er_file}")
    except Exception as e:
        logger.error(f"read_csv_file непредвиденная ошибка: ({e})")
    logger.info("read_csv_file завершение работы")
    return transactions


def read_excel_file(file_path: str = "data/transactions_excel.xlsx") -> List[Dict[Hashable, Any]]:
    """
    Функция читает exls файл. Принимает на фход путь к файлу и выводит список словарей (при ошибках пустой список)
    Путь по умолчанию "data/transactions_excel.xlsx"
    """
    logger.info(f"вызов read_excel_file с путем до файла: {file_path}")
    try:
        df = pd.read_excel(file_path)
        transactions = df.to_dict(orient="records")
        logger.info("read_excel_file завершение функции")
        return transactions
    except Exception as e:
        transactions = []
        logger.error(f"read_excel_file завершение функции с ошибкой({e}). На выходе пустой список")
        return transactions
