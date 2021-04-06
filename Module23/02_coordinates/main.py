import random


def f(x, y):
    x += random.randint(0, 5)
    y += random.randint(0, 10)
    return x / y


def f2(x, y):
    x -= random.randint(0, 5)
    y -= random.randint(0, 10)
    return y / x


with open('coordinates.txt', 'r') as file, \
        open('result.txt', 'w') as file_2:
    for line in file:
        nums_list = line.split()
        try:
            res1 = f(int(nums_list[0]), int(nums_list[1]))
        except ZeroDivisionError:
            print("Произошло деление на 0 в функции f")
            res1 = None
        try:
            res2 = f2(int(nums_list[0]), int(nums_list[1]))
        except ZeroDivisionError:
            print("Произошло деление на 0 в функции f2")
            res2 = None
        number = random.randint(0, 100)
        my_list = [res1, res2, number]
        if res1 and res2:
            my_list = sorted([res1, res2, number])
        file_2.write(' '.join(str(my_list)) + '\n')

# зачёт!
