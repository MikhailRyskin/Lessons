def calc(check_line):
    operand_1, operation, operand_2 = check_line.split(' ')
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
        raise NameError(f'Неизвестная операция {operation} в строке: {check_line}')
    return value


result = 0
with open('calc.txt', 'r') as file:
    for line in file:
        line = line[:-1]
        try:
            result += calc(line)
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                print(f'Нет хватает операции или операндов в строке: {line}')
            else:
                print(f'Не могу преобразовать операнд к числу в строке: {line}')
        except NameError as exc:
            print(exc)
print(f'Результат вычисления: {result}')
