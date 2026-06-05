import requests


def exchange_rate(currency:str="RUB") -> float:
    """
    Обращение к внешнему источнику для получения текущего курса валют и конвертации суммы операции в рубли
    Получает код краса валют, на выходе курс валюты по отношению к рублю
    """
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    list_of_currencies = requests.get(url).json()
    if currency == "RUB":
        return 1.0
    try:
        result = list_of_currencies.get("Valute").get(currency).get("Value")
    except:
        return 1.0
    return result
