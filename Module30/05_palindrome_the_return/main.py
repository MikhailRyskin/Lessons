from collections import Counter


# обычная функция
def is_poly(input_str: str) -> bool:
    """
    определяет, можно ли из строки сделать палиндром
    :param input_str: входная строка
    :return:
    """
    char_dict = {}
    for sym in input_str:
        char_dict[sym] = char_dict.get(sym, 0) + 1
    odd_count = 0
    for sym_value in char_dict.values():
        if sym_value % 2 != 0:
            odd_count += 1
    if odd_count <= 1:
        return True
    else:
        return False


# с использованием collections
def can_be_poly(in_str: str) -> bool:
    """
    определяет, можно ли из строки сделать палиндром
    :param in_str: входная строка
    :return:
    """
    if len(list(filter(lambda x: x % 2 != 0, Counter(in_str).values()))) <= 1:
        return True
    else:
        return False


if __name__ == '__main__':

    str_1 = 'aadsdfggagf'

    print(is_poly(str_1))
    print(can_be_poly(str_1))

    str_2 = 'ababc'

    print(is_poly(str_2))
    print(can_be_poly(str_2))
