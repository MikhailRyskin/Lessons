from typing import Callable
import functools

app = {}


def callback(event: str) -> Callable:
    def call_decorator(func: Callable):
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            app[event] = func

        return wrapped_func

    return call_decorator


# Пример функции:
@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


# Основной код:
example()
route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')

#  не понял сути задания по примеру функции и основному коду.
#  Что такое app.get('//'), где example()?

#  стоит создать внешнюю переменную "app" (пустой словарь).
#  При помощи декоратора, необходимо просто заполнить словарь данными.
#  Где ключ это указанный текст в декораторе "//", а значение - функция, к которой мы применили декоратор.
#  Код из "Основной код", стоит скопировать в этот файл сразу =)
#  При помощи "route = app.get('//')", мы получаем значение словаря по ключу "//".
#  Т.к. значение, это функция, то стоит просто вызвать route как функцию.

# зачёт!
