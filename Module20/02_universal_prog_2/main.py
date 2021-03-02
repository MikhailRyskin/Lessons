import math


def min_divider(number):
    min_divider = number
    for k in range(2, int(math.sqrt(number)) + 1):
        if number % k == 0:
            min_divider = k
            break
    return min_divider


def is_prime(number):
    prime = True
    min_div = min_divider(number)
    if min_div != number or min_div == 2:
        prime = False
    return prime


def cryptographic_func(inp_data):
    return [data for index, data in enumerate(inp_data) if is_prime(index)]


input_data = [0, 1, 2, 3, 4, 5, 6, 7, 8]
input_data_1 = 'абвгдеёжз'

crypt_list = cryptographic_func(input_data)
print(crypt_list)
crypt_list_1 = cryptographic_func(input_data_1)
print(crypt_list_1)
