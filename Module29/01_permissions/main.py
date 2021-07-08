from typing import Callable
import functools


def check_permission(user_name: str) -> Callable:
    """
    Декоратор, который проверяет есть ли у пользователя доступ к вызываемой функции.
    :param user_name: имя пользователя
    :return:
    """
    def check_decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            if user_name == 'admin':
                result = func(*args, **kwargs)
                return result
            else:
                # raise PermissionError(f'У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')
                print(f'PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')
        return wrapped_func
    return check_decorator


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
