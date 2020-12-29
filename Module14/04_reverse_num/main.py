# принимает целое число, возвращает строку наоборот
def number_backward(n):
    backward = ''
    while n > 0:
        symbol = str(n % 10)
        backward += symbol
        n //= 10
    return backward


# принимает вещ. число в виде строки, возвращает две строки
def integer_fractional(n_str):
    integer_str = ''
    fractional_str = ''
    flag_integer = True
    for symbol in n_str:
        if flag_integer:
            if symbol != '.':
                integer_str += symbol
            else:
                flag_integer = False
        else:
            fractional_str += symbol
    return integer_str, fractional_str


a = input('Введите первое число: ')
integer_str, fractional_str = integer_fractional(a)
a_backward = number_backward(int(integer_str)) + '.' + number_backward(int(fractional_str))
b = input('Введите второе число: ')
integer_str, fractional_str = integer_fractional(b)
b_backward = number_backward(int(integer_str)) + '.' + number_backward(int(fractional_str))
print('Первое число наоборот: ', a_backward)
print('Второе число наоборот: ', b_backward)
print('Сумма:', float(a_backward) + float(b_backward))
