import logging
import re

import src.processing as processing
import src.read_files as read_files
import src.utils as utils
import src.widget as widget

logger = logging.getLogger("Main")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/main.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def main() -> None:
    """
    Отвечает за основную логику проекта и связывает функциональности между собой
    """
    # 1 запрос пользователя
    logger.info("main Вызов функции")
    logger.info("main Запрос пользователю откуда получать данные(1: JSON,2: CSV,3: XLSX)")
    transactions: list[dict] = []
    while True:
        menu = input(
            """Привет! Добро пожаловать в программу работы с банковскими транзакциями.Выберите необходимый пункт меню:

                1. Получить информацию о транзакциях из JSON-файла
                2. Получить информацию о транзакциях из CSV-файла
                3. Получить информацию о транзакциях из XLSX-файла
            \nВвод данных: """
        )
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
        logger.error(f"main пользователь выбрал неверный пункт: {menu}")
    logger.info(f"main пользователь выбрал пункт: {menu}")
    # 2 запрос статуса, по которому необходимо выполнить фильтрацию
    valid_states = ["EXECUTED", "CANCELED", "PENDING"]
    logger.info("main Запрос пользователю по статусу операции (EXECUTED, CANCELED, PENDING)")
    while True:
        state_input = input(
            "Введите статус, по которому необходимо выполнить фильтрацию."
            "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
            "\n\nВвод данных: "
            ""
        )
        if any([state_input.lower() == state.lower() for state in valid_states]):
            if state_input.lower() == "executed":
                transactions_state_filtered = processing.filter_by_state(transactions, "EXECUTED")
                print("\nОперации отфильтрованы по статусу EXECUTED")
                break
            if state_input.lower() == "canceled":
                transactions_state_filtered = processing.filter_by_state(transactions, "CANCELED")
                print("\nОперации отфильтрованы по статусу CANCELED")
                break
            if state_input.lower() == "pending":
                transactions_state_filtered = processing.filter_by_state(transactions, "PENDING")
                print("\nОперации отфильтрованы по статусу PENDING")
                break
        print(f"\nСтатус операции {state_input} недоступен.\n")
        logger.error(f"main Пользователь выбрал неверный статус операции: {state_input}")
    logger.info(f"main Пользователь выбрал статус операции: {state_input}")
    # 3 сортировка по дате  и сортировка по возрастанию/убыванию
    logger.info("main Запрос пользователю по сортировке операций по дате")
    while True:
        data_filtered_input = input("Отсортировать операции по дате? Да/Нет\nВвод данных: ")
        if data_filtered_input.lower() == "да":
            logger.info("main Пользователю согласился на сортировку по дате")
            # Если сортировать то задаем вопрос по возрастанию/убыванию
            while True:
                sort_input = input("Отсортировать по возрастанию или по убыванию?\nВвод данных: ")
                if re.search(sort_input.lower(), "по убыванию убывание"):
                    logger.info("main Выбрана сортировка по убыванию")
                    sort_data = True
                    break
                if re.search(sort_input.lower(), "по возрастанию возрастание"):
                    logger.info("main Выбрана сортировка по возрастанию")
                    sort_data = False
                    break
                logger.info(f"main неверный ответ пользователя на сортироку по убыванию/возрвсианию: {sort_input}")
                print(f"Ввод '{sort_input}' не поддерживается")
            transactions_data_filtered = processing.sort_by_date(transactions_state_filtered, sort_data)
            break
        if data_filtered_input.lower() == "нет":
            logger.info("main Отказ пользователем от сортировки")
            transactions_data_filtered = transactions_state_filtered
            break
        print(f"Ввод '{data_filtered_input}' не поддерживается")
        logger.info(f"main неверный ответ пользователя на сортировку по дате: {data_filtered_input}")
    # 4 вывод только рублевых транзакций?
    logger.info("main Запрос пользователю на вывод транзакций только в рублях")
    while True:
        rub_filtered_input = input("Выводить только рублевые транзакции? Да/Нет\nВвод данных: ")
        if rub_filtered_input.lower() == "да":
            rub_filtered_input = "да"
            logger.info("main Пользователь согласился на вывод транзакций только в рублях")
            break
        if rub_filtered_input.lower() == "нет":
            rub_filtered_input = "нет"
            logger.info("main Пользователь согласился на вывод транзакций только в рублях")
            break
        logger.info(f"main неверный ответ пользователя на вывод транзакций только в рублях: {rub_filtered_input}")
        print(f"Ввод '{rub_filtered_input}' не поддерживается")
    if rub_filtered_input == "нет":
        transactions_rub_filtered = transactions_data_filtered
    if rub_filtered_input == "да":
        transactions_rub_filtered = []
        logger.info("main Выборка из транзакций только рублевых")
        for transact in transactions_data_filtered:
            # если не exсel файл
            if menu != "3":
                if transact.get("operationAmount").get("currency").get("code") == "RUB":
                    transactions_rub_filtered.append(transact)
            # если exсel файл
            if menu == "3":
                if transact.get("currency_code") == "RUB":
                    transactions_rub_filtered.append(transact)
        logger.info("main Окончание выборки из транзакций только рублевых")

    # 5 отфильтровать по слову в описании?
    logger.info("main Запрос пользователю на фильтрацию по слову в описании")
    while True:
        text_filtered_input = input(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n" "Ввод данных: "
        )
        if text_filtered_input.lower() == "нет":
            logger.info("main отказ пользователя на фильтрацию по слову в описании")
            transactions_search_filtered = transactions_rub_filtered
            break
        if text_filtered_input.lower() == "да":
            logger.info("main пользователя согласился на фильтрацию по слову в описании")
            text_search_input = input("Введите текст для сортировки\nВвод данных: ")
            transactions_search_filtered = processing.process_bank_search(transactions_rub_filtered, text_search_input)
            logger.info(f"main пользователь выбрал сортировку по выражению: {text_search_input}")
            break
    logger.info("main Вывод функцией финальных показателей")
    print("Распечатываю итоговый список транзакций...")
    if not transactions_search_filtered:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    if transactions_search_filtered:
        print(f"\nВсего банковских операций в выборке: {len(transactions_search_filtered)}")
        for transact_s in transactions_search_filtered:
            if transact_s:
                print(f"\n{widget.get_date(transact_s.get('date'))} {transact_s.get("description")}")
                # если в транцакции есть слово перевод
                if re.search("Перевод", transact_s.get("description")):
                    print(
                        f"{widget.mask_account_card(transact_s.get("from"))} -> "
                        f"{widget.mask_account_card(transact_s.get("to"))}"
                    )
                else:
                    # если в транцакции нет слова перевод
                    print(f"{widget.mask_account_card(transact_s.get("to"))}")
                # если не exсel файл
                if menu != "3":
                    sum_amount = round(float(transact_s.get("operationAmount").get("amount")))
                    valut = transact_s.get("operationAmount").get("currency").get("name")
                    print(f"Сумма: {sum_amount} {valut}")
                # если exсel файл
                if menu == "3":
                    sum_amount = round(float(transact_s.get("amount")))
                    valut = transact_s.get("currency_name")
                    print(f"Сумма: {sum_amount} {valut}")
        logger.info("main окончание работы функции")


if __name__ == "__main__":
    main()
