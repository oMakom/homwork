def get_mask_card_number(number_card: int | str) -> str:
    """
    принимает на вход номер карты и возвращает ее маску
    XXXX XX** **** XXXX
    """
    mask_card = ""
    counter = 1

    for num in str(number_card):
        if counter <= 6 or counter > len(str(number_card)) - 4:
            mask_card += str(num)
        else:
            mask_card += "*"
        if counter % 4 == 0:
            mask_card += " "
        counter += 1

    return mask_card


def get_mask_account(account_number: int | str) -> str:
    """
    принимает на вход номер счета и возвращает его маску
    **XXXX
    """
    mask_account = ""
    counter = 1

    for num in str(account_number):
        if counter > len(str(account_number)) - 4:
            mask_account += str(num)
        elif counter > len(str(account_number)) - 6:
            mask_account += "*"
        counter += 1

    return mask_account