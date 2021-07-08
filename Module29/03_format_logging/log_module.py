import time
from typing import Callable, Any
import functools
import datetime


def now_in_format(in_str: str) -> str:
    """
    Преобразует входной формат даты и времени и возвращает текущую  дату и время в правильном формате.
    :param in_str:
    :return:
    """
    out_str = ''
    for sym in in_str:
        if sym.isalpha():
            sym = '%' + sym
        out_str += sym
    now_str = datetime.datetime.strftime(datetime.datetime.now(), out_str)
    return now_str


def logging(time_mode: str, cls_name: str) -> Callable:
    def logging_decorator(func: Callable) -> Any:
        """
        Декоратор. Выводит класс и название метода, дату, время запуска и время работы.
        Если во время выполнения декорируемого метода возникла ошибка,
        то в файл function_errors.log записываются название класса и метода, название ошибки,
        дата и время возникновения ошибки.
        :param func:
        :return:
        """

        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            now = now_in_format(time_mode)
            print(f'- запускается "{cls_name}.{func.__name__}". Дата и время запуска: {now}')
            start_time = time.time()
            try:
                res = func(*args, **kwargs)
                print(f'- завершение "{cls_name}.{func.__name__}",'
                      f' время работы = {round(time.time()- start_time, 3)}s')
                return res
            except Exception as exc:
                with open('function_errors.log', 'a', encoding='utf-8') as log_file:
                    log_str = f'метод:{cls_name}.{func.__name__}, ошибка: {exc}, время:{datetime.datetime.now()}\n'
                    log_file.write(log_str)
        return wrapped_func
    return logging_decorator


def log_methods(time_mode: str) -> Callable:
    """
    Декоратор класса. Применяет декоратор logging ко всем методам класса.
    Передаётся формат вывода даты и времени логирования.
    Формат
    :param time_mode:
    :return:
    """
    def decorate(cls):
        for method_name in dir(cls):
            if not method_name.startswith('__'):
                cur_method = getattr(cls, method_name)
                decorator = logging(time_mode, cls.__name__)
                decorated_method = decorator(cur_method)
                setattr(cls, method_name, decorated_method)
        return cls
    return decorate
