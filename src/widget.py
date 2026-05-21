import src.masks as masks


def mask_account_card(payment_identifier: str) -> str:
    """
    обрабатывает информацию как о картах, так и о счетах
    Принимает строку, содержащую тип и номер карты или счета
    Возвращает строку с замаскированным номером
    """
    # На старте ищем первую позицию циферного знака
    position_digital = -1
    for pos in payment_identifier:
        position_digital += 1
        if pos.isdigit():
            break

    if payment_identifier is None or payment_identifier.find(" ") == -1:
        return "Введите корректные данные формата: Visa Platinum 7000792289606361"
    if not payment_identifier[position_digital:].isdigit():
        return "Ошибка ввода: тип карты/счет далее номер отделенные пробелом(Например: Visa Platinum 7000792289606361)"
    if not payment_identifier[:position_digital].replace(" ", "").isalpha():
        return "Ошибка ввода: введите тип карты/счет (Например: Visa Platinum ****, Счет ****, Maestro ****)"
    if "Счет" not in payment_identifier:
        return payment_identifier[0 : payment_identifier.rfind(" ") + 1] + masks.get_mask_card_number(
            payment_identifier[payment_identifier.rfind(" ") + 1 :]
        )
    else:
        return payment_identifier[0 : payment_identifier.rfind(" ") + 1] + masks.get_mask_account(
            payment_identifier[payment_identifier.rfind(" ") + 1 :]
        )


def get_date(date_time: str) -> str:
    """
    Принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    Возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")
    При вводе неподдерживаемого формата, пишет ошибку
    """
    from datetime import datetime

    try:
        formatted_date = datetime.fromisoformat(date_time)
        return formatted_date.strftime("%d.%m.%Y")
    except ValueError:
        return "Ошибка ввода: Введите кооректные данные по дате в ISO виде (например: 2024-03-11T02:26:18.671407)"
