from typing import Generator


def prime_numbers_generator(n: int) -> Generator:
    """
    генератор простых чисел
    :param n: верхняя граница диапазона
    :return:
    """
    end = n
    start = 1
    prime_numbers = []
    while start < end:
        start += 1
        for prime in prime_numbers:
            if start % prime == 0:
                break
        else:
            prime_numbers.append(start)
            yield start


def prime_number(number: int) -> list:
    """
    функция, возвращающая список простых чисел.
    :param number: граница диапазона
    :return:
    """
    prime_list = []
    for num in range(2, number + 1):
        for n in range(2, num // 2 + 1):
            if num % n == 0:
                break
        else:
            prime_list.append(num)
    return prime_list


if __name__ == '__main__':

    range_1 = 1000

    for cur_number in prime_numbers_generator(range_1):
        print(cur_number, end=' ')

    print()
    print(*prime_number(range_1))

    prime_numbers_list = list(filter(lambda num: all(num % n != 0 for n in range(2, num // 2 + 1)),
                                     [num for num in range(2, range_1 + 1)]))
    print(*prime_numbers_list)
