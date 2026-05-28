from functools import wraps
from typing import Any, Optional


def log(filename: Optional[str] = None):
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
            except Exception as error:
                error_log_message = f"{name_func} error: {error}. Inputs: args={args}, kwargs={kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(error_log_message + "\n")
                else:
                    print(error_log_message)

        return wrapper

    return log_decorator
