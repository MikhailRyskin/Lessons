def calc(check_line):
    try:
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
            raise NameError
    except (ValueError, NameError):
        print(f'Обнаружена ошибка в строке: {check_line}', end=' ')
        fix = input('Хотите исправить? ')
        if fix == 'да':
            fix_line = input('Введите исправленную строку: ')
            return calc(fix_line)
        else:
            return 0
    else:
        return value


result = 0
with open('calc.txt', 'r') as file:
    for line in file:
        line = line[:-1]
        result += calc(line)
print(f'Результат вычисления: {result}')
