with open('people.txt', 'r', encoding='utf8') as people_file, \
        open('errors.log', 'w', encoding='utf8') as errors_file:
    total_symbols = 0
    line_number = 0
    for line in people_file:
        line_number += 1
        # TODO, вместо среза, предлагаю попробовать использовать строковой метод rstrip()
        #  Дело в том, что методы более оптимизированы для работы со списками. Получится немного ускорить код.
        line = line[:-1]
        try:
            if len(line) < 3:
                raise ValueError(f'в строке {line_number} меньше 3-х символов')
            else:
                total_symbols += len(line)
        except ValueError as exc:
            print(exc)
            errors_file.write(str(exc) + '\n')
print('Всего символов в корректных строках:', total_symbols)
