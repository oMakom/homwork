import re

import src.utils as utils
import src.read_files as read_files
import src.processing as processing
import src.widget as widget


def main():
    # 1 запрос пользователя
    transactions = []
    while True:
        menu = input(
            """Привет! Добро пожаловать в программу работы с банковскими транзакциями.Выберите необходимый пункт меню:

                1. Получить информацию о транзакциях из JSON-файла  
                2. Получить информацию о транзакциях из CSV-файла  
                3. Получить информацию о транзакциях из XLSX-файла
            \nВвод данных: """)
        if menu == "1":
            transactions = utils.transaction_json_in_python()
            print("\nДля обработки выбран JSON-файл.\n")
            break
        if menu == "2":
            transactions = read_files.read_csv_file()
            print("\nДля обработки выбран CSV-файл.\n")
            break
        if menu == "3":
            transactions = read_files.read_csv_file()
            print("\nДля обработки выбран XLSX-файл.\n")
            break
        print("\nВведите кореектные данные\n")

    # 2 запрос статуса, по которому необходимо выполнить фильтрацию
    valid_states = ["EXECUTED", "CANCELED", "PENDING2"]
    while True:
        state_input = input("Введите статус, по которому необходимо выполнить фильтрацию."
                            "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING2"
                            "\n\nВвод данных: """)
        if any([state_input.lower() == state.lower() for state in valid_states]):
            if state_input.lower() == "executed":
                transactions_state_filtered = processing.filter_by_state(transactions, "EXECUTED")
                print("\nОперации отфильтрованы по статусу EXECUTED")
                break
            if state_input.lower() == "canceled":
                transactions_state_filtered = processing.filter_by_state(transactions, "CANCELED")
                print("\nОперации отфильтрованы по статусу CANCELED")
                break
            if state_input.lower() == "pending2":
                transactions_state_filtered = processing.filter_by_state(transactions, "PENDING2")
                print("\nОперации отфильтрованы по статусу PENDING2")
                break
        print(f"\nСтатус операции {state_input} недоступен.\n")

    # 3 сортировка по дате  и сортировка по возрастанию/убыванию
    while True:
        data_filtered_input = input("Отсортировать операции по дате? Да/Нет\nВвод данных: ")
        if data_filtered_input.lower() == "да":
            # Если сортировать то задаем вопрос по возрастанию/убыванию
            while True:
                sort_input = input("Отсортировать по возрастанию или по убыванию?\nВвод данных: ")
                if re.search(sort_input.lower(), 'по убыванию убывание'):
                    sort_data = True
                    break
                if re.search(sort_input.lower(), 'по возрастанию возрастание'):
                    sort_data = False
                    break
                print(f"Ввод '{sort_input}' не поддерживается")
            transactions_data_filtered = processing.sort_by_date(transactions_state_filtered, sort_data)
            break
        if data_filtered_input.lower() == "нет":
            transactions_data_filtered = transactions_state_filtered
            break
        print(f"Ввод '{data_filtered_input}' не поддерживается")

    # 4 вывод только рублевых транзакций?
    while True:
        rub_filtered_input = input("Выводить только рублевые транзакции? Да/Нет\nВвод данных: ")
        if rub_filtered_input.lower() == "да":
            rub_filtered_input = "да"
            break
        if rub_filtered_input.lower() == "нет":
            rub_filtered_input = "нет"
            break
        print(f"Ввод '{rub_filtered_input}' не поддерживается")
    if rub_filtered_input == "нет":
        transactions_rub_filtered = transactions_data_filtered
    if rub_filtered_input == "да":
        transactions_rub_filtered = []
        for transact in transactions_data_filtered:
                #если не exсel файл
                if menu != '3':
                    if transact.get("operationAmount").get("currency").get("code") == "RUB":
                        transactions_rub_filtered.append(transact)
                # если exсel файл
                if menu == '3':
                    if transact.get("currency_code") == "RUB":
                        transactions_rub_filtered.append(transact)

    # 5 отфильтровать по слову в описании?
    while True:
        text_filtered_input = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n"
                                   "Ввод данных: ")
        if text_filtered_input.lower() == "нет":
            transactions_search_filtered = transactions_rub_filtered
            break
        if text_filtered_input.lower() == "да":
            text_search_input = input("Введите текст для сортировки\nВвод данных: ")
            transactions_search_filtered = processing.process_bank_search(transactions_rub_filtered,
                                                                              text_search_input)
            break

    print("Распечатываю итоговый список транзакций...")
    if not transactions_search_filtered:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    if transactions_search_filtered:
        print(f"\nВсего банковских операций в выборке: {len(transactions_search_filtered)}")
        for transact_s in transactions_search_filtered:
            if transact_s:
                print(f"\n{widget.get_date(transact_s.get('date'))} {transact_s.get("description")}")
                #если в транцакции есть слово перевод
                if re.search("Перевод", transact_s.get("description")):
                    print(f"{widget.mask_account_card(transact_s.get("from"))} -> "
                          f"{widget.mask_account_card(transact_s.get("to"))}")
                else:
                    # если в транцакции нет слова перевод
                    print(f"{widget.mask_account_card(transact_s.get("to"))}")
                # если не exсel файл
                if menu != '3':
                    sum_amount = round(float(transact_s.get("operationAmount").get("amount")))
                    valut = transact_s.get("operationAmount").get("currency").get("name")
                    print(f"Сумма: {sum_amount} {valut}")
                # если exсel файл
                if menu == '3':
                    sum_amount = round(float(transact_s.get("amount")))
                    valut = transact_s.get("currency_name")
                    print(f"Сумма: {sum_amount} {valut}")


if __name__ == "__main__":
    main()


