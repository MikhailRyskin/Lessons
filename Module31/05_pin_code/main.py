import itertools


if __name__ == '__main__':
    pin_list = list(itertools.product([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], repeat=4))
    print('количество вариантов кода:', len(pin_list))
