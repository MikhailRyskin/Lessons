def calc(check_line):
    #     #  предлагаю попробовать разделить код и в функции calc только вызывать ошибки.
    #     #  А ловить их в основном цикле программы.

    if len(check_line.split(' ')) < 3:
        raise IndexError(f'Не хватает операции или операндов в строке: {line}')
    operand_1, operation, operand_2 = check_line.split(' ')
    if not operand_1.isdigit() or not operand_2.isdigit():
        raise ValueError(f'Не могу преобразовать операнд к числу в строке: {line}')
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    if operation == '+':
        value = operand_1 + operand_2
    elif operation == '-':
        value = operand_1 - operand_2
    elif operation == '/':
        value = operand_1 / operand_2
    elif operation == '*':
        value = operand_1 * operand_2
    elif operation == '//':
        value = operand_1 // operand_2
    elif operation == '%':
        value = operand_1 % operand_2
    else:
        raise ValueError(f'Неизвестная операция {operation} в строке: {check_line}')
    return value


result = 0
fix_flag = False
line_number = 0
with open('calc.txt', 'r') as file:
    file_content = file.readlines()
    while line_number < len(file_content):
        if not fix_flag:
            line = file_content[line_number]
            line_number += 1
        # вместо среза, предлагаю попробовать использовать строковой метод rstrip()
        #  Дело в том, что методы более оптимизированы для работы со списками. Получится немного ускорить код.
        line = line.rstrip()
        try:
            result += calc(line)
            fix_flag = False
        except (IndexError, ValueError):
            print(f'Обнаружена ошибка в строке: {line}', end=' ')
            fix = input('Хотите исправить? ')
            if fix == 'да':
                line = input('Введите исправленную строку: ')
                fix_flag = True
            else:
                fix_flag = False
                # предлагаю попробовать решить без рекурсии.
print(f'Результат вычисления: {result}')
