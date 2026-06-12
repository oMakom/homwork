import csv
import logging
import pandas as pd
from typing import Any, Dict, List


logger = logging.getLogger("read_files")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/read_files.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_cvs_file(file_path):
    logger.info(f"вызов read_cvs_file с путем до файла: {file_path}")
    transactions: List[Dict[str, Any]] = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            logger.info(f"read_cvs_file чтение файла: {file_path}")
            read_cvs = csv.DictReader(f, delimiter=";")
            for row in read_cvs:
                if any(value for value in row.values() if value):
                    transactions.append(dict(row))
    except  FileNotFoundError as er_file:
        logger.error(f"read_cvs_file ошибка открытия файла: {er_file}")
    except Exception as e:
        logger.error(f"read_cvs_file непредвиденная ошибка: ({e})")
    logger.info("read_cvs_file завершение работы")
    return transactions


def read_exel_file(file_path):
    logger.info(f"вызов read_exel_file с путем до файла: {file_path}")
    try:
        df = pd.read_excel(file_path)
        transactions = df.to_dict(orient="records")
        logger.info(f"read_exel_file завершение функции")
        return transactions
    except Exception as e:
        transactions: List[Dict[str, Any]] = []
        logger.error(f"read_exel_file завершение функции с ошибкой({e}). На выходе пустой список")
        return transactions
