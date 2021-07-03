import functools
from typing import Callable, Any


def debug(func: Callable) -> Any:
    """
    Декоратор, который выводит название, аргументы и результат декорируемой функции.
    :param func:
    :return:
    """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        args_kwargs = ','.join(f'"{str(elem)}"' for elem in args)
        for key, value in kwargs.items():
            args_kwargs += f',{key}={value} '
        print(f'Вызывается {func.__name__}({args_kwargs})')
        result = func(*args, **kwargs)
        print(f'"{func.__name__}" вернула значение "{result}"')
        return result

    return wrapped_func


@debug
def greeting(name: str, age: int = None) -> str:
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)

# зачёт!
