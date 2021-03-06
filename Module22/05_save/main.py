import os


def write_in_file(file_path, content):
    file = open(file_path, 'w', encoding='utf8')
    file.write(content)
    file.close()


text = input('Введите строку: ')

dir_path = input('Куда хотите сохранить документ?'
                 '   Введите последовательность папок (через пробел): ').split()
# dir_path = 'Skillbox PythonBasic Lessons Module22'.split()
abs_dir_path = os.path.abspath(os.path.join('/', *dir_path))
while not os.path.exists(abs_dir_path):
    print('Указанного пути не существует на диске!')
    dir_path = input('Куда хотите сохранить документ?'
                     ' Введите последовательность папок (через пробел): ').split()
    abs_dir_path = os.path.abspath(os.path.join('/', *dir_path))

file_name = input('Введите имя файла: ')
abs_file_path = os.path.join(abs_dir_path, file_name + '.txt')

# предлагаю подумать, как сократить количество следующего кода.
#  Возможно, стоит создать функцию для записи текста в файл.
if not os.path.exists(abs_file_path):
    write_in_file(abs_file_path, text)
    print('Файл успешно сохранён!')
else:
    rewriting = input('Вы действительно хотите перезаписать файл? ')
    if rewriting == 'да':
        write_in_file(abs_file_path, text)
        print('Файл успешно перезаписан!')

# зачёт!
