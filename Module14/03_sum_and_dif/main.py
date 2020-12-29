def sum_all_numbers(n):
    sum_all = 0
    for k in range(n + 1):
        sum_all += k
    return sum_all


def sum_digits(n):
    sum_digit = 0
    while n != 0:
        sum_digit += n % 10
        n //= 10
    return sum_digit


def number_digits(n):
    number_digit = 0
    while n != 0:
        number_digit += 1
        n //= 10
    return number_digit


n = int(input('Введите число: '))
sum_all = sum_all_numbers(n)
print('Сумма чисел:', sum_all)
number_digit = number_digits(n)
print('Кол-во цифр в числе:', number_digit)
print('Разность суммы чисел и кол-ва цифр:', sum_all - number_digit)
sum_digit = sum_digits(n)
print('Сумма цифр:', sum_digit)
print('Разность суммы цифр и кол-ва цифр:', sum_digit - number_digit)

# зачёт!