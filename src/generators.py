from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """
    Принимает на вход список словарей, представляющих транзакции и валюту операции
    Возвращает итератор, который поочередно выдает транзакции соответствующие заданной валюте операции
    """
    for transaction in transactions:
        if transaction.get("operationAmount").get("currency").get("code") == currency:
            yield transaction
        else:
            continue


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """
    Принимает список словарей с транзакциями
    Возвращает описание каждой операции по очереди
    """
    for transaction in transactions:
        if transaction.get("description"):
            yield transaction["description"]
        else:
            continue


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999
    """
    if str(start).isdigit() and str(stop).isdigit():
        #если все таки перепутали тип и написали строкой -> переобразуем в int
        if not isinstance(start, int):
            start=int(start)
        if not isinstance(stop, int):
            end=int(stop)
        #если значения "перепутаны" -> меняем местами
        if start > stop:
            dubbl_start = start
            start = stop
            stop = dubbl_start
        if start < 0:
            start = 0
        for card_number in range(start, stop + 1):
            #если номер карты вылезает за диапазон -> прерываем цикл
            if card_number > 9999999999999999:
                break

            str_card_number = f"{card_number:016d}"
            result_card_number = (
                f"{str_card_number[0:4]} {str(str_card_number)[4:8]} {str(str_card_number)[8:12]}"
                f" {str(str_card_number)[12:16]}"
            )
            yield result_card_number
