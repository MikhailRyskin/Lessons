import functools
import time
from typing import Callable, Any


def wait_3_sec(func: Callable) -> Any:
    """
    Декоратор, делающий паузу в 3 сек перед выполнением декорируемой функции
    :param func:
    :return:
    """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        time.sleep(3)
        result = func(*args, **kwargs)
        return result
    return wrapped_func


@wait_3_sec
def test() -> None:
    print('Выполнение тестовой функции')


print(time.time())
test()
print(time.time())

