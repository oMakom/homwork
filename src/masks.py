import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(number_card: int | str) -> str:
    """
    принимает на вход номер карты и возвращает ее маску
    XXXX XX** **** XXXX
    """
    logger.info(f"get_mask_card_number принимает номер карты: {number_card}")
    mask_card = ""
    counter = 1
    without_spaces_number_card = str(number_card).replace(" ", "")

    for num in str(without_spaces_number_card):
        if num.isalpha():
            logger.error('get_mask_card_number ошибка "Буквенный ввод недопустим". Завершение функции')
            return "Буквенный ввод недопустим"
        if num == " ":
            continue
        if counter <= 6 or counter > len(str(without_spaces_number_card)) - 4:
            mask_card += str(num)
        else:
            mask_card += "*"
        if counter % 4 == 0 and counter < len(str(without_spaces_number_card)):
            mask_card += " "
        counter += 1
    logger.info("get_mask_card_number завершение обработки номера карты")
    return mask_card


def get_mask_account(account_number: int | str) -> str:
    """
    принимает на вход номер счета и возвращает его маску
    **XXXX
    """
    logger.info(f"get_mask_account принимает номер счета: {account_number}")
    mask_account = ""
    counter = 1
    without_spaces_account_number = str(account_number).replace(" ", "")

    for num in str(without_spaces_account_number):
        if num.isalpha():
            logger.error('get_mask_account ошибка "Буквенный ввод недопустим". Завершение функции')
            return "Буквенный ввод недопустим"
        if counter > len(str(without_spaces_account_number)) - 4:
            mask_account += str(num)
        elif counter > len(str(without_spaces_account_number)) - 6:
            mask_account += "*"
        counter += 1
    logger.info("get_mask_account завершение обработки номера счета")
    return mask_account
