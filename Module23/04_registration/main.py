def data_validation(data_line):
    if len(data_line.split(' ')) < 3:
        raise IndexError('НЕ присутствуют все три поля')
    name, email, age = data_line.split(' ')
    age = int(age)
    if age < 10 or age > 99:
        raise ValueError('поле возраст НЕ является числом от 10 до 99')
    elif not name.isalpha():
        raise NameError('поле имени содержит НЕ только буквы')
    elif not ('@' in email and '.' in email):
        raise SyntaxError('поле емейл НЕ содержит @ и .(точку)')
    else:
        return True


with open('registrations.txt', 'r', encoding='utf8') as reg_file,\
        open('registrations_good.log', 'w+', encoding='utf8') as good_file,\
        open('registrations_bad.log', 'w+', encoding='utf8') as bad_file:
    for line in reg_file:
        # вместо среза, предлагаю попробовать использовать строковой метод rstrip()
        #  Дело в том, что методы более оптимизированы для работы со списками. Получится немного ускорить код.
        line = line.rstrip()
        try:
            # условный оператор лишний, т.к. если функция вызовет исключение, то запись в файл не произойдёт.
            data_validation(line)
            good_file.write(line + '\n')
        except (IndexError, ValueError, NameError, SyntaxError) as exc:
            except_content = f'в записи {line} {exc}\n'
            bad_file.write(except_content)
