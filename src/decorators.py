from collections.abc import Callable
from functools import wraps
from typing import Any


def log(filename: str | None = None) -> Callable:
    """Декоратор, который логирует работу функции и выводит результат в файл или в консоль"""

    def my_decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok\n")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} error: {e}. Input: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {e}. Input: {args}, {kwargs}\n")

        return wrapper

    return my_decorator


@log(filename="")
def my_function(x: int, y: int) -> int:
    """Функция, суммирующая два числа"""
    return x + y


my_function(1, 2)
