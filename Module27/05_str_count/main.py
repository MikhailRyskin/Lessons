import functools
from typing import Callable, Any, Dict
from collections import defaultdict

COUNT: Dict[str, int] = defaultdict(int)


def counter(func: Callable) -> Any:
    """
    Декоратор, считающий и выводящий количество вызовов декорируемой функции.
    :param func:
    :return:
    """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        res = func(*args, **kwargs)
        COUNT[func.__name__] += 1
        print(f'функция {func.__name__} вызывается в {COUNT[func.__name__]}-й раз')
        return res

    return wrapped_func


@counter
def test_1() -> str:
    return 'Выполнена тестовая функция 1'


@counter
def test_2() -> str:
    return 'Выполнена тестовая функция 2'


for num in range(6):
    print(test_1())
    if num % 2:
        print(test_2())

# зачёт!
