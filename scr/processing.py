
def filter_by_state(transactions_list: list, state: str='EXECUTED') -> list:
    the_filtered_list = []

    for transactions in transactions_list:
        if transactions['state'] == state:
            the_filtered_list.append(transactions)

    return the_filtered_list