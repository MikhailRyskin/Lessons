file_name = input('Название файла: ')
special_char = '@№$%^&*()'
special_flag = False
for letter in special_char:
    if file_name.startswith(letter):
        special_flag = True
        break
if special_flag:
    print('\nОшибка: название начинается на один из специальных символов')
elif not (file_name.endswith('txt') or file_name.endswith('docx')):
    print('\nОшибка: неверное расширение файла. Ожидалось .txt или .docx')
else:
    print('\nФайл назван верно.')

# зачёт!
