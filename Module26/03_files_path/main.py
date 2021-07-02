import os
from collections.abc import Iterable

#  начальную директорию стоит запрашивать у пользователя.
#  Т.к. такая директория может отсутствовать на другом ПК.

# start_path = 'C:\Skillbox\PythonBasic\Lessons'
start_path = input('Введите абсолютный путь начальноЙ директории: ')
path_normalized = os.path.normpath(start_path)
dir_name = '03_lucky_number'


#  os.walk отличный вариант =)
#  нам необходимо написать свою функцию на подобии os.walk. Которая будет рекурсивно обходить директории
#  и возвращать названия директорий, которые встречает на своём пути.
#  вообще-то нигде в задании не сказано, что нельзя использовать os.walk.
#  Попробовал сделать, без yield находит папку, с yield не работает. В чём ошибка?

# В случае, использования os.walk пропадает суть задания. Наша цель, научиться писать код. =)


# def files_path_generator(start_dir: str, dir_to_find: str) -> Iterable:
#     for dir_path, dir_names, file_names in os.walk(start_dir):
#         if dir_to_find in dir_names:
#             print(f'Найдена папка {dir_to_find}')
#             return
#         for file in file_names:
#             full_file_path = os.path.join(dir_path, file)
#             yield full_file_path

# file_gen = files_path_generator(path_normalized, dir_name)
# for file_path in file_gen:
#     print(file_path)

def dir_path_generator(start_dir: str, dir_to_find: str):
    list_dir = os.listdir(start_dir)
    if dir_to_find in list_dir:
        print(f'Найдена папка {dir_to_find}')
        return
    for elem in list_dir:
        if elem.startswith('.'):
            continue
        elem_path = os.path.join(start_dir, elem)
        # TODO, если elem_path это файл, стоит вернуть elem_path при помощи yield.
        if os.path.isdir(elem_path):
            print(elem_path)
            # yield elem_path
            # TODO, стоит реализовать цикл по возврату вызова функции ниже.
            #  Можно попробовать вместо range в цикле, использовать вызов нашей функции.
            #  Каждый элемент такого цикла стоит вернуть при помощи yield
            dir_path_generator(elem_path, dir_to_find)
    else:  # TODO, блок else с возвратом получился лишним.
        return


dir_path_generator(path_normalized, dir_name)

# dir_gen = dir_path_generator(path_normalized, dir_name)
# # for dir_path in dir_gen:
# #     print(dir_path)
