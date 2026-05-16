from datetime import datetime

import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("num_card, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("", "Введите корректные данные формата: Visa Platinum 7000792289606361"),
        (
            "Visa Platinum  ",
            "Ошибка ввода: тип карты/счет далее номер отделенные пробелом(Например: Visa Platinum 7000792289606361)",
        ),
        (
            " 7000792289606361",
            "Ошибка ввода: введите тип карты/счет (Например: Visa Platinum ****, Счет ****, Maestro ****)",
        ),
        (
            "Visa 70 00792 289606 361",
            "Ошибка ввода: тип карты/счет далее номер отделенные пробелом(Например: Visa Platinum 7000792289606361)",
        ),
    ],)
def test_mask_account_card(num_card: str, expected: str) -> None:
    assert mask_account_card(num_card) == expected


@pytest.mark.parametrize("date, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"),],)
def test_get_date(date: str, expected: str) -> None:
    assert get_date(date) == expected


@pytest.mark.parametrize("date", ["2024-03-1143", "", "20262012"])
def test_get_date_wrong_type(date) -> None:
    with pytest.raises(ValueError):
        datetime.fromisoformat(date)
