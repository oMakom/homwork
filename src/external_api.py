import os
from dotenv import load_dotenv
import requests


def exchange_rate(currency: str = "RUB") -> float:
    """
    Обращение к внешнему источнику для получения текущего курса валют и конвертации суммы операции в рубли
    Получает код курса валют, на выходе курс валюты по отношению к рублю
    """
    result = 1.0
    if currency == "USD" or currency == "EUR":
        load_dotenv()
        Api_Key = os.getenv("API_KEY")
        list_of_currencies = requests.get(f"https://currate.ru/api/?get=rates&pairs={currency}RUB&key={Api_Key}").json()
        try:
            result = list_of_currencies.get("data").get(currency+"RUB")
        except:
            return 1.0
    return result
