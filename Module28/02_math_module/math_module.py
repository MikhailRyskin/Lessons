import math
from abc import ABC


class MyMath(ABC):
    """
    Абстрактный класс. Предоставляет методы для вычисления параметров различных
    геометрических фигур.
    """

    # предлагаю попробовать использовать в ряде методах декоратор @staticmethod.
    #  В таком случае, cls будет лишним. =)
    @staticmethod
    def circle_len(radius: float) -> float:
        """
        вычисление длины окружности по формуле l = 2πr
        :param radius: радиус окружности
        :return: длина окружности
        """
        l_c = 2 * math.pi * radius
        return l_c

    @staticmethod
    def circle_sq(radius: float) -> float:
        """
        вычисление площади окружности по формуле s = πr**2
        :param radius: радиус окружности
        :return: площадь окружности
        """
        s = math.pi * radius ** 2
        return s

    @staticmethod
    def sphere_sq(radius: float) -> float:
        """
        # вычисление площади поверхности сферы по формуле S = 4πR**2
        :param radius: радиус сферы
        :return: площадь поверхности сферы
        """
        s = 4 * math.pi * radius ** 2
        return s

    @staticmethod
    def cube_vol(a: float) -> float:
        """
        вычисление объёма куба по формуле v = s**3
        :param a: сторона куба
        :return: объём куба
        """
        v = a ** 3
        return v
