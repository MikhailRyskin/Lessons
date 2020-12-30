import math


def min_divider(number):
    min_divider = number
    for k in range(2, int(math.sqrt(number)) + 1):
        if n % k == 0:
            min_divider = k
            break
    return min_divider


n = int(input('Введите число: '))
print('Наименьший делитель, отличный от единицы:', min_divider(n))

# зачёт!
