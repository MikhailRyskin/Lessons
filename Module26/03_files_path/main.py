import os
from collections.abc import Iterable

# TODO, начальную директорию стоит запрашивать у пользователя.
#  Т.к. такая директория может отсутствовать на другом ПК.
start_path = 'C:\Skillbox\PythonBasic\Lessons'
path_normalized = os.path.normpath(start_path)
dir_name = '04_players'


# TODO, os.walk отличный вариант =)
#  нам необходимо написать свою функцию на подобии os.walk. Которая будет рекурсивно обходить директории
#  и возвращать названия директорий, которые встречает на своём пути.

def files_path_generator(start_dir: str, dir_to_find: str) -> Iterable:
    for dir_path, dir_names, file_names in os.walk(start_dir):
        if dir_to_find in dir_names:
            print(f'Найдена папка {dir_to_find}')
            return
        for file in file_names:
            full_file_path = os.path.join(dir_path, file)
            yield full_file_path


file_gen = files_path_generator(path_normalized, dir_name)
for file_path in file_gen:
    print(file_path)
