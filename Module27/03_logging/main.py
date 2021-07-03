import functools
from typing import Callable, Any
import datetime


def logging(func: Callable) -> Any:
    """
    Декоратор. Выводит название функции и её документацию. Если во время выполнения
    Если во время выполнения декорируемой функции возникла ошибка,
    то в файл function_errors.log записываются название функции, название ошибки, дата и время возникновения ошибки.
    :param func:
    :return:
    """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        print(f'\nвыполняется функция: {func.__name__}{func.__doc__}')
        try:
            res = func(*args, **kwargs)
            return res
        except Exception as exc:
            with open('function_errors.log', 'a', encoding='utf-8') as log_file:
                log_str = f'функция:{func.__name__}, ошибка: {exc}, время:{datetime.datetime.now()}\n'
                log_file.write(log_str)

    return wrapped_func


@logging
def test_1():
    """
    функция возвращает сообщение
    :return:
    """
    return 'Выполнена тестовая функция 1'


@logging
def test_2():
    """
    функция добавляет "5" к строке
    :return:
    """
    a = 'Петя'
    b = a + 5
    return b


@logging
def test_3():
    """
    функция делит 10 на число
    :return:
    """
    a = 0
    b = 10 / a
    return b


@logging
def test_4():
    """
    функция складывает два числа
    :return:
    """
    a = 56
    b = 44
    c = a + b
    return c


print(test_1())
print(test_2())
print(test_3())
print(test_4())

# зачёт!
