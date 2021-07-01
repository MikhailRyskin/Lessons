import os
from collections.abc import Iterable


def str_count(file_path: str) -> int:
    with open(file_path, 'r', encoding='utf-8') as file_py:
        lines_count = 0
        for line in file_py:
            if line.rstrip():
                if not line.startswith('#'):
                    lines_count += 1
        return lines_count


def str_count_generator(start_dir: str) -> Iterable:
    for dir_path, dir_names, file_names in os.walk(start_dir):
        for file in file_names:
            # TODO, если file текст, то , стоит проверять последние символы текста при помощи строкового метода .endswith()
            #  Методы оптимизированы для работы с текстом и должны работать быстрее, чем срезы =)
            if file[-2:] == 'py':
                full_file_path = os.path.join(dir_path, file)
                number_str = str_count(full_file_path)
                yield full_file_path, number_str

# TODO, начальную директорию стоит запрашивать у пользователя.
#  Т.к. такая директория может отсутствовать на другом ПК.
start_path = 'C:\Skillbox\PythonBasic\Lessons\Module25'
path_normalized = os.path.normpath(start_path)

str_count_gen = str_count_generator(path_normalized)
files_count = 0
lines_value = 0

for file in str_count_gen:
    print(f'файл {file[0]} строк кода: {file[1]} ')
    files_count += 1
    lines_value += file[1]
print(f'В папке {path_normalized} содержится питоновских файлов: {files_count}, всего строк кода {lines_value}.')
