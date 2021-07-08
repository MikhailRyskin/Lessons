import functools


def singleton(cls):
    """
    Декоратор класса singleton.
    При множественном инициализации объекта этого класса будет сохранён только первый инстанс,
    а все остальные попытки создания будут возвращать первый экземпляр.
    :param cls:
    :return:
    """
    first_instance = {}

    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if cls.__name__ in first_instance:
            instance = first_instance[cls.__name__]
        else:
            instance = cls(*args, **kwargs)
            first_instance[cls.__name__] = instance
        return instance
    return wrapper


@singleton
class Example:
    pass


@singleton
class ExampleNew:
    pass


my_obj = Example()
my_another_obj = Example()
print(id(my_obj))
print(id(my_another_obj))
print(my_obj is my_another_obj)

obj_1 = ExampleNew()
obj_2 = ExampleNew()
print(id(obj_1))
print(id(obj_2))
obj_3 = ExampleNew()
print(id(obj_2))
print(obj_1 is obj_3)
