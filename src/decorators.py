from functools import wraps
from typing import Any, Optional


def log(filename: Optional[str] = None):
    """
    Декоратор: логирует  начало и конец выполнения функции, ее результаты или возникшие ошибки.
    Принимает необязательный аргумент 'filename', который определяет,
    куда будут записываться логи (в файл или в консоль)
    """
    def log_decorator(function: Any):
        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any):
            name_func = function.__name__
            try:
                try_result = function(*args, **kwargs)
                log_message = f"{name_func} ok"
                if filename:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(log_message + "\n")
                else:
                    print(log_message)
                return try_result
            except Exception as error:
                error_log_message = f"{name_func} error: {error}. Inputs: args={args}, kwargs={kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(error_log_message + "\n")
                else:
                    print(error_log_message)

        return wrapper

    return log_decorator
