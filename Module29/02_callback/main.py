from typing import Callable
import functools


def callback(event: str) -> Callable:
    def call_decorator(func: Callable):
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            if event == '//':
                result = func(*args, **kwargs)
                return result
            else:
                return None
        return wrapped_func
    return call_decorator


# Пример функции:
@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


# Основной код:
route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')

# TODO не понял сути задания по примеру функции и основному коду.
#  Что такое app.get('//'), где example()?
