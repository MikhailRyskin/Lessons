import functools
from typing import Callable, Any


def how_are_you(func: Callable) -> Any:
    """
    Декоратор, задающий вопрос и добавляющий сообщение перед выполнением декорируемой функции.
    :param func:
    :return:
    """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        result = func(*args, **kwargs)
        return result

    return wrapped_func


@how_are_you
def test() -> None:
    print('<Тут что-то происходит...>')


@how_are_you
def test_1(num_1: float, num_2: float) -> None:
    total = num_1 + num_2
    print(f'Сумма чисел {num_1} и {num_2} равна {total}')


test()
print()
test_1(23, 8)

# зачёт!
