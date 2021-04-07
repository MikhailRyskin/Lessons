def calc(check_line):
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
with open('calc.txt', 'r') as file:
    for line in file:
        line = line[:-1]
        try:
            result += calc(line)
        # предлагаю попробовать вызывать свои исключение с нужным текстом
        #  В таком случае, условный оператор получится лишний и наши ошибки можно будет ловить группой.
        except (IndexError, ValueError) as exc:
            print(exc)
print(f'Результат вычисления: {result}')

# зачёт!
