import math


class Circle:

    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r
        self.s = math.pi * self.r ** 2
        self.p = 2 * math.pi * self.r

    def print_info(self):
        print(f'центр круга {self.x}:{self.y}, радиус {self.r}, площадь {self.s} периметр {self.p}')

    def increase(self, k):
        self.r *= k
        self.s = math.pi * self.r ** 2
        self.p = 2 * math.pi * self.r

    def is_intersect(self, other):
        if math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2) <= self.r + other.r:
            print('Окружности пересекаются')
        else:
            print('Окружности не пересекаются')


circle_1 = Circle(1, 2, 1)
circle_2 = Circle()
circle_1.print_info()
circle_2.print_info()
circle_1.is_intersect(circle_2)
circle_1.increase(5)
circle_1.print_info()
circle_1.is_intersect(circle_2)
