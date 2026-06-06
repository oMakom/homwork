import requests


def exchange_rate(currency: str = "RUB") -> float:
    """
    Обращение к внешнему источнику для получения текущего курса валют и конвертации суммы операции в рубли
    Получает код курса валют, на выходе курс валюты по отношению к рублю
    """
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    if currency == "RUB":
        return 1.0
    list_of_currencies = requests.get(url).json()
    try:
        result = list_of_currencies.get("Valute").get(currency).get("Value")
    except:
        return 1.0
    return result
