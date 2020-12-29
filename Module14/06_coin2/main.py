import math


def inside_circle(x, y, r):
    if math.sqrt(abs(x) ** 2 + abs(y) ** 2) > r:
        print('Монетки в области нет')
    else:
        print('Монетка где-то рядом')


x = float(input('Введите координату x: '))
y = float(input('Введите координату y: '))
r = float(input('Введите радиус: '))
inside_circle(x, y, r)

# зачёт!
