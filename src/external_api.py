import os
import logging
import requests
from dotenv import load_dotenv


logger = logging.getLogger("external_api.py")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/external_api.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def exchange_rate(currency: str = "RUB") -> float:
    """
    Обращение к внешнему источнику для получения текущего курса валют и конвертации суммы операции в рубли
    Получает код курса валют, на выходе курс валюты по отношению к рублю
    """
    logger.info(f"вызов exchange_rate для валюты : {currency}")
    result = 1.0
    if currency == "USD" or currency == "EUR":
        load_dotenv()
        Api_Key = os.getenv("API_KEY")
        list_of_currencies = requests.get(
            f"https://currate.ru/api/?get=rates&pairs={currency}RUB&key={Api_Key}"
        ).json()
        try:
            result = list_of_currencies.get("data").get(currency + "RUB")
            logger.info(f"exchange_rate полученние данных по курсу валют({currency}: {result})")
        except Exception as e:
            logger.error(f"exchange_rate ошибка получение курса по {currency}: {e})")
            return 1.0
    return result
