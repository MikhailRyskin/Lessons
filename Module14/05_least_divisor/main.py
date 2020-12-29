import math


n = int(input('Введите число: '))
min_divider = n
for k in range(2, int(math.sqrt(n)) + 1):
    if n % k == 0:
        min_divider = k
        break
print('Наименьший делитель, отличный от единицы:', min_divider)
