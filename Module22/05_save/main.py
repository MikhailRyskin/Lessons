import os

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
# print(abs_file_path)

if not os.path.exists(abs_file_path):
    out_file = open(abs_file_path, 'w', encoding='utf8')
    out_file.write(text)
    out_file.close()
    print('Файл успешно сохранён!')
else:
    rewriting = input('Вы действительно хотите перезаписать файл? ')
    if rewriting == 'да':
        out_file = open(abs_file_path, 'w', encoding='utf8')
        out_file.write(text)
        out_file.close()
        print('Файл успешно перезаписан!')
