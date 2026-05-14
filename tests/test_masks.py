import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("num_card, expected", [(7000792289606361, "7000 79** **** 6361"),
                                                ("700079228960636", "7000 79** ***0 636"),
                                                ("7000792", "7000 792"),
                                                ("", ""),
                                                ("абц", "Буквенный ввод недопустим"),
                                                ("70 0079 2289 6063 6", "7000 79** ***0 636"),])
def test_get_mask_card_number(num_card: str | int, expected: str) -> None:
    assert get_mask_card_number(num_card) == expected


@pytest.mark.parametrize("num_card, expected", [(7000792289606361, "**6361"),
                                                ("700079228960636", "**0636"),
                                                ("7000792", "**0792"),
                                                ("", ""),
                                                ("абс", "Буквенный ввод недопустим"),
                                                ("70 0079 2289 6063 6", "**0636"),])
def test_get_mask_account(num_card: str | int, expected: str) -> None:
    assert get_mask_account(num_card) == expected
