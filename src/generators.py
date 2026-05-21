from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    for transaction in transactions:
        if transaction.get("operationAmount").get("currency").get("code") == currency:
            yield transaction
        else:
            continue


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    for transaction in transactions:
        if transaction.get("description"):
            yield transaction["description"]
        else:
            continue


def card_number_generator(start: int, end: int) -> Iterator[str]:
    if start > end:
        dubbl_start = start
        start = end
        end = dubbl_start

    for card_number in range(start, end+1):
        str_card_number = str(card_number)
        if len(str_card_number) > 16:
            break
        while len(str_card_number) < 16:
            str_card_number = "0" + str_card_number

        result_card_number = f"{str_card_number[0:4]} {str(str_card_number)[4:8]} {str(str_card_number)[8:12]} {str(str_card_number)[12:16]}"
        yield result_card_number