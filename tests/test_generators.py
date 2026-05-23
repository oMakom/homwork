import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions() -> list[dict]:
    """Фикстура с образцом транзакций для тестирования."""
    transactions_list = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                },
            },
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]
    return transactions_list


def test_filter_by_currency(transactions: list[dict], currency: str = "USD") -> None:
    """Проверка корректных значений"""
    filter_by_currency_test = filter_by_currency(transactions, currency)
    assert next(filter_by_currency_test) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(filter_by_currency_test) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(filter_by_currency_test) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }


@pytest.mark.parametrize("currency", [" ", "Долар", 1232])
def test_filter_by_not_currency(transactions: list[dict], currency: str) -> None:
    """Проверка отсутствия корректных значений(Проверка Конца Итерации)"""
    filter_by_currency_test = filter_by_currency(transactions, currency)
    with pytest.raises(StopIteration):
        next(filter_by_currency_test)


@pytest.mark.parametrize("transactions_null, currency", [([], " "), ([], "Долар"), ([], 1232)])
def test_filter_by_note_transactions(transactions_null: list, currency: str) -> None:
    """Проверка отсутствия списка транзакций"""
    filter_by_currency_test = filter_by_currency(transactions_null, currency)
    with pytest.raises(StopIteration):
        next(filter_by_currency_test)


def test_transaction_descriptions(transactions: list[dict]) -> None:
    """Проверка корректных значений"""
    transaction_descriptions_test = transaction_descriptions(transactions)
    assert next(transaction_descriptions_test) == "Перевод организации"
    assert next(transaction_descriptions_test) == "Перевод со счета на счет"
    assert next(transaction_descriptions_test) == "Перевод со счета на счет"
    assert next(transaction_descriptions_test) == "Перевод с карты на карту"
    assert next(transaction_descriptions_test) == "Перевод организации"


def test_transaction_descriptions_note_transactions(transactions: list[dict] = ([])) -> None:
    """Проверка отсутствия списка транзакций"""
    transaction_descriptions_test = transaction_descriptions(transactions)
    with pytest.raises(StopIteration):
        next(transaction_descriptions_test)


def test_card_number_generator(start: int = 25, end: int = 30) -> None:
    """Проверка корректных значений"""
    card_number_generator_test = card_number_generator(start, end)
    assert next(card_number_generator_test) == "0000 0000 0000 0025"
    assert next(card_number_generator_test) == "0000 0000 0000 0026"
    assert next(card_number_generator_test) == "0000 0000 0000 0027"
    assert next(card_number_generator_test) == "0000 0000 0000 0028"
    assert next(card_number_generator_test) == "0000 0000 0000 0029"


def test_card_number_generator_revers(start: int = 30, end: int = 25) -> None:
    """Проверка некорректных(обратных) значений"""
    card_number_generator_test = card_number_generator(start, end)
    assert next(card_number_generator_test) == "0000 0000 0000 0025"
    assert next(card_number_generator_test) == "0000 0000 0000 0026"
    assert next(card_number_generator_test) == "0000 0000 0000 0027"
    assert next(card_number_generator_test) == "0000 0000 0000 0028"
    assert next(card_number_generator_test) == "0000 0000 0000 0029"


@pytest.mark.parametrize("start, end", [("кпцу", 25), ("", ""), (0, ""), (-5, 10)])
def test_card_number_generator_boundary_values(start: int, end: int) -> None:
    """Проверка некорректных(текстовых) значений"""
    card_number_generator_test = card_number_generator(start, end)
    with pytest.raises(StopIteration):
        next(card_number_generator_test)


def test_card_number_generator_uncorrected(start: int = 9999999999999999, end: int = 199999999999999999) -> None:
    """Проверка некорректных(граничных) значений"""
    card_number_generator_test = card_number_generator(start, end)
    assert next(card_number_generator_test) == "9999 9999 9999 9999"
    with pytest.raises(StopIteration):
        next(card_number_generator_test)
