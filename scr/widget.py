import scr.masks as masks


def mask_account_card(payment_identifier: str) -> str:
    """
    обрабатывает информацию как о картах, так и о счетах
    Принимает строку, содержащую тип и номер карты или счета
    Возвращает строку с замаскированным номером
    """
    if payment_identifier is None or payment_identifier.find(" ") == -1:
        return "Введите корректные данные формата: Visa Platinum 7000792289606361"
    if not payment_identifier[payment_identifier.rfind(" ") + 1 :].isdigit():
        return "Ошибка ввода: тип карты/счет далее номер отделенные пробелом(Например: Visa Platinum 7000792289606361)"
    if "Счет" not in payment_identifier:
        return payment_identifier[0 : payment_identifier.rfind(" ") + 1] + masks.get_mask_card_number(
            payment_identifier[payment_identifier.rfind(" ") + 1 :]
        )
    else:
        return payment_identifier[0 : payment_identifier.rfind(" ") + 1] + masks.get_mask_account(
            payment_identifier[payment_identifier.rfind(" ") + 1 :]
        )
